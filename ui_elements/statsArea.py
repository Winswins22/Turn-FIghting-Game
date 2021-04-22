from ui_elements.healthBar import drawHP
from ui_elements.infoBar import drawInfo

# draw hp, turns, battles
def drawStats(screen, font, smallerFont):
  drawHP(screen, font)
  drawInfo(screen, smallerFont)