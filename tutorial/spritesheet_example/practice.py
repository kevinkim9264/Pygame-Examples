import pygame, sys
from pygame.locals import *

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 450

class Player(pygame.sprite.Sprite):

  def __init__(self):
    super(Player, self).__init__()
    self.image = pygame.Surface([25, 15])
    self.image.fill(RED)

    self.velocity_x = 0
    self.velocity_y = 0

    self.rect = self.image.get_rect()

    self.rect.x = WIDTH / 2 - self.rect.width
    self.rect.y = HEIGHT / 2 - self.rect.height

  def go_left(self):
    self.velocity_x += -6

  def go_right(self):
    self.velocity_x += 6

  def go_up(self):
    self.velocity_y += -6

  def go_down(self):
    self.velocity_y += 6

  def stop_x(self):
    self.velocity_x = 0

  def stop_y(self):
    self.velocity_y = 0

""" Abstract class Map, which will be inherited by specific maps."""
class Map(object):
  def __init__(self, player):
    self.player = player
    self.wall_list = pygame.sprite.Group()
    self.world_shift_x = 0
    self.world_shift_y = 0

  def update(self):
    self.world_shift_x = -1 * self.player.velocity_x
    self.world_shift_y = -1 * self.player.velocity_y
    
    self.wall_list.update(self.world_shift_x, 0)
    if self.collide():
      self.wall_list.update(-1 * self.world_shift_x, 0)

    self.wall_list.update(0, self.world_shift_y)
    if self.collide():
      self.wall_list.update(0, -1 * self.world_shift_y)
  

  def draw(self, screen):
    screen.fill(WHITE)
    self.wall_list.draw(screen)

  def collide(self):
    collide_list = pygame.sprite.spritecollide(self.player, self.wall_list, False)
    if len(collide_list) > 0:
      return True

""" Level 1 Map """
class LevelOne(Map):
  def __init__(self, player):
    super(LevelOne, self).__init__(player)
    # x_pos, y_pos, width, height
    walls = [ [WIDTH*9/10, HEIGHT*3/10, 40, 150],
              [-40, HEIGHT*5/10, 50, 200],
              [WIDTH*5/10, HEIGHT*9/10, 300, 100],
              [-100, -100, 40, HEIGHT + 200],
              [-100, -100, WIDTH + 200, 40],
              [WIDTH + 100, -100, 40, HEIGHT + 200],
              [-100, HEIGHT + 100, WIDTH + 200, 40]
            ]

    for wall in walls:
      new_wall = Wall(wall[0], wall[1], wall[2], wall[3])
      self.wall_list.add(new_wall)


""" Wall sprite """
class Wall(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height):
    super(Wall, self).__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)

    self.rect = self.image.get_rect()

    self.rect.x = x
    self.rect.y = y

  def update(self, shift_x, shift_y):
    self.rect.x += shift_x
    self.rect.y += shift_y


class Game(object):
  def start(self):
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Baram?")
    DISPLAYSURF.fill(WHITE)
    FPS = 60
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    
    player = Player()

    all_sprites.add(player)
    current_map = LevelOne(player)
    

    while(True):

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            player.go_left()
          elif event.key == pygame.K_RIGHT:
            player.go_right()
          elif event.key == pygame.K_UP:
            player.go_up()
          elif event.key == pygame.K_DOWN:
            player.go_down()
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
            player.go_right()
          elif event.key == pygame.K_RIGHT:
            player.go_left()
          elif event.key == pygame.K_UP:
            player.go_down()
          elif event.key == pygame.K_DOWN:
            player.go_up()

      
      current_map.update()

      #### DRAWING GOES BELOW THIS LINE
      DISPLAYSURF.fill(WHITE)

      current_map.draw(DISPLAYSURF)
      all_sprites.draw(DISPLAYSURF)
      

      pygame.display.update()
      clock.tick(FPS)

if __name__ == "__main__":
  game = Game()
  game.start()
      

    
  
