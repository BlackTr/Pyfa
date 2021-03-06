# moduleBonusFighterSupportUnit
#
# Used by:
# Modules from group: Fighter Support Unit (8 of 8)
type = "passive"
def handler(fit, src, context):
    fit.fighters.filteredItemBoost(lambda mod: mod.item.requiresSkill("Fighters"), "shieldCapacity", src.getModifiedItemAttr("fighterBonusShieldCapacityPercent"))
    fit.fighters.filteredItemBoost(lambda mod: mod.item.requiresSkill("Fighters"), "maxVelocity", src.getModifiedItemAttr("fighterBonusVelocityPercent"), stackingPenalties=True)
    fit.fighters.filteredItemBoost(lambda mod: mod.item.requiresSkill("Fighters"), "fighterAbilityAttackMissileDuration", src.getModifiedItemAttr("fighterBonusROFPercent"), stackingPenalties=True)
    fit.fighters.filteredItemBoost(lambda mod: mod.item.requiresSkill("Fighters"), "fighterAbilityAttackTurretDuration", src.getModifiedItemAttr("fighterBonusROFPercent"), stackingPenalties=True)
    fit.fighters.filteredItemBoost(lambda mod: mod.item.requiresSkill("Fighters"), "fighterAbilityMissilesDuration", src.getModifiedItemAttr("fighterBonusROFPercent"), stackingPenalties=True)
    fit.fighters.filteredItemBoost(lambda mod: mod.item.requiresSkill("Fighters"), "shieldRechargeRate", src.getModifiedItemAttr("fighterBonusShieldRechargePercent"))
