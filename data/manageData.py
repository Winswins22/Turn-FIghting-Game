from random import shuffle
import json

def getColors():

  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()

  data = json.loads(data)

  #print (data["colors"])
  return data["colors"]

"""def changeColors(skillInfo):
  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()

  data = json.loads(data)
  colorInfo = data["colors"]

  colorInfo["red"] = max(0, colorInfo["red"] + skillInfo["red"])
  colorInfo["green"] = max(0, colorInfo["green"] + skillInfo["green"])
  colorInfo["blue"] = max(0, colorInfo["blue"] + skillInfo["blue"])
  colorInfo["purple"] = max(0, colorInfo["purple"] + skillInfo["purple"])

  data["colors"] = colorInfo

  with open('data/data.txt'', 'w') as _data:
    _data.write(json.dumps(data))"""


def changeColors(redChange, greenChange, blueChange, purpleChange):
  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()

  data = json.loads(data)
  colorInfo = data["colors"]

  colorInfo["red"] = max(0, colorInfo["red"] + redChange)
  colorInfo["green"] = max(0, colorInfo["green"] + greenChange)
  colorInfo["blue"] = max(0, colorInfo["blue"] + blueChange)
  colorInfo["purple"] = max(0, colorInfo["purple"] + purpleChange)

  data["colors"] = colorInfo

  with open('data/data.txt', 'w') as _data:
    _data.write(json.dumps(data))

def getUserHp():
  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()
  
  data = json.loads(data)

  return data["health"]["player"]

def getEnemyHp():
  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()
  
  data = json.loads(data)

  return data["health"]["enemy"]

def reduceUserHp(damage):
  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()
  
  data = json.loads(data)

  data["health"]["player"] = max(0, data["health"]["player"] - damage)

  with open('data/data.txt', 'w') as _data:
    _data.write(json.dumps(data))


def reduceEnemyHp(damage):
  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()
  
  data = json.loads(data)
  data["health"]["enemy"] = max(0, data["health"]["enemy"] - damage)

  with open('data/data.txt', 'w') as _data:
    _data.write(json.dumps(data))


def getStats():
  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()
  
  data = json.loads(data)

  return data["gameplayStats"]

def increaseTurn():
  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()
  
  data = json.loads(data)

  data["gameplayStats"]["turns"] += 1

  with open('data/data.txt', 'w') as _data:
    _data.write(json.dumps(data))

def resetData():
  baseData = {
    "gameplayStats" : {"turns": 0, "battles": 0},
    "health" : {"player": 200, "enemy": 100},
    "colors": {"red": 175, "green": 175, "blue": 175, "purple": 175},

    "skillsAreInHand": {
        "Heartbeat Red": False,
        "Flame Slash": False,
        "Flame Prison": True,
        "Heartbeat Green": False,
        "Bright Slash": False,
        "Nature's Will": False,
        "Heartbeat Blue": False,
        "Water Slash": True,
        "Hydroblaster": False,
        "Heartbeat Purple": False,
        "Dark Slash": False,
        "Shadozer": True,

        "Reliable Defense": True,
        "Nature's Blessing": True,
        "Water Shield": False,
        "Dark Devotion": False
    }
  }

  with open('data/data.txt', 'w') as _data:
    _data.write(json.dumps(baseData))
  
  print ("new data!")

# in json it was not possible to have a 2D item as a value beacuse it would not get hashed(error). To get around this, this was declared here instead of inside data.txt
allUserSkills = {

  "attackSkills": [
    {
      "name": "Heartbeat Red",
      "damage": 1,
      "red": 200,
      "green": -50,
      "blue": -50,
      "purple": -100,
    },

    {
      "name": "Flame Slash",
      "damage": 10,
      "red": -20,
      "green": 10,
      "blue": 10,
      "purple": 0,
    },

    {
      "name": "Flame Prison",
      "damage": 35,
      "red": -300,
      "green": 180,
      "blue": 100,
      "purple": 20,
    },

    {
      "name": "Heartbeat Green",
      "damage": 1,
      "red": -100,
      "green": 200,
      "blue": -50,
      "purple": -50,
    },

    {
      "name": "Bright Slash",
      "damage": 10,
      "red": 0,
      "green": -20,
      "blue": 10,
      "purple": 10,
    },

    {
      "name": "Nature's Will",
      "damage": 20,
      "red": 75,
      "green": -75,
      "blue": -75,
      "purple": 75,
    },

    {
      "name": "Heartbeat Blue",
      "damage": 1,
      "red": -50,
      "green": -100,
      "blue": 200,
      "purple": -50,
    },

    {
      "name": "Water Slash",
      "damage": 10,
      "red": 10,
      "green": 0,
      "blue": -20,
      "purple": 10,
    },

    {
      "name": "Hydroblaster",
      "damage": 25,
      "red": 70,
      "green": 30,
      "blue": -200,
      "purple": 100,
    },

    {
      "name": "Heartbeat Purple",
      "damage": 1,
      "red": -50,
      "green": -50,
      "blue": -100,
      "purple": 200,
    },

    {
      "name": "Dark Slash",
      "damage": 10,
      "red": 10,
      "green": 10,
      "blue": 0,
      "purple": -20,
    },

    {
      "name": "Shadozer",
      "damage": 30,
      "red": 140,
      "green": 40,
      "blue": 20,
      "purple": -200,
    },

  ],

  "defenseSkills": [
    {
      "name": "Reliable Defense",
      "defense": 4,
      "red": 0,
      "green": 0,
      "blue": 0,
      "purple": 0,
    },

    {
      "name": "Nature's Blessing",
      "defense": 50,
      "red": 10,
      "green": -150,
      "blue": 100,
      "purple": 40,
    },

    {
      "name": "Water Shield",
      "defense": 8,
      "red": 20,
      "green": 10,
      "blue": -60,
      "purple": 30,
    },

    {
      "name": "Dark Devotion",
      "defense": 5,
      "red": 35,
      "green": 15,
      "blue": 5,
      "purple": -55,
    },
  ]

}

def getSkillTypeFromName(skillName):
  attackSkills = allUserSkills["attackSkills"]
  defenseSkills = allUserSkills["defenseSkills"]

  for i in attackSkills:
    if i["name"] == skillName:
      return "attack"
  
  for i in defenseSkills:
    if i["name"] == skillName:
      return "defense"
  
  print ("Skill not found?!?!?")
  return;

def getSkillInfoFromName(skillName):
  attackSkills = allUserSkills["attackSkills"]
  defenseSkills = allUserSkills["defenseSkills"]

  for i in attackSkills:
    if i["name"] == skillName:
      return i
  
  for i in defenseSkills:
    if i["name"] == skillName:
      return i
  
  print ("Skill not found?!?!?")
  return;

# returns a list of strings (aka names of skills only)
def getSkillsInHand():
  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()

  data = json.loads(data)

  skillsInHand = []

  for i in data["skillsAreInHand"].items():
    if (i[1] == True):
      skillsInHand.append(i[0])

  return skillsInHand

# returns a list of strings (aka names of skills only)
def getSkillsNotInHand():
  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()

  data = json.loads(data)

  skillsNotInHand = []

  for i in data["skillsAreInHand"].items():
    if (i[1] == False):
      skillsNotInHand.append(i[0])

  return skillsNotInHand

# skillInfo : a dict with skill info (see manageData.py)
def canCastSkill(skillInfo):
  colorInfo = getColors()

  if ((colorInfo["red"] + skillInfo["red"]) < 0):
    return False
  
  elif ((colorInfo["green"] + skillInfo["green"]) < 0):
    return False

  elif ((colorInfo["blue"] + skillInfo["blue"]) < 0):
    return False

  elif ((colorInfo["purple"] + skillInfo["purple"] )< 0):
    return False

  return True

def removeSkillFromHand(skillNameToGetOutOfHand):
  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()

  data = json.loads(data)

  data["skillsAreInHand"][skillNameToGetOutOfHand] = False

  with open('data/data.txt', 'w') as _data:
    _data.write(json.dumps(data))

def putSkillInHand(skillNameToPutInHand):
  with open("data/data.txt", "r", encoding="utf-8") as _data:
    data = _data.read()

  data = json.loads(data)

  data["skillsAreInHand"][skillNameToPutInHand] = True

  with open('data/data.txt', 'w') as _data:
    _data.write(json.dumps(data))

# gets a new skill that is not in hand and is the same type
def getNewSkill(skillNameToGetOutOfHand):
  # get info
  skills = getSkillsNotInHand()
  shuffle(skills)
  oldSkillType = getSkillTypeFromName(skillNameToGetOutOfHand)

  for i in skills:
    if oldSkillType == getSkillTypeFromName(i):
      newSkill = i
      break
  
  removeSkillFromHand(skillNameToGetOutOfHand)
  putSkillInHand(newSkill)

  return getSkillInfoFromName(newSkill)