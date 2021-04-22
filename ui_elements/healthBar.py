import pygame

from ui_elements.components import drawBoxBorders
from data.manageData import getUserHp

from pygame.color import THECOLORS

TEXT_COLOR = "white"
BORDER_COLOR = "black"
BORDER_THICKNESS = 5

NO_HP_COLOR = "red"
HP_COLOR = "green"
HP_BAR_X = 25
HP_BAR_Y = 275
HP_BAR_WIDTH = 200
HP_BAR_HEIGHT = 50

def drawHP(screen, font):
  heart = pygame.image.load("images/heart.png")

  # get info
  userHealth = getUserHp()

  #borders
  drawBoxBorders(screen, HP_BAR_X, HP_BAR_Y, HP_BAR_WIDTH, HP_BAR_HEIGHT, BORDER_COLOR)

  # draw HP background
  pygame.draw.rect(screen, THECOLORS[HP_COLOR], (HP_BAR_X, HP_BAR_Y, userHealth, HP_BAR_HEIGHT))
  pygame.draw.rect(screen, THECOLORS[NO_HP_COLOR], (HP_BAR_X + userHealth, HP_BAR_Y, HP_BAR_WIDTH - userHealth, HP_BAR_HEIGHT))


  # draw HP bar + image
  screen.blit(heart, (HP_BAR_X-10, HP_BAR_Y-10))
  HPText = font.render(str(userHealth), True, THECOLORS[TEXT_COLOR])
  screen.blit(HPText, (HP_BAR_X + 50, HP_BAR_Y))