import random, pygame, sys
from pygame.locals import *

WIDTH = 1000
HEIGHT = 500

WHITE = (255, 255, 255)
BLACK = (0,   0,   0  )
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Block(pygame.sprite.Sprite):
  def __init__(self):
    super(Block, self).__init__()
    self.image = pygame.Surface([20, 15])
    self.image.fill(BLUE)

    self.rect = self.image.get_rect()

  def update(self):
    self.rect.y += 1

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.image = pygame.Surface([25, 15])
    self.image.fill(RED)

    self.rect = self.image.get_rect()

  def update(self):
    mouse_pos = pygame.mouse.get_pos()
    self.rect.x = mouse_pos[0]

class Bullet(pygame.sprite.Sprite):
  def __init__(self):
    super(Bullet, self).__init__()
    self.image = pygame.Surface([5, 10])
    self.image.fill(BLACK)

    self.rect = self.image.get_rect()

  def update(self):
    self.rect.y -= 3


class Game(object):
  def start(self):
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Invader")
    DISPLAYSURF.fill(WHITE)
    FPS = 60
    clock = pygame.time.Clock()

    block_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    for i in range(50):
      block = Block()
      block.rect.x = random.randrange(0, WIDTH)
      block.rect.y = random.randrange(0, HEIGHT - 20)
      block_list.add(block)
      all_sprites.add(block)

    player = Player()
    player.rect.y = HEIGHT - 20
    all_sprites.add(player)

    while(True):
      
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
          bullet = Bullet()
          bullet.rect.x = player.rect.x
          bullet.rect.y = player.rect.y
          bullet_list.add(bullet)
          all_sprites.add(bullet)

      for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, False)

        for block in block_hit_list:
          bullet_list.remove(bullet)
          all_sprites.remove(bullet)
          all_sprites.remove(block)
          block_list.remove(block)

        if bullet.rect.y < 0:
          bullet_list.remove(bullet)
          all_sprites.remove(bullet)

      DISPLAYSURF.fill(WHITE)

      all_sprites.update()
      all_sprites.draw(DISPLAYSURF)
      pygame.display.update()

      clock.tick(FPS)


if __name__ == "__main__":
  game = Game()
  game.start()
