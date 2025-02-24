from utils import (
    DnDSpell, SpellLevel, SchoolOfMagic, SpellcastingClass, Component,
    CastingTimeType, RangeType, DurationType, AreaOfEffectType, DamageType,
    SavingThrowType, AbilityScore
)

def get_animal_friendship():
    return DnDSpell(
        name="Animal Friendship",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.RANGER, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a morsel of food",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="24 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_animal_messenger():
    return DnDSpell(
        name="Animal Messenger",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.RANGER, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a morsel of food",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="24 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_animate_objects():
    return DnDSpell(
        name="Animate Objects",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="up ot 1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.BLUDGEONING,
        damage_dice="1d4",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_awaken():
    return DnDSpell(
        name="Awaken",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="an agate worth at least 1,000 gp, which the spell consumes",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="8 hours",
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

def get_blade_ward():
    return DnDSpell(
        name="Blade Ward",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.BARD, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.FIXED,
        duration_time="1 round",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.BLUDGEONING,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_charm_person():
    return DnDSpell(
        name="Charm Person",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.BARD, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
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

def get_cloud_of_daggers():
    return DnDSpell(
        name="Cloud of Daggers",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a sliver of glass",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.SLASHING,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_comprehend_languages():
    return DnDSpell(
        name="Comprehend Languages",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of soot and salt",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_compulsion():
    return DnDSpell(
        name="Compulsion",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_confusion():
    return DnDSpell(
        name="Confusion",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.BARD, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="three nut shells",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=90,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_crown_of_madness():
    return DnDSpell(
        name="Crown of Madness",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
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

def get_dancing_lights():
    return DnDSpell(
        name="Dancing Lights",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of phosphorus or wychwood, or a glowworm",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
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

def get_detect_thoughts():
    return DnDSpell(
        name="Detect Thoughts",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a copper piece",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_dimension_door():
    return DnDSpell(
        name="Dimension Door",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=500,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_disguise_self():
    return DnDSpell(
        name="Disguise Self",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
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

def get_dissonant_whispers():
    return DnDSpell(
        name="Dissonant Whispers",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD],
        components=[Component.VERBAL],
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
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_dominate_monster():
    return DnDSpell(
        name="Dominate Monster",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_dominate_person():
    return DnDSpell(
        name="Dominate Person",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
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

def get_dream():
    return DnDSpell(
        name="Dream",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a handful of sand, a dab of ink, and a writing quill plucked from a sleeping bird",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.FIXED,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_enthrall():
    return DnDSpell(
        name="Enthrall",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_eyebite():
    return DnDSpell(
        name="Eyebite",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
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

def get_faerie_fire():
    return DnDSpell(
        name="Faerie Fire",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.BARD],
        components=[Component.VERBAL],
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
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_fear():
    return DnDSpell(
        name="Fear",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD, SpellcastingClass.SORCERER],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a white feather or the heart of a hen",
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
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_feather_fall():
    return DnDSpell(
        name="Feather Fall",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.MATERIAL],
        material_component_desc="a white feather or the heart of a hen",
        casting_time=CastingTimeType.REACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_feeblemind():
    return DnDSpell(
        name="Feeblemind",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.DRUID, SpellcastingClass.WIZARD, SpellcastingClass.SORCERER],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a handful of clay, crystal, glass, or mineral spheres",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=150,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.INTELLIGENCE,
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

def get_forcecage():
    return DnDSpell(
        name="Forcecage",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="ruby dust worth 1,500gp",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=100,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CHARISMA,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_foresight():
    return DnDSpell(
        name="Foresight",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.DRUID, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a hummingbird feather",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_friends():
    return DnDSpell(
        name="Friends",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.BARD, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
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

def get_glibness():
    return DnDSpell(
        name="Glibness",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.BARD],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
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

def get_greater_invisibility():
    return DnDSpell(
        name="Greater Invisibility",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
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
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_guards_and_wards():
    return DnDSpell(
        name="Guards and Wards",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="burning incense, a small measure of brimstone and oil, a knotted string, a small amount of umber hulk blood, and a small silver rod worth at least 10 gp",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="24 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_hallucinatory_terrain():
    return DnDSpell(
        name="Hallucinatory Terrain",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.DRUID, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a stone, a twig, and a bit of green plant",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.FIXED,
        range_distance=300,
        duration_type=DurationType.FIXED,
        duration_time="24 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_heat_metal():
    return DnDSpell(
        name="Heat Metal",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.DRUID],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a piece of iron and a flame",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.CONCENTRATION,
        duration_time="up ot 1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
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

def get_hold_monster():
    return DnDSpell(
        name="Hold Monster",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small, straight piece of iron",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=90,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_hold_person():
    return DnDSpell(
        name="Hold Person",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small, straight piece of iron",
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
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_hypnotic_pattern():
    return DnDSpell(
        name="Hypnotic Pattern",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
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

def get_identify():
    return DnDSpell(
        name="Identify",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pearl worth at least 100 gp and an owl feather",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_illusory_script():
    return DnDSpell(
        name="Illusory Script",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="10 days",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_invisibility():
    return DnDSpell(
        name="Invisibility",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="an eyelash encased in gum arabic",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
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

def get_knock():
    return DnDSpell(
        name="Knock",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.TRANSMUATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_leomunds_tiny_hut():
    return DnDSpell(
        name="Leomund's Tiny Hut",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small crystal bead",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=10,
        duration_type=DurationType.FIXED,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
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

def get_locate_animals_or_plants():
    return DnDSpell(
        name="Locate Animals or Plants",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.RANGER, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of fur from a bloodhound",
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

def get_longstrider():
    return DnDSpell(
        name="Longstrider",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.DRUID, SpellcastingClass.RANGER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of dirt",
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

def get_mage_hand():
    return DnDSpell(
        name="Mage Hand",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.BARD, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_magic_mouth():
    return DnDSpell(
        name="Magic Mouth",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small bit of honeycomb and jade dust worth at least 10 gp, which the spell consumes",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="Until dispelled",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_major_image():
    return DnDSpell(
        name="Major Image",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of fleece",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.COLD,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
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

def get_mass_suggestion():
    return DnDSpell(
        name="Mass Suggestion",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.MATERIAL],
        material_component_desc="a snake's tongue and either a bit of honeycomb or a drop of sweet oil",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="24 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_message():
    return DnDSpell(
        name="Message",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a short piece of copper wire",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
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

def get_mind_blank():
    return DnDSpell(
        name="Mind Blank",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="24 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_minor_illusion():
    return DnDSpell(
        name="Minor Illusion",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.BARD, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of fleece",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_mirage_arcane():
    return DnDSpell(
        name="Mirage Arcane",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.SIGHT,
        duration_type=DurationType.FIXED,
        duration_time="10 days",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_mislead():
    return DnDSpell(
        name="Mislead",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_modify_memory():
    return DnDSpell(
        name="Modify Memory",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.ACID,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_mordenkainens_magnificent_mansion():
    return DnDSpell(
        name="Mordenkainen's Magnificent Mansion",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a miniature portal carved from ivory, a small piece of polished marble, and a tiny silver spoon, each item worth at least 5 gp",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=300,
        duration_type=DurationType.FIXED,
        duration_time="24 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_mordenkainens_sword():
    return DnDSpell(
        name="Mordenkainen's Sword",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a miniature platinum sword with a grip and pommel of copper and zinc, worth 250 gp",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_nondetection():
    return DnDSpell(
        name="Nondetection",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.RANGER, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of diamond dust worth 25 gp sprinkled over the target, which the spell consumes",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_ottos_irresistible_dance():
    return DnDSpell(
        name="Otto's Irresistible Dance",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL],
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
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_phantasmal_force():
    return DnDSpell(
        name="Phantasmal Force",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of fleece",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.ACID,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.INTELLIGENCE,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_plant_growth():
    return DnDSpell(
        name="Plant Growth",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.DRUID, SpellcastingClass.RANGER],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action or 8 hours",
        range_type=RangeType.FIXED,
        range_distance=150,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_polymorph():
    return DnDSpell(
        name="Polymorph",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a caterpillar cocoon",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_power_word_heal():
    return DnDSpell(
        name="Power Word Heal",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC],
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

def get_power_word_kill():
    return DnDSpell(
        name="Power Word Kill",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_power_word_stun():
    return DnDSpell(
        name="Power Word Stun",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_prestidigitation():
    return DnDSpell(
        name="Prestidigitation",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.BARD, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=10,
        duration_type=DurationType.FIXED,
        duration_time="Up to 1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_programmed_illusion():
    return DnDSpell(
        name="Programmed Illusion",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="A bit of fleece and jade dust worth at least 25 gp ",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.FIXED,
        duration_time="Until dispelled",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_project_image():
    return DnDSpell(
        name="Project Image",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small replica of you made from materials worth at least 5 gp",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=500,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 day",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_see_invisibility():
    return DnDSpell(
        name="See Invisibility",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of Talc and a small sprinkling of powdered silver",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
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

def get_seeming():
    return DnDSpell(
        name="Seeming",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CHARISMA,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_shatter():
    return DnDSpell(
        name="Shatter",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a chip of mica",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.THUNDER,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
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

def get_silent_image():
    return DnDSpell(
        name="Silent Image",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of fleece",
        casting_time=CastingTimeType.ACTION,
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

def get_sleep():
    return DnDSpell(
        name="Sleep",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of find sand, rose petals, or a cricket",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=90,
        duration_type=DurationType.FIXED,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_speak_with_animals():
    return DnDSpell(
        name="Speak with Animals",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.DRUID, SpellcastingClass.RANGER],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.FIXED,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_speak_with_plants():
    return DnDSpell(
        name="Speak with Plants",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.BARD, SpellcastingClass.DRUID, SpellcastingClass.RANGER],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
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

def get_stinking_cloud():
    return DnDSpell(
        name="Stinking Cloud",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a rotten egg or several skunk cabbage leaves",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=90,
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

def get_teleport():
    return DnDSpell(
        name="Teleport",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=10,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        damage_dice="1d10",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_true_polymorph():
    return DnDSpell(
        name="True Polymorph",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a drop of mercury, a dollop of gum arabic, and a wisp of smoke",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_true_strike():
    return DnDSpell(
        name="True Strike",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.BARD, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 round",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_unseen_servant():
    return DnDSpell(
        name="Unseen Servant",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD, SpellcastingClass.BARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a piece of string and a bit of wood",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        effect_role="Healing",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_vicious_mockery():
    return DnDSpell(
        name="Vicious Mockery",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.BARD],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d4",
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


KNOWN_BARD_SPELLS = {
    "animal_friendship": get_animal_friendship,
    "animal_messenger": get_animal_messenger,
    "animate_objects": get_animate_objects,
    "awaken": get_awaken,
    "bane": get_bane,
    "bestow_curse": get_bestow_curse,
    "blade_ward": get_blade_ward,
    "blindness_deafness": get_blindness_deafness,
    "calm_emotions": get_calm_emotions,
    "charm_person": get_charm_person,
    "clairvoyance": get_clairvoyance,
    "cloud_of_daggers": get_cloud_of_daggers,
    "comprehend_languages": get_comprehend_languages,
    "compulsion": get_compulsion,
    "confusion": get_confusion,
    "crown_of_madness": get_crown_of_madness,
    "cure_wounds": get_cure_wounds,
    "dancing_lights": get_dancing_lights,
    "detect_magic": get_detect_magic,
    "detect_thoughts": get_detect_thoughts,
    "dimension_door": get_dimension_door,
    "disguise_self": get_disguise_self,
    "dispel_magic": get_dispel_magic,
    "dissonant_whispers": get_dissonant_whispers,
    "dominate_monster": get_dominate_monster,
    "dominate_person": get_dominate_person,
    "dream": get_dream,
    "enhance_ability": get_enhance_ability,
    "enthrall": get_enthrall,
    "etherealness": get_etherealness,
    "eyebite": get_eyebite,
    "faerie_fire": get_faerie_fire,
    "fear": get_fear,
    "feather_fall": get_feather_fall,
    "feeblemind": get_feeblemind,
    "feign_death": get_feign_death,
    "find_the_path": get_find_the_path,
    "forcecage": get_forcecage,
    "foresight": get_foresight,
    "freedom_of_movement": get_freedom_of_movement,
    "friends": get_friends,
    "geas": get_geas,
    "glibness": get_glibness,
    "glyph_of_warding": get_glyph_of_warding,
    "greater_invisibility": get_greater_invisibility,
    "greater_restoration": get_greater_restoration,
    "guards_and_wards": get_guards_and_wards,
    "hallucinatory_terrain": get_hallucinatory_terrain,
    "healing_word": get_healing_word,
    "heat_metal": get_heat_metal,
    "heroism": get_heroism,
    "hold_monster": get_hold_monster,
    "hold_person": get_hold_person,
    "hypnotic_pattern": get_hypnotic_pattern,
    "identify": get_identify,
    "illusory_script": get_illusory_script,
    "invisibility": get_invisibility,
    "knock": get_knock,
    "legend_lore": get_legend_lore,
    "leomunds_tiny_hut": get_leomunds_tiny_hut,
    "lesser_restoration": get_lesser_restoration,
    "light": get_light,
    "locate_animals_or_plants": get_locate_animals_or_plants,
    "locate_creature": get_locate_creature,
    "locate_object": get_locate_object,
    "longstrider": get_longstrider,
    "mage_hand": get_mage_hand,
    "magic_mouth": get_magic_mouth,
    "major_image": get_major_image,
    "mass_cure_wounds": get_mass_cure_wounds,
    "mass_suggestion": get_mass_suggestion,
    "mending": get_mending,
    "message": get_message,
    "mind_blank": get_mind_blank,
    "minor_illusion": get_minor_illusion,
    "mirage_arcane": get_mirage_arcane,
    "mislead": get_mislead,
    "modify_memory": get_modify_memory,
    "mordenkainens_magnificent_mansion": get_mordenkainens_magnificent_mansion,
    "mordenkainens_sword": get_mordenkainens_sword,
    "nondetection": get_nondetection,
    "ottos_irresistible_dance": get_ottos_irresistible_dance,
    "phantasmal_force": get_phantasmal_force,
    "planar_binding": get_planar_binding,
    "plant_growth": get_plant_growth,
    "polymorph": get_polymorph,
    "power_word_heal": get_power_word_heal,
    "power_word_kill": get_power_word_kill,
    "power_word_stun": get_power_word_stun,
    "prestidigitation": get_prestidigitation,
    "programmed_illusion": get_programmed_illusion,
    "project_image": get_project_image,
    "raise_dead": get_raise_dead,
    "regenerate": get_regenerate,
    "resurrection": get_resurrection,
    "scrying": get_scrying,
    "see_invisibility": get_see_invisibility,
    "seeming": get_seeming,
    "sending": get_sending,
    "shatter": get_shatter,
    "silence": get_silence,
    "silent_image": get_silent_image,
    "sleep": get_sleep,
    "speak_with_animals": get_speak_with_animals,
    "speak_with_dead": get_speak_with_dead,
    "speak_with_plants": get_speak_with_plants,
    "stinking_cloud": get_stinking_cloud,
    "suggestion": get_suggestion,
    "symbol": get_symbol,
    "teleport": get_teleport,
    "teleportation_circle": get_teleportation_circle,
    "thunderwave": get_thunderwave,
    "tongues": get_tongues,
    "true_polymorph": get_true_polymorph,
    "true_seeing": get_true_seeing,
    "true_strike": get_true_strike,
    "unseen_servant": get_unseen_servant,
    "vicious_mockery": get_vicious_mockery,
    "zone_of_truth": get_zone_of_truth
}