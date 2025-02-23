from utils import (
    DnDSpell, SpellLevel, SchoolOfMagic, SpellcastingClass, Component,
    CastingTimeType, RangeType, DurationType, AreaOfEffectType, DamageType,
    SavingThrowType, AbilityScore
)

def get_aid():
    return DnDSpell(
        name="Aid",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a tiny strip of white cloth",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_aura_of_life():
    return DnDSpell(
        name="Aura of Life",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.NECROTIC,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_aura_of_purity():
    return DnDSpell(
        name="Aura of Purity",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_aura_of_vitality():
    return DnDSpell(
        name="Aura of Vitality",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="2d6",
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_banishing_smite():
    return DnDSpell(
        name="Banishing Smite",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.BONUS_ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_banishment():
    return DnDSpell(
        name="Banishment",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="an item distasteful to the target",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CHARISMA,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_bless():
    return DnDSpell(
        name="Bless",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a sprinkling of holy water",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_blinding_smite():
    return DnDSpell(
        name="Blinding Smite",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.BONUS_ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="3d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_branding_smite():
    return DnDSpell(
        name="Branding Smite",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.BONUS_ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_circle_of_power():
    return DnDSpell(
        name="Circle of Power",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_command():
    return DnDSpell(
        name="Command",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.WARLOCK, SpellcastingClass.CLERIC],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="1 round",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_commune():
    return DnDSpell(
        name="Commune",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="incense and a vial of holy water or unholy water",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.SELF,
        duration_type=DurationType.FIXED,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_commune_with_nature():
    return DnDSpell(
        name="Commune with Nature",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.PALADIN, SpellcastingClass.RANGER],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.SELF,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_compelled_duel():
    return DnDSpell(
        name="Compelled Duel",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.BONUS_ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_create_food_and_water():
    return DnDSpell(
        name="Create Food and Water",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_crusaders_mantle():
    return DnDSpell(
        name="Crusader's Mantle",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d4",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_cure_wounds():
    return DnDSpell(
        name="Cure Wounds",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.PALADIN, SpellcastingClass.RANGER, SpellcastingClass.CLERIC, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d8",
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_daylight():
    return DnDSpell(
        name="Daylight",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.PALADIN, SpellcastingClass.RANGER, SpellcastingClass.CLERIC, SpellcastingClass.SORCERER],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_destructive_wave():
    return DnDSpell(
        name="Destructive Wave",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.NECROTIC,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_detect_evil_and_good():
    return DnDSpell(
        name="Detect Evil and Good",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_detect_magic():
    return DnDSpell(
        name="Detect Magic",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.PALADIN, SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.BARD, SpellcastingClass.RANGER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_detect_poison_and_disease():
    return DnDSpell(
        name="Detect Poison and Disease",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.PALADIN, SpellcastingClass.RANGER, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a yew leaf",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_dispel_evil_and_good():
    return DnDSpell(
        name="Dispel Evil and Good",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="holy water or powdered silver and iron",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CHARISMA,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_dispel_magic():
    return DnDSpell(
        name="Dispel Magic",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.PALADIN, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_divine_favor():
    return DnDSpell(
        name="Divine Favor",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.BONUS_ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d4",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_elemental_weapon():
    return DnDSpell(
        name="Elemental Weapon",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.ACID,
        damage_dice="1d4",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_find_steed():
    return DnDSpell(
        name="Find Steed",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_geas():
    return DnDSpell(
        name="Geas",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.WIZARD, SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="30 days",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_heroism():
    return DnDSpell(
        name="Heroism",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_lesser_restoration():
    return DnDSpell(
        name="Lesser Restoration",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.PALADIN, SpellcastingClass.RANGER],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_locate_creature():
    return DnDSpell(
        name="Locate Creature",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.PALADIN, SpellcastingClass.RANGER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of fur from a bloodhound",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_locate_object():
    return DnDSpell(
        name="Locate Object",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.PALADIN, SpellcastingClass.RANGER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a forked twig",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_magic_circle():
    return DnDSpell(
        name="Magic Circle",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.WARLOCK, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="holy water or powdered silver and iron worth at least 100 gp, which the spell consumes",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=10,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CHARISMA,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_magic_weapon():
    return DnDSpell(
        name="Magic Weapon",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.BONUS_ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_protection_from_evil_and_good():
    return DnDSpell(
        name="Protection from Evil and Good",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.PALADIN, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="holy water or powdered silver and iron, which the spell consumes",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_protection_from_poison():
    return DnDSpell(
        name="Protection from Poison",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.PALADIN, SpellcastingClass.RANGER, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_purify_food_and_drink():
    return DnDSpell(
        name="Purify Food and Drink",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.PALADIN],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=10,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_raise_dead():
    return DnDSpell(
        name="Raise Dead",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.BARD, SpellcastingClass.PALADIN],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a diamond worth at least 500 gp, which the spell consumes",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_remove_curse():
    return DnDSpell(
        name="Remove Curse",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.WARLOCK, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_revivify():
    return DnDSpell(
        name="Revivify",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="diamonds worth 300 gp, which the spell consumes",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_searing_smite():
    return DnDSpell(
        name="Searing Smite",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.BONUS_ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_shield_of_faith():
    return DnDSpell(
        name="Shield of Faith",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small parchment with a bit of holy text written on it",
        casting_time=CastingTimeType.BONUS_ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_spirit_guardians():
    return DnDSpell(
        name="Spirit Guardians",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a holy symbol",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=15,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.NECROTIC,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_staggering_smite():
    return DnDSpell(
        name="Staggering Smite",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 bonus action",
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_stoneskin():
    return DnDSpell(
        name="Stoneskin",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.PALADIN, SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.RANGER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="diamond dust worth 100 gp, which the spell consumes",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.TOUCH,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.BLUDGEONING,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_thunderous_smite():
    return DnDSpell(
        name="Thunderous Smite",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 bonus action",
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.THUNDER,
        damage_dice="2d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.STRENGTH,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_tree_stride():
    return DnDSpell(
        name="Tree Stride",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.PALADIN, SpellcastingClass.RANGER, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_warding_bond():
    return DnDSpell(
        name="Warding Bond",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pair of platinum rings worth at least 50 gp each, which you and target must wear for the duration",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_wrathful_smite():
    return DnDSpell(
        name="Wrathful Smite",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.PALADIN],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 bonus action",
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_zone_of_truth():
    return DnDSpell(
        name="Zone of Truth",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.PALADIN, SpellcastingClass.CLERIC, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CHARISMA,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

