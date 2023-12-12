import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
echiquier  = pygame.display.set_mode((width, height))
case_size = 20
pygame.display.set_caption('Dessin avec Pygame')

import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Affichage d\'un Score avec Pygame')

# Couleur
black = (0, 0, 0)
white = (255, 255, 255)

# Score initial
score = 0

# Police
font = pygame.font.Font(None, 36)

# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#échiquier
echiquier.fill(white)

for i in range(20):
    for j in range(15):
        color = white if (i + j) % 2 == 0 else black
        pygame.draw.rect(echiquier, color, (i * case_size, j * case_size, case_size, case_size))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Effacer l'écran
    #screen.fill((255, 255, 255))

    #code à rajouter serpent
    #texte du score
    score_text = font.render("Score: {}".format(score), True, (255,20,147))
    screen.blit(score_text, (10, 10))

    # Rafraîchir l'écran
    pygame.display.flip()