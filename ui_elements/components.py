# contains reusable drawing code
import pygame
from pygame.color import THECOLORS

# note : borders are drawn outwards
# Call this function before you draw your box
def drawBoxBorders(screen, x, y, width, height, borderColor="black", borderSize=5):
  pygame.draw.rect(
    screen, THECOLORS[borderColor], (x-borderSize, y-borderSize, width+borderSize*2, height+borderSize*2))

# note : borders are drawn outwards
# Call this function before you draw your circle
def drawCircleBorders(screen, x, y, radius, borderColor="black", borderSize=5):
  pygame.draw.circle(screen, THECOLORS[borderColor], (x, y), radius+borderSize)