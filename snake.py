import pygame
import random  

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode( (400, 300) )
pygame.draw.rect(screen, red, (50, 100, 100, 50))


"""
def affichage(L):
    if 
"""
clock = pygame.time.Clock()

while True:

    clock.tick(1)

    for event in pygame.event.get():
        pass

    screen.fill( (0, 255, 0) )

    pygame.display.update()

pygame.quit()

