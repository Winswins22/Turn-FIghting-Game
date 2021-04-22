import pygame

from ui_elements.components import drawBoxBorders
from data.manageData import getStats

from pygame.color import THECOLORS

TEXT_COLOR = "white"
BORDER_COLOR = "black"
BORDER_THICKNESS = 5

STATS_BG_COLOR = "green"
STATS_BAR_X = 25
STATS_BAR_Y = 340
STATS_BAR_WIDTH = 200
STATS_BAR_HEIGHT = 50

def drawInfo(screen, font):
  # get info
  stats = getStats()

  turns = font.render("Turns: " + str(stats["turns"]), True, THECOLORS[TEXT_COLOR])
  battles =  font.render("Battles: " +  str(stats["battles"]), True, THECOLORS[TEXT_COLOR])

  # draw box
  drawBoxBorders(screen, STATS_BAR_X, STATS_BAR_Y, STATS_BAR_WIDTH, STATS_BAR_HEIGHT, BORDER_COLOR)

  pygame.draw.rect(screen, THECOLORS[STATS_BG_COLOR], (STATS_BAR_X, STATS_BAR_Y, STATS_BAR_WIDTH, STATS_BAR_HEIGHT))

  # draw info
  screen.blit(turns, (STATS_BAR_X, STATS_BAR_Y))
  screen.blit(battles, (STATS_BAR_X, STATS_BAR_Y + 25))