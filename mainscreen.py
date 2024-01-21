import pygame
import sys


pygame.init()


width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Picking Mushroom")


white = (255, 255, 255)
blue = (0, 0, 255)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




    screen.fill(white)



 
    pygame.display.flip()