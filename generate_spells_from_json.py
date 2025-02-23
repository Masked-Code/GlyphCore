import json
import os
import logging
import re
from utils import (
    DnDSpell, SpellLevel, SchoolOfMagic, SpellcastingClass, Component,
    CastingTimeType, RangeType, DurationType, AreaOfEffectType, DamageType,
    SavingThrowType, AbilityScore
)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("spell_generation.log"),
        logging.StreamHandler()
    ]
)

# Load JSON data with UTF-8 encoding
def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                raise ValueError("JSON file is empty")
            data = json.loads(content)
            if "allSpells" not in data:
                raise KeyError("Missing 'allSpells' key in JSON")
            return data["allSpells"]
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"JSON parsing error at {e.pos}: {e.msg}. First 100 chars: {content[:100]}...")
        raise
    except Exception as e:
        logging.error(f"Unexpected error loading JSON: {e}")
        raise

# Map JSON level to SpellLevel enum
def get_spell_level(level_num, spell_name):
    level_map = {
        0: "CANTRIP",
        1: "LEVEL_1",
        2: "LEVEL_2",
        3: "LEVEL_3",
        4: "LEVEL_4",
        5: "LEVEL_5",
        6: "LEVEL_6",
        7: "LEVEL_7",
        8: "LEVEL_8",
        9: "LEVEL_9"
    }
    try:
        return f"SpellLevel.{level_map[level_num]}"
    except KeyError:
        logging.error(f"Spell '{spell_name}': Invalid level value '{level_num}'. Expected 0-9.")
        raise ValueError(f"Invalid level: {level_num}")

# Map JSON components to Component enum
def get_components(components_str, material, spell_name):
    try:
        comps = []
        components_list = [comp.strip() for comp in components_str.split(",")]
        if "Verbal" in components_list:
            comps.append("Component.VERBAL")
        if "Somatic" in components_list:
            comps.append("Component.SOMATIC")
        if "Material" in components_list:
            comps.append("Component.MATERIAL")
        material_value = material if "Material" in components_list and material != "none" else None
        return comps, material_value
    except AttributeError:
        logging.error(f"Spell '{spell_name}': Invalid components format '{components_str}'. Expected string.")
        raise ValueError(f"Invalid components: {components_str}")

# Parse range and AoE with enhanced handling
def parse_range(range_str, spell_name):
    try:
        range_str = range_str.strip().lower()
        if range_str.startswith("self"):
            range_type = "RangeType.SELF"
            distance = None
            if "(" in range_str:
                aoe_part = range_str.split("(")[1].replace(")", "").strip()
                match = re.match(r"(\d+[-\s]*(?:foot|ft|mile|radius))\s*(radius|cone|cube|line|sphere|hemisphere)?", aoe_part)
                if match:
                    size_str = match.group(1).replace(" ", "").replace("radius", "")
                    size = int(size_str.replace("foot", "").replace("ft", "").replace("mile", ""))
                    shape = match.group(2) or "sphere"  # Default to sphere if no shape
                    aoe_type = f"AreaOfEffectType.{shape.upper()}"
                    aoe_size = {"radius": size * 5280 if "mile" in size_str else size}
                else:
                    logging.warning(f"Spell '{spell_name}': Unrecognized AoE format in range '{range_str}'. Defaulting to NONE.")
                    aoe_type = "AreaOfEffectType.NONE"
                    aoe_size = None
            else:
                aoe_type = "AreaOfEffectType.NONE"
                aoe_size = None
        elif range_str == "touch":
            range_type = "RangeType.TOUCH"
            distance = None
            aoe_type = "AreaOfEffectType.NONE"
            aoe_size = None
        elif range_str == "sight":
            range_type = "RangeType.SIGHT"
            distance = None
            aoe_type = "AreaOfEffectType.NONE"
            aoe_size = None
        elif range_str in ["unlimited", "special", "school"]:
            range_type = "RangeType.FIXED" if range_str == "school" else "RangeType.SELF"
            distance = None
            aoe_type = "AreaOfEffectType.NONE"
            aoe_size = None
            logging.warning(f"Spell '{spell_name}': Unusual range '{range_str}'. Treating as SELF or FIXED with no distance.")
        else:
            range_type = "RangeType.FIXED"
            distance_str = range_str.replace("ft", "").replace("feet", "").split()[0]
            distance = int(distance_str)
            aoe_type = "AreaOfEffectType.NONE"
            aoe_size = None
        return range_type, distance, aoe_type, aoe_size
    except ValueError as e:
        logging.error(f"Spell '{spell_name}': Invalid range '{range_str}': {e}")
        raise
    except Exception as e:
        logging.error(f"Spell '{spell_name}': Error parsing range '{range_str}': {e}")
        raise

# Parse casting time
def parse_casting_time(casting_time_str, spell_name):
    try:
        casting_time_str = casting_time_str.strip().lower()
        standard_times = {
            "action": "ACTION",
            "bonus action": "BONUS_ACTION",
            "reaction": "REACTION",
            "1 minute": "MINUTE"
        }
        if casting_time_str in standard_times:
            return f"CastingTimeType.{standard_times[casting_time_str]}", None
        else:
            return "CastingTimeType.CUSTOM", casting_time_str
    except Exception as e:
        logging.error(f"Spell '{spell_name}': Error parsing casting time '{casting_time_str}': {e}")
        raise ValueError(f"Invalid casting time: {casting_time_str}")

# Parse duration
def parse_duration(duration_str, spell_name):
    try:
        duration_str = duration_str.strip()
        if "Concentration" in duration_str:
            duration_type = "DurationType.CONCENTRATION"
            duration_time = duration_str.replace("Concentration, ", "").replace("up to ", "")
        elif duration_str == "Instantaneous":
            duration_type = "DurationType.INSTANTANEOUS"
            duration_time = None
        else:
            duration_type = "DurationType.FIXED"
            duration_time = duration_str
        return duration_type, duration_time
    except Exception as e:
        logging.error(f"Spell '{spell_name}': Error parsing duration '{duration_str}': {e}")
        raise ValueError(f"Invalid duration: {duration_str}")

# Infer effect role, damage type, damage dice, and saving throw from description
def infer_spell_details(desc, spell_name):
    try:
        desc = desc.lower()
        effect_role = None
        damage_type = None
        damage_dice = None
        saving_throw = None

        if "damage" in desc:
            effect_role = "Damage"
        elif "heal" in desc or "hit point" in desc:
            effect_role = "Healing"
        elif "saving throw" in desc:
            effect_role = "Control"
        else:
            effect_role = "Utility"

        damage_types = {
            "acid": "ACID", "fire": "FIRE", "necrotic": "NECROTIC", "cold": "COLD",
            "lightning": "LIGHTNING", "thunder": "THUNDER", "force": "FORCE",
            "bludgeoning": "BLUDGEONING", "piercing": "PIERCING", "slashing": "SLASHING"
        }
        for dmg, enum in damage_types.items():
            if dmg in desc:
                damage_type = f"DamageType.{enum}"
                break
        for dice in ["1d4", "1d6", "1d8", "1d10", "1d12", "2d6", "3d8"]:
            if dice in desc:
                damage_dice = dice
                break

        save_types = {
            "dexterity": "DEXTERITY", "constitution": "CONSTITUTION", "wisdom": "WISDOM",
            "intelligence": "INTELLIGENCE", "strength": "STRENGTH", "charisma": "CHARISMA"
        }
        for save, enum in save_types.items():
            if f"{save} saving throw" in desc:
                saving_throw = f"SavingThrowType.{enum}"
                break

        return effect_role, damage_type, damage_dice, saving_throw
    except Exception as e:
        logging.error(f"Spell '{spell_name}': Error inferring details from description: {e}")
        raise

# Convert spell to function string with detailed error handling
def spell_to_function(spell):
    spell_name = spell.get("name", "Unknown")
    try:
        name = spell_name.replace(" ", "_").replace("'", "").replace("/", "_").lower()
        level = get_spell_level(spell["level"], spell_name)
        school = f"SchoolOfMagic.{spell['school'].upper()}"
        classes = [f"SpellcastingClass.{cls.strip().upper()}" for cls in spell["classes"].split(", ")]
        components, material = get_components(spell["components"], spell.get("Material:", spell.get("material", "none")), spell_name)
        casting_time, custom_casting_time = parse_casting_time(spell["castingTime"], spell_name)
        range_type, range_distance, aoe_type, aoe_size = parse_range(spell["range"], spell_name)
        duration_type, duration_time = parse_duration(spell["duration"], spell_name)
        effect_role, damage_type, damage_dice, saving_throw = infer_spell_details(spell["description"], spell_name)
        source_book = spell["source"]

        ability_map = {
            "ARTIFICER": "INTELLIGENCE", "WIZARD": "INTELLIGENCE", "SORCERER": "CHARISMA",
            "BARD": "CHARISMA", "WARLOCK": "CHARISMA", "CLERIC": "WISDOM", "DRUID": "WISDOM",
            "RANGER": "WISDOM", "PALADIN": "CHARISMA"
        }
        spellcasting_ability = "AbilityScore.INTELLIGENCE"
        for cls in classes:
            cls_name = cls.split(".")[1]
            if cls_name in ability_map:
                spellcasting_ability = f"AbilityScore.{ability_map[cls_name]}"
                break

        func = f"""def get_{name}():
    return DnDSpell(
        name="{spell_name}",
        level={level},
        school={school},
        casting_classes=[{', '.join(classes)}],
        components=[{', '.join(components)}],
"""
        if material:
            func += f"        material_component_desc=\"{material}\",\n"
        func += f"        casting_time={casting_time},\n"
        if custom_casting_time:
            func += f"        custom_casting_time=\"{custom_casting_time}\",\n"
        func += f"        range_type={range_type},\n"
        if range_distance is not None:
            func += f"        range_distance={range_distance},\n"
        func += f"        duration_type={duration_type},\n"
        if duration_time:
            func += f"        duration_time=\"{duration_time}\",\n"
        func += f"        targets=None,\n"
        func += f"        aoe_type={aoe_type},\n"
        if aoe_size:
            func += f"        aoe_size={aoe_size},\n"
        if damage_type:
            func += f"        damage_type={damage_type},\n"
        if damage_dice:
            func += f"        damage_dice=\"{damage_dice}\",\n"
        if effect_role:
            func += f"        effect_role=\"{effect_role}\",\n"
        func += f"        is_ritual={spell['ritual']},\n"
        func += f"        requires_attack_roll=False,\n"
        if saving_throw:
            func += f"        saving_throw={saving_throw},\n"
        func += f"        spellcasting_ability={spellcasting_ability},\n"
        func += f"        source_book=\"{source_book}\"\n"
        func += "    )\n"
        return func
    except KeyError as e:
        logging.error(f"Spell '{spell_name}': Missing required field {e}")
        return None
    except ValueError as e:
        logging.error(f"Spell '{spell_name}': Value error: {e}")
        return None
    except TypeError as e:
        logging.error(f"Spell '{spell_name}': Type error (possible list/str mismatch): {e}")
        return None
    except Exception as e:
        logging.error(f"Spell '{spell_name}': Unexpected error: {e}")
        return None

# Generate class-specific spell files with error tolerance
def generate_class_files(spell_data):
    imports = """from utils import (
    DnDSpell, SpellLevel, SchoolOfMagic, SpellcastingClass, Component,
    CastingTimeType, RangeType, DurationType, AreaOfEffectType, DamageType,
    SavingThrowType, AbilityScore
)
"""
    class_spells = {}
    failed_spells = 0
    for spell in spell_data:
        func = spell_to_function(spell)
        if func is None:
            failed_spells += 1
            continue
        classes = [cls.strip() for cls in spell["classes"].split(", ")]
        for cls in classes:
            if cls not in class_spells:
                class_spells[cls] = []
            class_spells[cls].append(func)

    for cls, spells in class_spells.items():
        file_content = imports + "\n"
        for spell_func in spells:
            file_content += spell_func + "\n"
        file_name = f"{cls.lower().replace(' ', '_')}_spells.py"
        try:
            with open(f"spells/{file_name}", "w") as f:
                f.write(file_content)
            logging.info(f"Generated {file_name} with {len(spells)} spells")
        except IOError as e:
            logging.error(f"Failed to write {file_name}: {e}")

    if failed_spells > 0:
        logging.warning(f"Processed {len(spell_data)} spells, {failed_spells} failed")
    else:
        logging.info("All spells processed successfully")

# Main execution
if __name__ == "__main__":
    try:
        spell_data = load_json("spells.json")
        generate_class_files(spell_data)
        logging.info("Spell generation completed")
    except UnicodeDecodeError as e:
        logging.error(f"Error decoding JSON file: {e}. Ensure the file is UTF-8 encoded.")
    except FileNotFoundError:
        logging.error("spells.json not found in the current directory.")
    except ValueError as e:
        logging.error(f"Value error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)  # Include stack trace