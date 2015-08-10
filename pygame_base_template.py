"""
 Show how to use a sprite backed by a graphic.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

rect_x = 50
rect_y = 50

rect_size_x = 70
rect_size_y = 50

rect_change_x = 5
rect_change_y = 5
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, rect_size_x, rect_size_y])

    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_y > size[1]-rect_size_y or rect_y < 0:
      rect_change_y = rect_change_y * -1
    if rect_x > size[0]-rect_size_x or rect_x < 0:
      rect_change_x = rect_change_x * -1
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
