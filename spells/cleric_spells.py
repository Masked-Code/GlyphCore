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

def get_animate_dead():
    return DnDSpell(
        name="Animate Dead",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a drop of blood, a piece of flesh, and a pinch of bone dust",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=10,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_antimagic_field():
    return DnDSpell(
        name="Antimagic Field",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of powdered iron or iron filings",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_astral_projection():
    return DnDSpell(
        name="Astral Projection",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="for each creature you affect with this spell, you must provide one jacinth worth at least 1,000 gp and one ornately carved bar of silver worth at least 100 gp, all of which the spell consumes",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 hour",
        range_type=RangeType.FIXED,
        range_distance=10,
        duration_type=DurationType.FIXED,
        duration_time="Special",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_augury():
    return DnDSpell(
        name="Augury",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="specially marked sticks, bones, or similar tokens worth at least 25 gp",
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

def get_bane():
    return DnDSpell(
        name="Bane",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a drop of blood",
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
        saving_throw=SavingThrowType.CHARISMA,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_beacon_of_hope():
    return DnDSpell(
        name="Beacon of Hope",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_bestow_curse():
    return DnDSpell(
        name="Bestow Curse",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.NECROTIC,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_blade_barrier():
    return DnDSpell(
        name="Blade Barrier",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=90,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.SLASHING,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_blight():
    return DnDSpell(
        name="Blight",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.NECROTIC,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_blindness_deafness():
    return DnDSpell(
        name="Blindness/Deafness",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_calm_emotions():
    return DnDSpell(
        name="Calm Emotions",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
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
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_clairvoyance():
    return DnDSpell(
        name="Clairvoyance",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a focus worth at least 100 gp, either a jeweled horn for hearing or a glass eye for scrying",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.FIXED,
        range_distance=1,
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

def get_conjure_celestial():
    return DnDSpell(
        name="Conjure Celestial",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=90,
        duration_type=DurationType.FIXED,
        duration_time="Conjuration, up to 1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_contagion():
    return DnDSpell(
        name="Contagion",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="7 days",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_continual_flame():
    return DnDSpell(
        name="Continual Flame",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="ruby dust worth 50 gp, which the spell consumes",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="Until dispelled",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_control_weather():
    return DnDSpell(
        name="Control Weather",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="burning incense and bits of earth and wood mixed in water",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.FIXED,
        range_distance=5,
        duration_type=DurationType.CONCENTRATION,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.COLD,
        damage_dice="1d4",
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_create_undead():
    return DnDSpell(
        name="Create Undead",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="one clay pot filled with grave dirt, one clay pot filled with brackish water, and one 150 gp black onyx stone for each corpse",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=10,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_create_or_destroy_water():
    return DnDSpell(
        name="Create or Destroy Water",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a drop of water if creating water or a few grains of sand if destroying it",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_death_ward():
    return DnDSpell(
        name="Death Ward",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_divination():
    return DnDSpell(
        name="Divination",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="incense and a sacrificial offering appropriate to your religion, together worth at least 25 gp, which the spell consumes",
        casting_time=CastingTimeType.ACTION,
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

def get_divine_word():
    return DnDSpell(
        name="Divine Word",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.BONUS_ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CHARISMA,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_earthquake():
    return DnDSpell(
        name="Earthquake",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of dirt, a piece of rock, and a lump of clay",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=500,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.BLUDGEONING,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_enhance_ability():
    return DnDSpell(
        name="Enhance Ability",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="fur or a feather from a beast",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="2d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_etherealness():
    return DnDSpell(
        name="Etherealness",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.TRANSMUATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.FIXED,
        duration_time="Up to 8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_feign_death():
    return DnDSpell(
        name="Feign Death",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of graveyard dirt",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_find_traps():
    return DnDSpell(
        name="Find Traps",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.RANGER],
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
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_find_the_path():
    return DnDSpell(
        name="Find the Path",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.DRUID],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a set of divinatory tools - such as bones, ivory sticks, cards, teeth, or carved runes - worth 100 gp and an object from the location you wish to find",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 day",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_fire_storm():
    return DnDSpell(
        name="Fire Storm",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.SORCERER],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=150,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_flame_strike():
    return DnDSpell(
        name="Flame Strike",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of sulfur",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_forbiddance():
    return DnDSpell(
        name="Forbiddance",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a sprinkling of holy water, rare incense, and powdered ruby worth at least 1,000 gp",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="1 day",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.NECROTIC,
        effect_role="Damage",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_freedom_of_movement():
    return DnDSpell(
        name="Freedom of Movement",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.RANGER],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a leather strap, bound around the arm or similar appendage",
        casting_time=CastingTimeType.ACTION,
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

def get_gate():
    return DnDSpell(
        name="Gate",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a diamond worth at least 5,000gp",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
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

def get_gentle_repose():
    return DnDSpell(
        name="Gentle Repose",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of salt and one copper piece placed on each of the corpse's eyes, which must remain there for the duration",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="10 days",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_glyph_of_warding():
    return DnDSpell(
        name="Glyph of Warding",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="incense and powdered diamond worth at least 200 gp, which the spell consumes",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 hour",
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="Until dispelled or triggered",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.ACID,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_greater_restoration():
    return DnDSpell(
        name="Greater Restoration",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="diamond dust worth 100 gp, which the spell consumes",
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

def get_guardian_of_faith():
    return DnDSpell(
        name="Guardian of Faith",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_guidance():
    return DnDSpell(
        name="Guidance",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
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

def get_hallow():
    return DnDSpell(
        name="Hallow",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="herbs, oils, and incense worth at least 1,000 gp, which the spell consumes",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="24 hours",
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="Until dispelled",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.BLUDGEONING,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CHARISMA,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_harm():
    return DnDSpell(
        name="Harm",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.NECROTIC,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_heal():
    return DnDSpell(
        name="Heal",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_healing_word():
    return DnDSpell(
        name="Healing Word",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.DRUID],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.BONUS_ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d4",
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_heroes_feast():
    return DnDSpell(
        name="Heroes' Feast",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a gem-encrusted bowl worth at least 1,000 gp, which the spell consumes",
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
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_holy_aura():
    return DnDSpell(
        name="Holy Aura",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a tiny reliquary worth at least 1,000 gp containing a sacred relic, such as a scrap of cloth from a saint's robe or a piece of parchment from a religious text",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_inflict_wounds():
    return DnDSpell(
        name="Inflict Wounds",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.NECROTIC,
        damage_dice="1d10",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_insect_plague():
    return DnDSpell(
        name="Insect Plague",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a few grains of sugar, some kernels of grain, and a smear of fat",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=300,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.PIERCING,
        damage_dice="1d10",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_legend_lore():
    return DnDSpell(
        name="Legend Lore",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="incense worth at least 250 gp, which the spell consumes, and four ivory strips worth at least 50 gp each",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.SELF,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
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

def get_light():
    return DnDSpell(
        name="Light",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.MATERIAL],
        material_component_desc="a firefly or phosphorescent moss",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
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

def get_mass_cure_wounds():
    return DnDSpell(
        name="Mass Cure Wounds",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=60,
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

def get_mass_heal():
    return DnDSpell(
        name="Mass Heal",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_mass_healing_word():
    return DnDSpell(
        name="Mass Healing Word",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.BONUS_ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d4",
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_meld_into_stone():
    return DnDSpell(
        name="Meld into Stone",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.BLUDGEONING,
        effect_role="Damage",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_mending():
    return DnDSpell(
        name="Mending",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="two lodestones",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_planar_ally():
    return DnDSpell(
        name="Planar Ally",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_planar_binding():
    return DnDSpell(
        name="Planar Binding",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc=" jewel worth at least 1,000 gp, which the spell consumes",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 hour",
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="24 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CHARISMA,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_plane_shift():
    return DnDSpell(
        name="Plane Shift",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a forked, metal rod worth at least 250 gp, attuned to a particular plane of existence",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CHARISMA,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_prayer_of_healing():
    return DnDSpell(
        name="Prayer of Healing",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
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

def get_protection_from_energy():
    return DnDSpell(
        name="Protection from Energy",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.DRUID, SpellcastingClass.RANGER, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.ACID,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_regenerate():
    return DnDSpell(
        name="Regenerate",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a prayer wheel and holy water",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
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

def get_resistance():
    return DnDSpell(
        name="Resistance",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a miniature cloak",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_resurrection():
    return DnDSpell(
        name="Resurrection",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a diamond worth at least 1,000 gp, which the spell consumes",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 hour",
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

def get_sacred_flame():
    return DnDSpell(
        name="Sacred Flame",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_scrying():
    return DnDSpell(
        name="Scrying",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC, SpellcastingClass.BARD, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a focus worth at least 1,000 gp, such as a crystal ball, a silver mirror, or a font filled with holy water",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_sending():
    return DnDSpell(
        name="Sending",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a short piece of fine copper wire",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.FIXED,
        duration_time="1 round",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
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

def get_silence():
    return DnDSpell(
        name="Silence",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC, SpellcastingClass.RANGER],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.THUNDER,
        effect_role="Damage",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_spare_the_dying():
    return DnDSpell(
        name="Spare the Dying",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
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

def get_speak_with_dead():
    return DnDSpell(
        name="Speak with Dead",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="burning incense",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=10,
        duration_type=DurationType.FIXED,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_spike_growth():
    return DnDSpell(
        name="Spike Growth",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.RANGER, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="seven sharp thorns or seven small twigs, each sharpened to a point",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=150,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.PIERCING,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_spiritual_weapon():
    return DnDSpell(
        name="Spiritual Weapon",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 bonus action",
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_stone_shape():
    return DnDSpell(
        name="Stone Shape",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="soft clay, which must be worked into roughly the desired shape of the stone object",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_suggestion():
    return DnDSpell(
        name="Suggestion",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.BARD, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.MATERIAL],
        material_component_desc="range",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.CONCENTRATION,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_symbol():
    return DnDSpell(
        name="Symbol",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.CLERIC, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="range",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="Until dispelled or triggered",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_teleportation_circle():
    return DnDSpell(
        name="Teleportation Circle",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.MATERIAL],
        material_component_desc="rare chalks and inks infused with precious gems with 50 gp, which the spell consumes",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=10,
        duration_type=DurationType.FIXED,
        duration_time="1 round",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_thaumaturgy():
    return DnDSpell(
        name="Thaumaturgy",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="Up to 1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.THUNDER,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_thunderwave():
    return DnDSpell(
        name="Thunderwave",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.BARD, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=15,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.THUNDER,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_tongues():
    return DnDSpell(
        name="Tongues",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.MATERIAL],
        material_component_desc="a small clay model of a ziggurat",
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

def get_true_resurrection():
    return DnDSpell(
        name="True Resurrection",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a sprinkle of holy water and diamonds worth at least 25,000 gp, which the spell consumes",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 hour",
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_true_seeing():
    return DnDSpell(
        name="True Seeing",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="an ointment for the eyes that costs 25 gp, is made from mushroom powder, saffron, and fat, and is consumed by the spell",
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

def get_vampiric_touch():
    return DnDSpell(
        name="Vampiric Touch",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.CLERIC, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.NECROTIC,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_wall_of_fire():
    return DnDSpell(
        name="Wall of Fire",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.CLERIC, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small piece of phosphorus",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
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

def get_water_walk():
    return DnDSpell(
        name="Water Walk",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.RANGER, SpellcastingClass.CLERIC, SpellcastingClass.SORCERER],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a piece of cork",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.ACID,
        effect_role="Damage",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_wind_wall():
    return DnDSpell(
        name="Wind Wall",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.RANGER, SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a tiny fan and a feather of exotic origin",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.BLUDGEONING,
        damage_dice="3d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.STRENGTH,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_word_of_recall():
    return DnDSpell(
        name="Word of Recall",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.CLERIC],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=5,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
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

