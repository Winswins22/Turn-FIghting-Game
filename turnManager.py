import pygame
from data.manageData import reduceEnemyHp, reduceUserHp, getSkillTypeFromName, changeColors, canCastSkill, increaseTurn

def onPlayerAttack(skillInfo):
  reduceEnemyHp(skillInfo["damage"])

def onEnemyAttack(skillInfo, playerDefenseValue = 0):
  
  if canCastSkill(skillInfo):
    changeColors(skillInfo["red"], skillInfo["green"], skillInfo["blue"], skillInfo["purple"])
    reduceUserHp(max(0, skillInfo["damage"]-playerDefenseValue))

def doTurn(playerSkillInfo, enemySkillInfo):

  # aka enemy is dead
  if enemySkillInfo == None:
    return

  # player does a shuffle
  elif playerSkillInfo == None:
    increaseTurn()
    onEnemyAttack(enemySkillInfo)

  # player attacks
  elif getSkillTypeFromName(playerSkillInfo["name"]) == "attack":
    increaseTurn()
    onPlayerAttack(playerSkillInfo)
    onEnemyAttack(enemySkillInfo)
  
  # player defends
  elif getSkillTypeFromName(playerSkillInfo["name"]) == "defense":
    increaseTurn()
    onEnemyAttack(enemySkillInfo, playerSkillInfo["defense"])
