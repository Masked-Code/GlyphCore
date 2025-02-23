from utils import (
    DnDSpell, SpellLevel, SchoolOfMagic, SpellcastingClass, Component,
    CastingTimeType, RangeType, DurationType, AreaOfEffectType, DamageType,
    SavingThrowType, AbilityScore
)

def get_acid_splash():
    return DnDSpell(
        name="Acid Splash",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.ACID,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_alter_self():
    return DnDSpell(
        name="Alter Self",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.BLUDGEONING,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_blink():
    return DnDSpell(
        name="Blink",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
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

def get_blur():
    return DnDSpell(
        name="Blur",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL],
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

def get_burning_hands():
    return DnDSpell(
        name="Burning Hands",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=15,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_chain_lightning():
    return DnDSpell(
        name="Chain Lightning",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of fur, a piece of amber, glass, or crystal rod, and three silver pins",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=150,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.LIGHTNING,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_chill_touch():
    return DnDSpell(
        name="Chill Touch",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.FIXED,
        duration_time="1 round",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.NECROTIC,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_chromatic_orb():
    return DnDSpell(
        name="Chromatic Orb",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a diamond worth at least 50gp",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=90,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.ACID,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_circle_of_death():
    return DnDSpell(
        name="Circle of Death",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="the powder of a crushed black pearl worth at least 500gp",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=150,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.NECROTIC,
        damage_dice="2d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_cloudkill():
    return DnDSpell(
        name="Cloudkill",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_color_spray():
    return DnDSpell(
        name="Color Spray",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of powder or sand that is colored red, yellow, and blue",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=15,
        duration_type=DurationType.FIXED,
        duration_time="1 round",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
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

def get_cone_of_cold():
    return DnDSpell(
        name="Cone of Cold",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small crystal or glass cone",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.COLD,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
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

def get_counterspell():
    return DnDSpell(
        name="Counterspell",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.SOMATIC],
        casting_time=CastingTimeType.REACTION,
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

def get_creation():
    return DnDSpell(
        name="Creation",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a tiny piece of matter of the same type of the item you plan to create",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="Special",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_darkness():
    return DnDSpell(
        name="Darkness",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.MATERIAL],
        material_component_desc="bat fur and a drop of pitch or piece of coal",
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

def get_darkvision():
    return DnDSpell(
        name="Darkvision",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.RANGER, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="either a pinch of dried carrot or an agate",
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

def get_delayed_blast_fireball():
    return DnDSpell(
        name="Delayed Blast Fireball",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a tiny ball of bat guano and sulfur",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=150,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
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

def get_disintegrate():
    return DnDSpell(
        name="Disintegrate",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a lodestone and a pinch of dust",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
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

def get_dominate_beast():
    return DnDSpell(
        name="Dominate Beast",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER],
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
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_enlarge_reduce():
    return DnDSpell(
        name="Enlarge/Reduce",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of powdered iron",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d4",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
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

def get_expeditious_retreat():
    return DnDSpell(
        name="Expeditious Retreat",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.BONUS_ACTION,
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

def get_false_life():
    return DnDSpell(
        name="False Life",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small amount of alcohol or distilled spirits",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d4",
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_finger_of_death():
    return DnDSpell(
        name="Finger of Death",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
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
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_fire_bolt():
    return DnDSpell(
        name="Fire Bolt",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        damage_dice="1d10",
        effect_role="Damage",
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

def get_fireball():
    return DnDSpell(
        name="Fireball",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a tiny ball of bat guano and sulfur",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=150,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_fly():
    return DnDSpell(
        name="Fly",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a wing feather from any bird",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
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

def get_fog_cloud():
    return DnDSpell(
        name="Fog Cloud",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.RANGER, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_gaseous_form():
    return DnDSpell(
        name="Gaseous Form",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of gauze and a wisp of smoke",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
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

def get_globe_of_invulnerability():
    return DnDSpell(
        name="Globe of Invulnerability",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a glass or crystal bead that shatters when the spell ends",
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

def get_gust_of_wind():
    return DnDSpell(
        name="Gust of Wind",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.DRUID],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a legume seed",
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
        saving_throw=SavingThrowType.STRENGTH,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_haste():
    return DnDSpell(
        name="Haste",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a shaving of licorice root",
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

def get_ice_storm():
    return DnDSpell(
        name="Ice Storm",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of dust and a few drops of water",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=300,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.COLD,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_incendiary_cloud():
    return DnDSpell(
        name="Incendiary Cloud",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=150,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_jump():
    return DnDSpell(
        name="Jump",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.RANGER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a grasshopper's hind leg",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_levitate():
    return DnDSpell(
        name="Levitate",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="either a small leather loop or a piece of golden wire bent into a cup shape with a long shank on one end",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
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

def get_lightning_bolt():
    return DnDSpell(
        name="Lightning Bolt",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of fur and a rod of amber, crystal, or glass",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=100,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.LIGHTNING,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_mage_armor():
    return DnDSpell(
        name="Mage Armor",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a piece of cured leather",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
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

def get_magic_missile():
    return DnDSpell(
        name="Magic Missile",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        damage_dice="1d4",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_meteor_swarm():
    return DnDSpell(
        name="Meteor Swarm",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=1,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_mirror_image():
    return DnDSpell(
        name="Mirror Image",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.SELF,
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

def get_misty_step():
    return DnDSpell(
        name="Misty Step",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.BONUS_ACTION,
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

def get_move_earth():
    return DnDSpell(
        name="Move Earth",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="an iron blade and a small bag containing a mixture of soils - clay, loam, and sand",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="2 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_poison_spray():
    return DnDSpell(
        name="Poison Spray",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=10,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d12",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_prismatic_spray():
    return DnDSpell(
        name="Prismatic Spray",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.ACID,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_ray_of_sickness():
    return DnDSpell(
        name="Ray of Sickness",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
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
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_reverse_gravity():
    return DnDSpell(
        name="Reverse Gravity",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a lodestone and iron filing",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=100,
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

def get_scorching_ray():
    return DnDSpell(
        name="Scorching Ray",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        damage_dice="2d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_shield():
    return DnDSpell(
        name="Shield",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.REACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.FIXED,
        duration_time="1 round",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_shocking_grasp():
    return DnDSpell(
        name="Shocking Grasp",
        level=SpellLevel.CANTRIP,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.LIGHTNING,
        damage_dice="1d8",
        effect_role="Damage",
        is_ritual=False,
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

def get_sleet_storm():
    return DnDSpell(
        name="Sleet Storm",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of dust and a few drops of water",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=150,
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

def get_slow():
    return DnDSpell(
        name="Slow",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a drop of molasses",
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
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_spider_climb():
    return DnDSpell(
        name="Spider Climb",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a drop of bituem and a spider",
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

def get_sunburst():
    return DnDSpell(
        name="Sunburst",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="fire and a piece of sunstone",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=150,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="2d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_telekinesis():
    return DnDSpell(
        name="Telekinesis",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
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

def get_time_stop():
    return DnDSpell(
        name="Time Stop",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.SELF,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d4",
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_wall_of_stone():
    return DnDSpell(
        name="Wall of Stone",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small block of granite",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_water_breathing():
    return DnDSpell(
        name="Water Breathing",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.RANGER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a short reed or piece of straw",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
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

def get_web():
    return DnDSpell(
        name="Web",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of spider web",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
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

def get_wish():
    return DnDSpell(
        name="Wish",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
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

def get_witch_bolt():
    return DnDSpell(
        name="Witch Bolt",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.SORCERER, SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a twig from a tree that has been struck by lightning",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.LIGHTNING,
        damage_dice="1d12",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

KNOWN_SORCERER_SPELLS = {
    "acid_splash": get_acid_splash,
    "alter_self": get_alter_self,
    "animate_objects": get_animate_objects,
    "banishment": get_banishment,
    "blade_ward": get_blade_ward,
    "blight": get_blight,
    "blindness_deafness": get_blindness_deafness,
    "blink": get_blink,
    "blur": get_blur,
    "burning_hands": get_burning_hands,
    "chain_lightning": get_chain_lightning,
    "charm_person": get_charm_person,
    "chill_touch": get_chill_touch,
    "chromatic_orb": get_chromatic_orb,
    "circle_of_death": get_circle_of_death,
    "clairvoyance": get_clairvoyance,
    "cloud_of_daggers": get_cloud_of_daggers,
    "cloudkill": get_cloudkill,
    "color_spray": get_color_spray,
    "comprehend_languages": get_comprehend_languages,
    "cone_of_cold": get_cone_of_cold,
    "confusion": get_confusion,
    "counterspell": get_counterspell,
    "creation": get_creation,
    "crown_of_madness": get_crown_of_madness,
    "dancing_lights": get_dancing_lights,
    "darkness": get_darkness,
    "darkvision": get_darkvision,
    "daylight": get_daylight,
    "delayed_blast_fireball": get_delayed_blast_fireball,
    "detect_magic": get_detect_magic,
    "detect_thoughts": get_detect_thoughts,
    "disguise_self": get_disguise_self,
    "disintegrate": get_disintegrate,
    "dispel_magic": get_dispel_magic,
    "dominate_beast": get_dominate_beast,
    "dominate_monster": get_dominate_monster,
    "dominate_person": get_dominate_person,
    "dream": get_dream,
    "earthquake": get_earthquake,
    "enhance_ability": get_enhance_ability,
    "enlarge_reduce": get_enlarge_reduce,
    "etherealness": get_etherealness,
    "expeditious_retreat": get_expeditious_retreat,
    "eyebite": get_eyebite,
    "false_life": get_false_life,
    "fear": get_fear,
    "feather_fall": get_feather_fall,
    "feeblemind": get_feeblemind,
    "finger_of_death": get_finger_of_death,
    "fire_bolt": get_fire_bolt,
    "fire_storm": get_fire_storm,
    "fireball": get_fireball,
    "fly": get_fly,
    "fog_cloud": get_fog_cloud,
    "friends": get_friends,
    "gaseous_form": get_gaseous_form,
    "gate": get_gate,
    "globe_of_invulnerability": get_globe_of_invulnerability,
    "greater_invisibility": get_greater_invisibility,
    "gust_of_wind": get_gust_of_wind,
    "haste": get_haste,
    "hold_monster": get_hold_monster,
    "hold_person": get_hold_person,
    "hypnotic_pattern": get_hypnotic_pattern,
    "ice_storm": get_ice_storm,
    "incendiary_cloud": get_incendiary_cloud,
    "insect_plague": get_insect_plague,
    "invisibility": get_invisibility,
    "jump": get_jump,
    "knock": get_knock,
    "levitate": get_levitate,
    "light": get_light,
    "lightning_bolt": get_lightning_bolt,
    "mage_armor": get_mage_armor,
    "mage_hand": get_mage_hand,
    "magic_missile": get_magic_missile,
    "major_image": get_major_image,
    "mass_suggestion": get_mass_suggestion,
    "mending": get_mending,
    "message": get_message,
    "meteor_swarm": get_meteor_swarm,
    "minor_illusion": get_minor_illusion,
    "mirror_image": get_mirror_image,
    "misty_step": get_misty_step,
    "move_earth": get_move_earth,
    "phantasmal_force": get_phantasmal_force,
    "plane_shift": get_plane_shift,
    "poison_spray": get_poison_spray,
    "polymorph": get_polymorph,
    "power_word_kill": get_power_word_kill,
    "power_word_stun": get_power_word_stun,
    "prestidigitation": get_prestidigitation,
    "prismatic_spray": get_prismatic_spray,
    "protection_from_energy": get_protection_from_energy,
    "ray_of_sickness": get_ray_of_sickness,
    "reverse_gravity": get_reverse_gravity,
    "scorching_ray": get_scorching_ray,
    "see_invisibility": get_see_invisibility,
    "seeming": get_seeming,
    "shatter": get_shatter,
    "shield": get_shield,
    "shocking_grasp": get_shocking_grasp,
    "silent_image": get_silent_image,
    "sleep": get_sleep,
    "sleet_storm": get_sleet_storm,
    "slow": get_slow,
    "spider_climb": get_spider_climb,
    "stinking_cloud": get_stinking_cloud,
    "stoneskin": get_stoneskin,
    "suggestion": get_suggestion,
    "sunburst": get_sunburst,
    "telekinesis": get_telekinesis,
    "teleport": get_teleport,
    "teleportation_circle": get_teleportation_circle,
    "thunderwave": get_thunderwave,
    "time_stop": get_time_stop,
    "tongues": get_tongues,
    "true_seeing": get_true_seeing,
    "true_strike": get_true_strike,
    "wall_of_fire": get_wall_of_fire,
    "wall_of_stone": get_wall_of_stone,
    "water_breathing": get_water_breathing,
    "water_walk": get_water_walk,
    "web": get_web,
    "wish": get_wish,
    "witch_bolt": get_witch_bolt
}