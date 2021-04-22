import pygame

from turnManager import doTurn
from ui_elements.components import drawBoxBorders
from ui_elements.enemyUI import getCurrentEnemySkill, assignNewSkill
from data.manageData import canCastSkill, getSkillInfoFromName, getSkillsInHand, changeColors, getNewSkill, getSkillTypeFromName, getUserHp

from pygame.color import THECOLORS

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

ATTACK_BUTTON_COORDS = [
  (275, 275),
  (445, 275),
  (615, 275)
]

DEFENSE_BUTTON_COORDS = [
  (275, 340),
  (445, 340),
]

SHUFFLE_BUTTON_COORDS = (615, 340)
SHUFFLE_BUTTON_COLOR = "green"

allButtons = []
skillsHaveBeenDrawn = False

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
    # check if dead
    if getUserHp() != 0:
      #Pos is the mouse position or a tuple of (x,y) coordinates
      if pos[0] > self.x and pos[0] < self.x + self.width:
          if pos[1] > self.y and pos[1] < self.y + self.height:
              #print("Change:", (self.redCost, self.greenCost, self.blueCost, self.purpleCost))
              if canCastSkill(self.skillInfo):
                changeColors(self.redCost, self.greenCost, self.blueCost, self.purpleCost)

                # do a turn
                doTurn(self.skillInfo, getCurrentEnemySkill())
                assignNewSkill()

                # return for popping
                return self.name

def putNewSkillInHandAfterCast(skillName):
  global allButtons
  newSkillInfo = getNewSkill(skillName)

  # pop old skill and add in new skill
  for i in range(len(allButtons)):

    # find skill name
    if allButtons[i].name == skillName: 

      allButtons.pop(i)

      skillType = getSkillTypeFromName(skillName)

      if skillType == "attack":
        x = ATTACK_BUTTON_COORDS[i][0]
        y = ATTACK_BUTTON_COORDS[i][1]
      else:
        x = DEFENSE_BUTTON_COORDS[i-3][0]
        y = DEFENSE_BUTTON_COORDS[i-3][1]

      allButtons.insert(i, skillButton(x, y, BUTTON_WIDTH, BUTTON_HEIGHT, newSkillInfo))

def shuffleSkills():
  for i in allButtons:
    putNewSkillInHandAfterCast(i.name)
  
  doTurn(None, getCurrentEnemySkill())

class shuffleButton():
  def __init__(self, x = SHUFFLE_BUTTON_COORDS[0], y = SHUFFLE_BUTTON_COORDS[1], width = BUTTON_WIDTH, height = BUTTON_HEIGHT, text="Shuffle"):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text
    self.bgColor = SHUFFLE_BUTTON_COLOR

  def draw(self, font, screen):
    drawBoxBorders(screen, self.x,self.y,self.width,self.height, BORDER_COLOR)
          
    pygame.draw.rect(screen, THECOLORS[self.bgColor], (self.x,self.y,self.width,self.height))

    text = font.render("Shuffle", True, THECOLORS[TEXT_COLOR])
    screen.blit(text, (self.x-75 + (self.width - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

  def onOver(self, pos):
    #Pos is the mouse position or a tuple of (x,y) coordinates
    if pos[0] > self.x and pos[0] < self.x + self.width:
        if pos[1] > self.y and pos[1] < self.y + self.height:
            self.bgColor = HOVER_VALID_CAST_COLOR
            return;

    # reset color if not over
    self.bgColor = SHUFFLE_BUTTON_COLOR

  def onClick(self, pos):
    # check if dead
    if getUserHp() != 0:
      #Pos is the mouse position or a tuple of (x,y) coordinates
      if pos[0] > self.x and pos[0] < self.x + self.width:
          if pos[1] > self.y and pos[1] < self.y + self.height:
              shuffleSkills()

def createSkills(screen, font):
  global allButtons

  skillsInHand = getSkillsInHand()

  for i in range(len(ATTACK_BUTTON_COORDS)):
    oneButton = skillButton(ATTACK_BUTTON_COORDS[i][0], ATTACK_BUTTON_COORDS[i][1], BUTTON_WIDTH, BUTTON_HEIGHT, getSkillInfoFromName(skillsInHand[i]))
    allButtons.append(oneButton)

  for i in range(len(DEFENSE_BUTTON_COORDS)):
    oneButton = skillButton(DEFENSE_BUTTON_COORDS[i][0], DEFENSE_BUTTON_COORDS[i][1], BUTTON_WIDTH, BUTTON_HEIGHT, getSkillInfoFromName(skillsInHand[len(ATTACK_BUTTON_COORDS)+i]))
    allButtons.append(oneButton)

shuffle = shuffleButton()

# checks if a skill can be casted when a click event is fired
def checkSkillsClick():
  shuffle.onClick(pygame.mouse.get_pos())

  for oneButton in allButtons:
    skillName = oneButton.onClick(pygame.mouse.get_pos())

    if (skillName != None): # need to pop the skill because it was casted
      putNewSkillInHandAfterCast(skillName)

# draw 3 offense skills, 2 defense skills
def drawSkills(screen, font, smallerFont, smallestFont):
  global skillsHaveBeenDrawn

  if (not skillsHaveBeenDrawn):
    createSkills(screen, smallerFont)
    skillsHaveBeenDrawn = True

  shuffle.draw(font, screen)
  shuffle.onOver(pygame.mouse.get_pos())

  for oneButton in allButtons:
    oneButton.onOver(pygame.mouse.get_pos())
    oneButton.draw(smallerFont, smallestFont, screen)