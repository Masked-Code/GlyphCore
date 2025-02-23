from utils import (
    DnDSpell, SpellLevel, SchoolOfMagic, SpellcastingClass, Component,
    CastingTimeType, RangeType, DurationType, AreaOfEffectType, DamageType,
    SavingThrowType, AbilityScore
)
from typing import List
import json

def get_fireball():
    return DnDSpell(
        name="Fireball",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.SORCERER],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a tiny ball of bat guano and sulfur",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=150,
        duration_type=DurationType.INSTANTANEOUS,
        aoe_type=AreaOfEffectType.SPHERE,
        aoe_size={"radius": 40},
        damage_type=DamageType.FIRE,
        damage_dice="10d6",
        effect_role="Damage",
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_cure_wounds():
    return DnDSpell(
        name="Cure Wounds",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=1,
        effect_role="Healing",
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_magic_missile():
    return DnDSpell(
        name="Magic Missile",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.SORCERER],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.INSTANTANEOUS,
        targets=3,
        damage_type=DamageType.FORCE,
        damage_dice="1d4 + 1",
        effect_role="Damage",
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_shield():
    return DnDSpell(
        name="Shield",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.SORCERER],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.REACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.FIXED,
        duration_time="1 round",
        effect_role="Buff",
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_invisibility():
    return DnDSpell(
        name="Invisibility",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.SORCERER, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="an eyelash encased in gum arabic",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=1,
        effect_role="Utility",
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_counterspell():
    return DnDSpell(
        name="Counterspell",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK],
        components=[Component.SOMATIC],
        casting_time=CastingTimeType.REACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        effect_role="Control",
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_wish():
    return DnDSpell(
        name="Wish",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.SORCERER],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.INSTANTANEOUS,
        effect_role="Utility",
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

KNOWN_SPELLS = {
    "fireball": get_fireball,
    "cure_wounds": get_cure_wounds,
    "magic_missile": get_magic_missile,
    "shield": get_shield,
    "invisibility": get_invisibility,
    "counterspell": get_counterspell,
    "wish": get_wish,
}

def load_spells_from_json(file_path: str) -> List[DnDSpell]:
    """Load spells from a JSON file and return a list of DnDSpell objects."""
    try:
        with open(file_path, 'r') as f:
            spell_data = json.load(f)
        
        spells = []
        for spell in spell_data:
            spells.append(DnDSpell(
                name=spell["name"],
                level=SpellLevel[spell["level"]],
                school=SchoolOfMagic[spell["school"]],
                casting_classes=[SpellcastingClass[cls] for cls in spell["casting_classes"]],
                components=[Component[comp] for comp in spell["components"]],
                material_component_desc=spell.get("material_component_desc"),
                casting_time=CastingTimeType[spell["casting_time"]],
                custom_casting_time=spell.get("custom_casting_time"),
                range_type=RangeType[spell["range_type"]],
                range_distance=spell.get("range_distance"),
                duration_type=DurationType[spell["duration_type"]],
                duration_time=spell.get("duration_time"),
                targets=spell.get("targets"),
                aoe_type=AreaOfEffectType[spell["aoe_type"]] if spell["aoe_type"] else AreaOfEffectType.NONE,
                aoe_size=spell.get("aoe_size"),
                damage_type=DamageType[spell["damage_type"]] if spell.get("damage_type") else None,
                damage_dice=spell.get("damage_dice"),
                effect_role=spell.get("effect_role"),
                is_ritual=spell.get("is_ritual", False),
                requires_attack_roll=spell.get("requires_attack_roll", False),
                saving_throw=SavingThrowType[spell["saving_throw"]] if spell.get("saving_throw") else None,
                spellcasting_ability=AbilityScore[spell["spellcasting_ability"]],
                metamagic_options=None,  # Add if needed
                source_book=spell.get("source_book", "Player's Handbook")
            ))
        return spells
    except FileNotFoundError:
        print(f"Spell file {file_path} not found.")
        return []
    except KeyError as e:
        print(f"Error in spell data format: missing or invalid key {e}")
        return []