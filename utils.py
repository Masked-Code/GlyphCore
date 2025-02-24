from enum import Enum
from typing import List, Optional, Dict, Union
from PIL import Image, ImageDraw
import math

class SpellLevel(Enum):
    CANTRIP = 0
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4
    LEVEL_5 = 5
    LEVEL_6 = 6
    LEVEL_7 = 7
    LEVEL_8 = 8
    LEVEL_9 = 9

class SchoolOfMagic(Enum):
    ABJURATION = "Abjuration"
    CONJURATION = "Conjuration"
    DIVINATION = "Divination"
    ENCHANTMENT = "Enchantment"
    EVOCATION = "Evocation"
    ILLUSION = "Illusion"
    NECROMANCY = "Necromancy"
    TRANSMUTATION = "Transmutation"

class SpellcastingClass(Enum):
    ARTIFICER = "Artificer"
    BARD = "Bard"
    CLERIC = "Cleric"
    DRUID = "Druid"
    PALADIN = "Paladin"
    RANGER = "Ranger"
    SORCERER = "Sorcerer"
    WARLOCK = "Warlock"
    WIZARD = "Wizard"

class Component(Enum):
    VERBAL = "V"
    SOMATIC = "S"
    MATERIAL = "M"

class CastingTimeType(Enum):
    ACTION = "1 Action"
    BONUS_ACTION = "1 Bonus Action"
    REACTION = "1 Reaction"
    MINUTE = "1 Minute"
    CUSTOM = "Custom"

class RangeType(Enum):
    SELF = "Self"
    TOUCH = "Touch"
    FIXED = "Fixed"
    SIGHT = "Sight"

class DurationType(Enum):
    INSTANTANEOUS = "Instantaneous"
    CONCENTRATION = "Concentration"
    FIXED = "Fixed"
    UNTIL_DISPELLED = "Until Dispelled"

class AreaOfEffectType(Enum):
    NONE = "None"
    CONE = "Cone"
    CUBE = "Cube"
    CYLINDER = "Cylinder"
    LINE = "Line"
    SPHERE = "Sphere"

class DamageType(Enum):
    ACID = "Acid"
    BLUDGEONING = "Bludgeoning"
    COLD = "Cold"
    FIRE = "Fire"
    FORCE = "Force"
    LIGHTNING = "Lightning"
    NECROTIC = "Necrotic"
    POISON = "Poison"
    PSYCHIC = "Psychic"
    RADIANT = "Radiant"
    SLASHING = "Slashing"
    PIERCING = "Piercing"
    THUNDER = "Thunder"

class SavingThrowType(Enum):
    STRENGTH = "Strength"
    DEXTERITY = "Dexterity"
    CONSTITUTION = "Constitution"
    INTELLIGENCE = "Intelligence"
    WISDOM = "Wisdom"
    CHARISMA = "Charisma"

class AbilityScore(Enum):
    INTELLIGENCE = "Intelligence"
    WISDOM = "Wisdom"
    CHARISMA = "Charisma"

class Metamagic(Enum):
    TWINNED = "Twinned Spell"
    QUICKENED = "Quickened Spell"
    SUBTLE = "Subtle Spell"
    HEIGHTENED = "Heightened Spell"

class DnDSpell:
    def __init__(
        self,
        name: str,
        level: SpellLevel,
        school: SchoolOfMagic,
        casting_classes: List[SpellcastingClass],
        components: List[Component],
        material_component_desc: Optional[str] = None,
        casting_time: CastingTimeType = CastingTimeType.ACTION,
        custom_casting_time: Optional[str] = None,
        range_type: RangeType = RangeType.SELF,
        range_distance: Optional[int] = None,
        duration_type: DurationType = DurationType.INSTANTANEOUS,
        duration_time: Optional[str] = None, 
        targets: Optional[int] = None,
        aoe_type: AreaOfEffectType = AreaOfEffectType.NONE,
        aoe_size: Optional[Dict[str, int]] = None,
        damage_type: Optional[DamageType] = None,
        damage_dice: Optional[str] = None,
        effect_role: Optional[str] = None,
        is_ritual: bool = False,
        requires_attack_roll: bool = False,
        saving_throw: Optional[SavingThrowType] = None,
        spellcasting_ability: AbilityScore = AbilityScore.INTELLIGENCE,
        metamagic_options: Optional[List[Metamagic]] = None,
        source_book: str = "Player's Handbook"
    ):
        """Initialize a D&D spell with all its properties."""
        self.name = name
        self.level = level
        self.school = school
        self.casting_classes = casting_classes
        self.components = components
        self.material_component_desc = material_component_desc
        self.casting_time = casting_time
        self.custom_casting_time = custom_casting_time if casting_time == CastingTimeType.CUSTOM else None
        self.range_type = range_type
        self.range_distance = range_distance if range_type == RangeType.FIXED else None
        self.duration_type = duration_type
        self.duration_time = duration_time
        self.targets = targets
        self.aoe_type = aoe_type
        self.aoe_size = aoe_size if aoe_type != AreaOfEffectType.NONE else None
        self.damage_type = damage_type
        self.damage_dice = damage_dice
        self.effect_role = effect_role
        self.is_ritual = is_ritual
        self.requires_attack_roll = requires_attack_roll
        self.saving_throw = saving_throw
        self.spellcasting_ability = spellcasting_ability
        self.metamagic_options = metamagic_options if metamagic_options else []
        self.source_book = source_book

    def __str__(self) -> str:
        """String representation of the spell."""
        output = f"{self.name} (Level {self.level.value})\n"
        output += f"School: {self.school.value}\n"
        output += f"Classes: {', '.join([cls.value for cls in self.casting_classes])}\n"
        output += f"Components: {', '.join([comp.value for comp in self.components])}\n"
        if self.material_component_desc:
            output += f"Material: {self.material_component_desc}\n"
        output += f"Casting Time: {self.casting_time.value if self.casting_time != CastingTimeType.CUSTOM else self.custom_casting_time}\n"
        output += f"Range: {self.range_type.value}{' ' + str(self.range_distance) + ' ft' if self.range_distance else ''}\n"
        output += f"Duration: {self.duration_type.value}{' up to ' + self.duration_time if self.duration_time else ''}\n"
        if self.targets:
            output += f"Targets: {self.targets}\n"
        if self.aoe_type != AreaOfEffectType.NONE:
            output += f"Area: {self.aoe_type.value} {self.aoe_size}\n"
        if self.damage_type:
            output += f"Damage: {self.damage_dice} {self.damage_type.value}\n"
        if self.effect_role:
            output += f"Effect: {self.effect_role}\n"
        output += f"Ritual: {self.is_ritual}\n"
        output += f"Attack Roll: {self.requires_attack_roll}\n"
        if self.saving_throw:
            output += f"Saving Throw: {self.saving_throw.value}\n"
        output += f"Spellcasting Ability: {self.spellcasting_ability.value}\n"
        if self.metamagic_options:
            output += f"Metamagic: {', '.join([meta.value for meta in self.metamagic_options])}\n"
        output += f"Source: {self.source_book}"
        return output

SCHOOL_SHAPES = {
    SchoolOfMagic.ABJURATION: 4,  
    SchoolOfMagic.CONJURATION: 6, 
    SchoolOfMagic.DIVINATION: 8,   
    SchoolOfMagic.ENCHANTMENT: 5, 
    SchoolOfMagic.EVOCATION: 0,    
    SchoolOfMagic.ILLUSION: 7,
    SchoolOfMagic.NECROMANCY: 5,  
    SchoolOfMagic.TRANSMUTATION: 3
}

class RuneGenerator:
    def __init__(self, spell: DnDSpell):
        self.spell = spell
        self.image_size = 800 
        self.center = (self.image_size // 2, self.image_size // 2)
        self.base_radius = min(150 + (self.spell.range_distance or 0) // 5, 350) 

    def draw_shape(self, draw: ImageDraw.Draw, sides: int):
        """Draw the base shape based on school of magic."""
        if sides == 0: 
            draw.ellipse(
                [self.center[0] - self.base_radius, self.center[1] - self.base_radius,
                 self.center[0] + self.base_radius, self.center[1] + self.base_radius],
                outline="black", width=3  
            )
        else:  
            angle_step = 360 / sides
            points = [
                (self.center[0] + self.base_radius * math.cos(math.radians(angle_step * i)),
                 self.center[1] + self.base_radius * math.sin(math.radians(angle_step * i)))
                for i in range(sides)
            ]
            draw.polygon(points, outline="black", width=3) 

    def draw_damage_pattern(self, draw: ImageDraw.Draw):
        """Draw a pattern inside the shape based on damage type."""
        inner_radius = self.base_radius * 0.8 
        damage_type = self.spell.damage_type

        if damage_type == DamageType.ACID:
            for i in range(-int(inner_radius), int(inner_radius), 15):
                draw.line(
                    [self.center[0] + i, self.center[1] - inner_radius,
                     self.center[0] + i + inner_radius, self.center[1] + inner_radius],
                    fill="black", width=2  
                )
        elif damage_type == DamageType.FIRE:
            for i in range(0, 360, 60):
                angle = math.radians(i)
                p1 = (self.center[0] + inner_radius * 0.5 * math.cos(angle),
                      self.center[1] + inner_radius * 0.5 * math.sin(angle))
                p2 = (self.center[0] + inner_radius * 0.7 * math.cos(angle + 0.2),
                      self.center[1] + inner_radius * 0.7 * math.sin(angle + 0.2))
                p3 = (self.center[0] + inner_radius * 0.7 * math.cos(angle - 0.2),
                      self.center[1] + inner_radius * 0.7 * math.sin(angle - 0.2))
                draw.polygon([p1, p2, p3], fill="black")
        elif damage_type == DamageType.COLD:
            for x in range(-int(inner_radius), int(inner_radius), 15):
                for y in range(-int(inner_radius), int(inner_radius), 15):
                    if math.sqrt(x**2 + y**2) < inner_radius:
                        draw.ellipse(
                            [self.center[0] + x - 3, self.center[1] + y - 3,
                             self.center[0] + x + 3, self.center[1] + y + 3],  
                            fill="black"
                        )
        elif damage_type == DamageType.LIGHTNING:
            for i in range(0, 3):
                angle = math.radians(i * 120)
                start = (self.center[0] + inner_radius * 0.5 * math.cos(angle),
                         self.center[1] + inner_radius * 0.5 * math.sin(angle))
                mid = (self.center[0] + inner_radius * 0.7 * math.cos(angle + 0.1),
                       self.center[1] + inner_radius * 0.7 * math.sin(angle + 0.1))
                end = (self.center[0] + inner_radius * math.cos(angle),
                       self.center[1] + inner_radius * math.sin(angle))
                draw.line([start, mid, end], fill="black", width=2)
        elif damage_type == DamageType.FORCE:
            for r in range(15, int(inner_radius), 15):
                draw.ellipse(
                    [self.center[0] - r, self.center[1] - r,
                     self.center[0] + r, self.center[1] + r],
                    outline="black", width=2 
                )
        elif damage_type == DamageType.NECROTIC:
            for i in range(-int(inner_radius), int(inner_radius), 15):
                draw.line(
                    [self.center[0] + i, self.center[1] - inner_radius,
                     self.center[0] + i + inner_radius, self.center[1] + inner_radius],
                    fill="black", width=2 
                )
                draw.line(
                    [self.center[0] + i, self.center[1] + inner_radius,
                     self.center[0] + i + inner_radius, self.center[1] - inner_radius],
                    fill="black", width=2
                )

    def draw_level_lines(self, draw: ImageDraw.Draw):
        """Draw radiating lines based on spell level."""
        if self.spell.level == SpellLevel.CANTRIP:
            return 
        num_lines = self.spell.level.value
        angle_step = 360 / num_lines
        for i in range(num_lines):
            angle = math.radians(angle_step * i)
            start = (self.center[0] + self.base_radius * math.cos(angle),
                     self.center[1] + self.base_radius * math.sin(angle))
            end = (self.center[0] + (self.base_radius + 40) * math.cos(angle), 
                   self.center[1] + (self.base_radius + 40) * math.sin(angle))
            draw.line([start, end], fill="black", width=3)  

    def draw_border(self, draw: ImageDraw.Draw):
        """Draw border style based on casting time."""
        border_radius = self.base_radius + 20  
        if self.spell.casting_time == CastingTimeType.ACTION:
            draw.ellipse(
                [self.center[0] - border_radius, self.center[1] - border_radius,
                 self.center[0] + border_radius, self.center[1] + border_radius],
                outline="black", width=3 
            )
        elif self.spell.casting_time == CastingTimeType.REACTION:
            for i in range(0, 360, 20):
                start_angle = math.radians(i)
                end_angle = math.radians(i + 10)
                draw.arc(
                    [self.center[0] - border_radius, self.center[1] - border_radius,
                     self.center[0] + border_radius, self.center[1] + border_radius],
                    start=i, end=i + 10, fill="black", width=3
                )

    def draw_duration_symbol(self, draw: ImageDraw.Draw):
        """Draw a central symbol based on duration."""
        if self.spell.duration_type == DurationType.INSTANTANEOUS:
            draw.ellipse(
                [self.center[0] - 10, self.center[1] - 10,
                 self.center[0] + 10, self.center[1] + 10],
                fill="black"
            )
        elif self.spell.duration_type == DurationType.CONCENTRATION:
            for i in range(0, 360, 10):
                angle = math.radians(i)
                r = i / 25 
                x = self.center[0] + r * math.cos(angle)
                y = self.center[1] + r * math.sin(angle)
                draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill="black")

    def draw_components(self, draw: ImageDraw.Draw):
        """Draw small icons for components near the edge."""
        offset = 0
        for component in self.spell.components:
            x = self.center[0] + (self.base_radius + 50) * math.cos(math.radians(offset))
            y = self.center[1] + (self.base_radius + 50) * math.sin(math.radians(offset))
            if component == Component.VERBAL:
                draw.arc([x - 10, y - 10, x + 10, y + 10], 0, 180, fill="black", width=3)
            elif component == Component.SOMATIC:
                draw.polygon([(x, y - 10), (x - 10, y + 10), (x + 10, y + 10)], fill="black") 
            elif component == Component.MATERIAL:
                draw.rectangle([x - 10, y - 10, x + 10, y + 10], fill="black") 
            offset += 45

    def generate_rune(self, filename: str = "rune.png"):
        """Generate and save the monochrome rune image."""
        image = Image.new("1", (self.image_size, self.image_size), 1) 
        draw = ImageDraw.Draw(image)
        sides = SCHOOL_SHAPES[self.spell.school]
        self.draw_shape(draw, sides)

        self.draw_damage_pattern(draw)

        self.draw_level_lines(draw)

        self.draw_border(draw)

        self.draw_duration_symbol(draw)

        self.draw_components(draw)

        image.save(f"runes/{filename}")
        print(f"Monochrome rune saved as {filename}")