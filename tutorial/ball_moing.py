import pygame, sys, os, random
from pygame.locals import *

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (450,200)
WIDTH = 500
HEIGHT = 350

WHITE = (255, 255, 255)
BLACK = (0  , 0  , 0  )
RED = (255, 0, 0)

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), )
pygame.display.set_caption("Ball moving!")

class Block(pygame.sprite.Sprite):
  def __init__(self, width, height, color):
    super(Block, self).__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill(color)
    self.rect = self.image.get_rect()



class App(object):
  def __init__(self):
    pass
  
  def main(self):
    pygame.init()
    INITIAL_X = 30
    INITIAL_Y = 50
    block_list = pygame.sprite.Group()
    block = Block(20, 25, BLACK)
    block_list.add(block)

    clock = pygame.time.Clock()
    block.rect.x = INITIAL_X
    block.rect.y = INITIAL_Y
    
    while (True):
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_UP:
            block.rect.y -= 2
          elif event.key == K_DOWN:
            block.rect.y += 2
          elif event.key == K_LEFT:
            block.rect.x -= 2
          elif event.key == K_RIGHT:
            block.rect.x += 2
          
      

      DISPLAYSURF.fill(WHITE)
      block_list.draw(DISPLAYSURF)   
      pygame.display.update()

      clock.tick(80)


if __name__ == "__main__":
  app = App()
  app.main()
