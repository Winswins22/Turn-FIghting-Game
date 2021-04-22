import pygame
from pygame.color import THECOLORS

from userInterface import drawUI

from data.manageData import *
from ui_elements.colorBar import drawColorBar
from ui_elements.skillsArea import drawSkills
from ui_elements.playerSprite import Player

from ui_elements.skillsArea import checkSkillsClick

# Setup const
SCREEN_WIDTH = 775
SCREEN_HEIGHT = 400
FPS = 60

# Setup pygame window
pygame.init() 
clock = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
screen = pygame.display.get_surface() 
pygame.display.set_caption('Animation') 

done = False

# Setup vars
BACKGROUND_COLOR = THECOLORS["grey"] 
font = pygame.font.SysFont("Comic Sans MS", 80)
smallerFont = pygame.font.SysFont("Comic Sans MS", 40)  
smallestFont = pygame.font.SysFont("Comic Sans MS", 20) 
# shhh i ran out of names to make it sound even smaller
smallerestFont =  pygame.font.SysFont("Comic Sans MS", 15) 

# Creating the sprites and groups
player = pygame.sprite.Group()
enemy = pygame.sprite.Group()

playerSprite = Player("player", 50,101)
enemySprite = Player("enemy", 600,145)

player.add(playerSprite)
enemy.add(enemySprite)

resetData()

# Game loop
while not done:

  # loop thru events
  for e in pygame.event.get():

    if e.type == pygame.QUIT:
      done = True
    
    if e.type == pygame.MOUSEBUTTONDOWN:
      
      # if left click
      if (e.button == 1):
        checkSkillsClick()

  # Draw background
  screen.fill(BACKGROUND_COLOR)

  # Draw items
  drawSkills(screen, smallerFont, smallerFont, smallerestFont)
  drawColorBar(screen, font)
  drawUI(screen, font, smallerFont, smallestFont, smallerestFont)

  # Sprites
  if getUserHp() != 0:
    player.draw(screen)
    player.update()

  if getEnemyHp() != 0:
    enemy.draw(screen)
    enemy.update()

  # draw the secreen + determine fps
  pygame.display.flip()
  clock.tick(FPS)

# Quit the program
pygame.quit()