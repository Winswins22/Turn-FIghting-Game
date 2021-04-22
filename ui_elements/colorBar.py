import pygame

from ui_elements.components import drawBoxBorders
from data.manageData import getColors

from pygame.color import THECOLORS

# declare consts
TEXT_COLOR = "white"
BORDER_COLOR = "black"
BAR_BACKGROUND_COLOR = "white"

BAR_WIDTH = 700
BAR_HEIGHT = 50

START_X = 50
START_Y = 20

# graphic
def drawBar(screen):
  #borders
  drawBoxBorders(screen, START_X, START_Y, BAR_WIDTH, BAR_HEIGHT, BORDER_COLOR)
  #the actual box
  pygame.draw.rect(screen, THECOLORS[BAR_BACKGROUND_COLOR], (START_X, START_Y, BAR_WIDTH, BAR_HEIGHT))
  
def drawResources(screen, font):

  colors = getColors()
  currX = START_X

  pygame.draw.rect(screen, THECOLORS["red"], (currX, START_Y, colors["red"], BAR_HEIGHT))
  text = font.render(str(colors["red"]), True, THECOLORS[TEXT_COLOR])
  screen.blit(text, (currX, START_Y))

  currX += colors["red"]

  pygame.draw.rect(screen, THECOLORS["green"], (currX, START_Y, colors["green"], BAR_HEIGHT))
  text = font.render(str(colors["green"]), True, THECOLORS[TEXT_COLOR])
  screen.blit(text, (currX, START_Y))

  currX += colors["green"]

  pygame.draw.rect(screen, THECOLORS["blue"], (currX, START_Y, colors["blue"], BAR_HEIGHT))
  text = font.render(str(colors["blue"]), True, THECOLORS[TEXT_COLOR])
  screen.blit(text, (currX, START_Y))

  currX += colors["blue"]

  pygame.draw.rect(screen, THECOLORS["purple"], (currX, START_Y, colors["purple"], BAR_HEIGHT))
  text = font.render(str(colors["purple"]), True, THECOLORS[TEXT_COLOR])
  screen.blit(text, (currX, START_Y))

  currX += colors["purple"]

def drawColorBar(screen, font):
  drawBar(screen)
  drawResources(screen, font)