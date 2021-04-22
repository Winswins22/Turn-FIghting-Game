import pygame


from ui_elements.components import drawBoxBorders
from data.manageData import canCastSkill, getSkillInfoFromName, getSkillsInHand, changeColors, getNewSkill, getSkillTypeFromName, getEnemyHp

from pygame.color import THECOLORS
from random import shuffle

TEXT_COLOR = "white"
BORDER_COLOR = "black"
OUTER_BORDER_THICKNESS = 5
INNER_BORDER_THICKNESS = 3

COLOR_BOX_WIDTH = 10
COLOR_BOX_HEIGHT = 10

DEFENSE_SYMBOL = pygame.image.load("images/smallShield.png") 
ATTACK_SYMBOL = pygame.image.load("images/smallSword.png")

BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

DEFENSE_COLOR = "blue"
ATTACK_COLOR = "red"

HOVER_VALID_CAST_COLOR = "purple"
HOVER_INVALID_CAST_COLOR = "grey"

class skillButton():
  # skillInfo:
  # A dict inside allUserSkills (see manageData.py)
  def __init__(self, x, y, width, height, skillInfo):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.name = skillInfo["name"]

    self.redCost = skillInfo["red"]
    self.greenCost = skillInfo["green"]
    self.blueCost = skillInfo["blue"]
    self.purpleCost = skillInfo["purple"]

    self.skillInfo = skillInfo

    if "damage" in skillInfo.keys():
      self.bgColor = ATTACK_COLOR
      self.image = ATTACK_SYMBOL
      self.skillType = "attack"

      # the damage/defense of the skill
      self.numericImpact = skillInfo["damage"]

    elif "defense" in skillInfo.keys():
      self.bgColor = DEFENSE_COLOR
      self.image = DEFENSE_SYMBOL
      self.skillType = "defense"

      # the damage/defense of the skill
      self.numericImpact = skillInfo["defense"]
    
    else:
      print ("WARN: Failed to assign damage/defense to: ", skillInfo)

  def draw(self, font, smallerFont, screen):
    #Call this method to draw the button on the screen
    drawBoxBorders(screen, self.x,self.y,self.width,self.height, BORDER_COLOR)
        
    pygame.draw.rect(screen, THECOLORS[self.bgColor], (self.x,self.y,self.width,self.height))

    name = font.render(self.name, True, THECOLORS[TEXT_COLOR])
    redCost = smallerFont.render(str(self.redCost), True, THECOLORS[TEXT_COLOR])
    greenCost = smallerFont.render(str(self.greenCost), True, THECOLORS[TEXT_COLOR])
    blueCost = smallerFont.render(str(self.blueCost), True, THECOLORS[TEXT_COLOR])
    purpleCost = smallerFont.render(str(self.purpleCost), True, THECOLORS[TEXT_COLOR])
    numericImpact = font.render(str(self.numericImpact), True, THECOLORS[TEXT_COLOR])

    # Draw the name
    screen.blit(name, (self.x + (self.width/2 - name.get_width()/2), self.y+2))

    # Draw costs + color boxes
    drawBoxBorders(screen, self.x+5, self.y+20, COLOR_BOX_WIDTH, COLOR_BOX_HEIGHT, BORDER_COLOR, INNER_BORDER_THICKNESS)
        
    pygame.draw.rect(screen, THECOLORS["red"], (self.x+5,self.y+20,COLOR_BOX_WIDTH,COLOR_BOX_HEIGHT))

    screen.blit(redCost, (self.x+5+2+COLOR_BOX_WIDTH, self.y+20))

    drawBoxBorders(screen, self.x+40, self.y+20, COLOR_BOX_WIDTH, COLOR_BOX_HEIGHT, BORDER_COLOR, INNER_BORDER_THICKNESS)
        
    pygame.draw.rect(screen, THECOLORS["green"], (self.x+40,self.y+20,COLOR_BOX_WIDTH,COLOR_BOX_HEIGHT))

    screen.blit(greenCost, (self.x+40+2+COLOR_BOX_WIDTH, self.y+20))

    drawBoxBorders(screen, self.x+75, self.y+20, COLOR_BOX_WIDTH, COLOR_BOX_HEIGHT, BORDER_COLOR, INNER_BORDER_THICKNESS)
        
    pygame.draw.rect(screen, THECOLORS["blue"], (self.x+75,self.y+20,COLOR_BOX_WIDTH,COLOR_BOX_HEIGHT))

    screen.blit(blueCost, (self.x+75+2+COLOR_BOX_WIDTH, self.y+20))

    drawBoxBorders(screen, self.x+110, self.y+20, COLOR_BOX_WIDTH, COLOR_BOX_HEIGHT, BORDER_COLOR, INNER_BORDER_THICKNESS)
        
    pygame.draw.rect(screen, THECOLORS["purple"], (self.x+110,self.y+20,COLOR_BOX_WIDTH,COLOR_BOX_HEIGHT))

    screen.blit(purpleCost, (self.x+110+2+COLOR_BOX_WIDTH, self.y+20))

    # Draw numericImpact
    screen.blit(self.image, (self.x+5, self.y+38))
    screen.blit(numericImpact, (self.x+18, self.y+38))

  def onOver(self, pos):
    #Pos is the mouse position or a tuple of (x,y) coordinates
    if pos[0] > self.x and pos[0] < self.x + self.width:
        if pos[1] > self.y and pos[1] < self.y + self.height:

            #print(pos[0], self.x)
            
            if canCastSkill(self.skillInfo):
              self.bgColor = HOVER_VALID_CAST_COLOR
            else:
              self.bgColor = HOVER_INVALID_CAST_COLOR

            return;

    # reset color if not over
    if self.skillType == "attack":
      self.bgColor = ATTACK_COLOR
    else:
      self.bgColor = DEFENSE_COLOR

  def onClick(self, pos):
    if getEnemyHp() != 0:

      #Pos is the mouse position or a tuple of (x,y) coordinates
      if pos[0] > self.x and pos[0] < self.x + self.width:
          if pos[1] > self.y and pos[1] < self.y + self.height:
              #print("Change:", (self.redCost, self.greenCost, self.blueCost, self.purpleCost))
              if canCastSkill(self.skillInfo):
                changeColors(self.redCost, self.greenCost, self.blueCost, self.purpleCost)

                # return for popping
                return self.name

allEnemySkills = [
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
]


TEXT_COLOR = "white"
BORDER_COLOR = "black"
BORDER_THICKNESS = 5

NO_HP_COLOR = "red"
HP_COLOR = "green"
HP_BAR_X = 500
HP_BAR_Y = 140
HP_BAR_WIDTH = 100
HP_BAR_HEIGHT = 25

SKILL_X = 450
SKILL_Y = 180

SKILL_WIDTH = 150
SKILL_HEIGHT = 50

def drawEnemyHP(screen, font):
  heart = pygame.image.load("images/smallHeart.png")

  # get info
  userHealth = getEnemyHp()

  #borders
  drawBoxBorders(screen, HP_BAR_X, HP_BAR_Y, HP_BAR_WIDTH, HP_BAR_HEIGHT, BORDER_COLOR)

  # draw HP background
  pygame.draw.rect(screen, THECOLORS[HP_COLOR], (HP_BAR_X, HP_BAR_Y, userHealth, HP_BAR_HEIGHT))
  pygame.draw.rect(screen, THECOLORS[NO_HP_COLOR], (HP_BAR_X + userHealth, HP_BAR_Y, HP_BAR_WIDTH - userHealth, HP_BAR_HEIGHT))

  # draw HP bar + image
  screen.blit(heart, (HP_BAR_X, HP_BAR_Y))
  HPText = font.render(str(userHealth), True, THECOLORS[TEXT_COLOR])
  screen.blit(HPText, (HP_BAR_X + 50, HP_BAR_Y))


currentSkill = skillButton(SKILL_X, SKILL_Y, SKILL_WIDTH, SKILL_HEIGHT, allEnemySkills[0])

def assignNewSkill():

  shuffle(allEnemySkills)
  currentSkill = skillButton(SKILL_X, SKILL_Y, SKILL_WIDTH, SKILL_HEIGHT, allEnemySkills[0])

assignNewSkill()

def drawSkill(smallestFont, smallerestFont, screen):
  currentSkill.draw(smallestFont, smallerestFont, screen)

def getCurrentEnemySkill():

  if getEnemyHp() != 0:
    return currentSkill.skillInfo
  return

def drawEnemyUI(screen, smallerFont, smallestFont, smallerestFont):
  if getEnemyHp() == 0:
    return
  drawEnemyHP(screen, smallerFont)
  drawSkill(smallestFont, smallerestFont, screen)