# Contains HP bar, stats, skills, and activation of those skills
import pygame

from ui_elements.components import drawBoxBorders
from ui_elements.statsArea import drawStats
from ui_elements.skillsArea import drawSkills
from ui_elements.enemyUI import drawEnemyUI

from math import floor
from pygame.color import THECOLORS

# declare consts
TEXT_COLOR = "white"

BORDER_COLOR = "black"
BORDER_THICKNESS = 5
BACKGROUND_COLOR = "cyan"

BG_START_X = 0
BG_START_Y = 250
BG_WIDTH = 775
BG_HEIGHT = 150

# graphic
def drawBackground(screen):
  #borders
  drawBoxBorders(screen, BG_START_X, BG_START_Y, BG_WIDTH, BG_HEIGHT, BORDER_COLOR)
  #the actual box
  pygame.draw.rect(screen, THECOLORS[BACKGROUND_COLOR], (BG_START_X, BG_START_Y, BG_WIDTH, BG_HEIGHT))

def drawLineSplit(screen):
  pygame.draw.line(screen, THECOLORS[BORDER_COLOR],
    (floor((BG_START_X+BG_WIDTH)/3), BG_START_Y),
    (floor((BG_START_X+BG_WIDTH)/3), BG_START_Y+BG_HEIGHT),
    BORDER_THICKNESS
  )

def drawUI(screen, font, smallerFont, smallestFont, smallerestFont):
  drawBackground(screen)
  drawLineSplit(screen)
  drawStats(screen, font, smallerFont)
  drawSkills(screen, smallerFont, smallestFont, smallerestFont)
  drawEnemyUI(screen, smallerFont, smallestFont, smallerestFont)