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

def get_alarm():
    return DnDSpell(
        name="Alarm",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.RANGER, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a tiny bell and a piece of fine silver wire",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_antipathy_sympathy():
    return DnDSpell(
        name="Antipathy/Sympathy",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.ENCHANTMENT,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="either a lump of alum soaked in vinegar for the antipathy effect or a drop of honey for the sympathy effect",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 hour",
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="10 days",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_arcane_eye():
    return DnDSpell(
        name="Arcane Eye",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of bat fur",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
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

def get_arcane_lock():
    return DnDSpell(
        name="Arcane Lock",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="gold dust worth at least 25 gp, which the spell consumes",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="Until dispelled",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_bigbys_hand():
    return DnDSpell(
        name="Bigby's Hand",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="an eggshell and a snakeskin glove",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        damage_dice="2d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_clone():
    return DnDSpell(
        name="Clone",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a diamond worth at least 1,000 gp and at least 1 cubic inch of flesh of the creature that is to be cloned, which the spell consumes, and a vessel worth at least 2,000 gp that has a sealable lid and is large enough to hold a Medium creature, such as a huge urn, coffin, mud-filled cyst in the ground, or crystal container filled with salt water",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 hour",
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_conjure_elemental():
    return DnDSpell(
        name="Conjure Elemental",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="burning incense for air, soft clay for earth, sulfur and phosphorus for fire, or water and sand for water",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=90,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_conjure_minor_elementals():
    return DnDSpell(
        name="Conjure Minor Elementals",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=90,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1  hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_contact_other_plane():
    return DnDSpell(
        name="Contact Other Plane",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL],
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.SELF,
        duration_type=DurationType.FIXED,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=True,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.INTELLIGENCE,
        spellcasting_ability=AbilityScore.CHARISMA,
        source_book="Player's Handbook"
    )

def get_contingency():
    return DnDSpell(
        name="Contingency",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a statuette of yourself carved from ivory and decorated with gems worth at least 1,500 gp",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.SELF,
        duration_type=DurationType.FIXED,
        duration_time="10 days",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_control_water():
    return DnDSpell(
        name="Control Water",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a drop of water and a pinch of dust",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=300,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.BLUDGEONING,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.STRENGTH,
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

def get_demiplane():
    return DnDSpell(
        name="Demiplane",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.SOMATIC],
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

def get_drawmijs_instant_summon():
    return DnDSpell(
        name="Drawmij's Instant Summon",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a sapphire worth 1,000 gp",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.TOUCH,
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

def get_evards_black_tentacles():
    return DnDSpell(
        name="Evard's Black Tentacles",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a piece of tentacle from a giant octopus or a giant squid",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=90,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.BLUDGEONING,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_fabricate():
    return DnDSpell(
        name="Fabricate",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_find_familiar():
    return DnDSpell(
        name="Find Familiar",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="10 gp worth of charcoal, incense, and herbs that must be consumed by fire in a brass brazier",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 hour",
        range_type=RangeType.FIXED,
        range_distance=10,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Healing",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_fire_shield():
    return DnDSpell(
        name="Fire Shield",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of phosphorous or a firefly",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.FIXED,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_flaming_sphere():
    return DnDSpell(
        name="Flaming Sphere",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of tallow, a pinch of brimstone, and a dustin of pwdered iron",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
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
        spellcasting_ability=AbilityScore.WISDOM,
        source_book="Player's Handbook"
    )

def get_flesh_to_stone():
    return DnDSpell(
        name="Flesh to Stone",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of lime, water, and earth",
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
        saving_throw=SavingThrowType.CONSTITUTION,
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

def get_grease():
    return DnDSpell(
        name="Grease",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a bit of pork rind or butter",
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
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_imprisonment():
    return DnDSpell(
        name="Imprisonment",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a vellum depiction or a carved statuette in the likeness of the target, and a special component that varies according to the version of the spell you choose, worth at least 500 gp per Hit Die of the target",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="Until dispelled",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Healing",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_leomunds_secret_chest():
    return DnDSpell(
        name="Leomund's Secret Chest",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="an exquisite chest, 3 feet by 2 feet by 2 feet, constructed from rare materials worth at least 5,000 gp, and a Tiny replica made from the same materials worth at least 50 gp",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_magic_jar():
    return DnDSpell(
        name="Magic Jar",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a gem, crystal, reliquary, or some other ornamental container worth at least 500 gp",
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.SELF,
        duration_type=DurationType.FIXED,
        duration_time="Until dispelled",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Control",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CHARISMA,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_maze():
    return DnDSpell(
        name="Maze",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.WIZARD],
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
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_melfs_acid_arrow():
    return DnDSpell(
        name="Melf's Acid Arrow",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="powdered rhubarb leaf and an adder's stomach",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=90,
        duration_type=DurationType.FIXED,
        duration_time="powdered rhubarb leaf and an adder's stomach",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.ACID,
        damage_dice="1d4",
        effect_role="Damage",
        is_ritual=False,
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

def get_mordenkainens_faithful_hound():
    return DnDSpell(
        name="Mordenkainen's Faithful Hound",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a tiny silver whistle, a piece of bone, and a thread",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="8 hours",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.PIERCING,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_mordenkainens_private_sanctum():
    return DnDSpell(
        name="Mordenkainen's Private Sanctum",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a thin sheet of lead, a piece of opaque glass, a wad of cotton or cloth, and powdered chrysolite",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="10 minutes",
        range_type=RangeType.FIXED,
        range_distance=120,
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

def get_nystuls_magic_aura():
    return DnDSpell(
        name="Nystul's Magic Aura",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small square of silk",
        casting_time=CastingTimeType.ACTION,
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

def get_otilukes_freezing_sphere():
    return DnDSpell(
        name="Otiluke's Freezing Sphere",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small crystal spher",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=300,
        duration_type=DurationType.INSTANTANEOUS,
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.COLD,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_otilukes_resilient_sphere():
    return DnDSpell(
        name="Otiluke's Resilient Sphere",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a hemispherical piece of clear crystal and a matching hemispherical piece of gum arabic",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_passwall():
    return DnDSpell(
        name="Passwall",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of sesame seeds",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
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

def get_phantasmal_killer():
    return DnDSpell(
        name="Phantasmal Killer",
        level=SpellLevel.LEVEL_4,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 minute",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_dice="1d10",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.WISDOM,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_phantom_steed():
    return DnDSpell(
        name="Phantom Steed",
        level=SpellLevel.LEVEL_3,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.MINUTE,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_prismatic_wall():
    return DnDSpell(
        name="Prismatic Wall",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.ABJURATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=60,
        duration_type=DurationType.FIXED,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.ACID,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_rarys_telepathic_bond():
    return DnDSpell(
        name="Rary's Telepathic Bond",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.DIVINATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="pieces of eggshell from two different kinds of creatures",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_ray_of_enfeeblement():
    return DnDSpell(
        name="Ray of Enfeeblement",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.NECROMANCY,
        casting_classes=[SpellcastingClass.WARLOCK, SpellcastingClass.WIZARD],
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
        saving_throw=SavingThrowType.CONSTITUTION,
        spellcasting_ability=AbilityScore.CHARISMA,
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

def get_rope_trick():
    return DnDSpell(
        name="Rope Trick",
        level=SpellLevel.LEVEL_2,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="powdered corn extract and a twisted loop of parchment",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_sequester():
    return DnDSpell(
        name="Sequester",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a powder composed of diamond, emerald, ruby, and sapphire dust worth at least 5,000 gp, which the spell consumes",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="Until dispelled",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_shapechange():
    return DnDSpell(
        name="Shapechange",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.TRANSMUTATION,
        casting_classes=[SpellcastingClass.DRUID, SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a jade circlet worth at least 1,500 gp, which you must place on your head before you cast the spell",
        casting_time=CastingTimeType.ACTION,
        range_type=RangeType.SELF,
        duration_type=DurationType.CONCENTRATION,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.WISDOM,
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

def get_simulacrum():
    return DnDSpell(
        name="Simulacrum",
        level=SpellLevel.LEVEL_7,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="snow or ice in quantities sufficient to made a life-size copy of the duplicated creature some hair, fingernail clippings, or other piece of that creature's body placed inside the snow or ice and powdered ruby worth 1,500 gp, sprinkled over the duplicate and consumed by the spell",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="12 hours",
        range_type=RangeType.TOUCH,
        duration_type=DurationType.FIXED,
        duration_time="Until dispelled",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_telepathy():
    return DnDSpell(
        name="Telepathy",
        level=SpellLevel.LEVEL_8,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pair of linked silver rings",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=120,
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

def get_tensers_floating_disk():
    return DnDSpell(
        name="Tenser's Floating Disk",
        level=SpellLevel.LEVEL_1,
        school=SchoolOfMagic.CONJURATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a drop of mercury",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=30,
        duration_type=DurationType.FIXED,
        duration_time="1 hour",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Utility",
        is_ritual=True,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_wall_of_force():
    return DnDSpell(
        name="Wall of Force",
        level=SpellLevel.LEVEL_5,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a pinch of powder made by crushing a clear gemstone",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FORCE,
        effect_role="Utility",
        is_ritual=False,
        requires_attack_roll=False,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
        source_book="Player's Handbook"
    )

def get_wall_of_ice():
    return DnDSpell(
        name="Wall of Ice",
        level=SpellLevel.LEVEL_6,
        school=SchoolOfMagic.EVOCATION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC, Component.MATERIAL],
        material_component_desc="a small piece of quartz",
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
        range_type=RangeType.FIXED,
        range_distance=120,
        duration_type=DurationType.CONCENTRATION,
        duration_time="10 minutes",
        targets=None,
        aoe_type=AreaOfEffectType.NONE,
        damage_type=DamageType.FIRE,
        damage_dice="1d6",
        effect_role="Damage",
        is_ritual=False,
        requires_attack_roll=False,
        saving_throw=SavingThrowType.DEXTERITY,
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

def get_weird():
    return DnDSpell(
        name="Weird",
        level=SpellLevel.LEVEL_9,
        school=SchoolOfMagic.ILLUSION,
        casting_classes=[SpellcastingClass.WIZARD],
        components=[Component.VERBAL, Component.SOMATIC],
        casting_time=CastingTimeType.CUSTOM,
        custom_casting_time="1 action",
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
        spellcasting_ability=AbilityScore.INTELLIGENCE,
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

