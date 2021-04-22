import pygame
from math import floor

class Player(pygame.sprite.Sprite):
  def __init__(self, characterName, x, y):
    super().__init__()
    self.sprites = []

    if characterName == "player":
      self.sprites.append(pygame.image.load('sprite_data/player/mage1.png'))
      self.sprites.append(pygame.image.load('sprite_data/player/mage2.png'))
      self.sprites.append(pygame.image.load('sprite_data/player/mage3.png'))
      self.sprites.append(pygame.image.load('sprite_data/player/mage4.png'))
      self.sprites.append(pygame.image.load('sprite_data/player/mage5.png'))
      self.sprites.append(pygame.image.load('sprite_data/player/mage6.png'))
      self.sprites.append(pygame.image.load('sprite_data/player/mage7.png'))
      self.sprites.append(pygame.image.load('sprite_data/player/mage8.png'))
      self.sprites.append(pygame.image.load('sprite_data/player/mage9.png'))

    elif characterName == "enemy":
      self.sprites.append(pygame.image.load('sprite_data/enemy/mage1.png'))
      self.sprites.append(pygame.image.load('sprite_data/enemy/mage2.png'))
      self.sprites.append(pygame.image.load('sprite_data/enemy/mage3.png'))
      self.sprites.append(pygame.image.load('sprite_data/enemy/mage4.png'))
      self.sprites.append(pygame.image.load('sprite_data/enemy/mage5.png'))
      self.sprites.append(pygame.image.load('sprite_data/enemy/mage6.png'))
      self.sprites.append(pygame.image.load('sprite_data/enemy/mage7.png'))
      self.sprites.append(pygame.image.load('sprite_data/enemy/mage8.png'))
    
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]

    self.rect = self.image.get_rect()
    self.rect.topleft = [x,y]

  def update(self):

    speed = 1/len(self.sprites)

    self.current_sprite += speed

    if self.current_sprite >= len(self.sprites):
      self.current_sprite = 0

    self.image = self.sprites[floor(self.current_sprite)]
  

  #def draw(self, screen):
  #  screen.blit(self.image, (self.x, self.y))