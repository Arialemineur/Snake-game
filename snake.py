import pygame
import random as rd 

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((400, 300))

import sys

width, height = 400, 300
screen = pygame.display.set_mode((width, height))
echiquier  = pygame.display.set_mode((width, height))
case_size = 20
pygame.display.set_caption('Dessin avec Pygame')
# Paramètres de la fenêtre


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

    score_text = font.render("Score: {}".format(score), True, (255,20,147))
    screen.blit(score_text, (10, 10))




class Fruit():
    def __init__(self, fruit_position):
        self.position = fruit_position

    def draw_fruit(self):
        for i in range(len(self.position)):
            pygame.draw.circle(screen, "red", (self.position[0] * 20 - 10,self.position[1] * 20 - 10), 9.5)

    def spawn_fruit(self):
        x= rd.randint(0,20)
        y = rd.randint(0,15)
        loc = [x,y]
        if not(loc in self.position):
            self.position = loc
            self.draw_fruit()
        else:
            self.spawn_fruit(self.position)


class Snake():
    def __init__(self, snake_position):
        self.position = snake_position

    def goes_up(self):
        snake_position = self.position
        lengh_snake = len(self.position)
        new_positions = self.position.copy()
        new_positions[0] = (self.position[0][0], self.position[0][1] - 1)
        for i in range(1,lengh_snake):
            new_positions[i] = self.position[i - 1]
        self.position = new_positions
        self.draw_snake()
        
    def goes_down(self):
        snake_position = self.position
        lengh_snake = len(self.position)
        new_positions = self.position.copy()
        new_positions[0] = (self.position[0][0], self.position[0][1] + 1)
        for i in range(1,lengh_snake):
            new_positions[i] = self.position[i - 1]
        self.position = new_positions
        self.draw_snake()

    def eats_fruit(self):
        elongation = (self.position[len(self.position) - 2][0] - self.position[len(self.position) - 1][0],self.position[len(self.position) - 2][1] - self.position[len(self.position) - 1][1])
        snake_position = self.position
        snake_position.append((self.position[len(self.position) - 1][0] + elongation[0],self.position[len(self.position) - 1][1] + elongation[1]))
        self.position = snake_position
        self.draw_snake()

    def goes_right(self):
        snake_position = self.position
        lengh_snake = len(snake_position)
        new_positions = snake_position.copy()
        new_positions[0] = (snake_position[0][0] + 1, snake_position[0][1])
        for i in range(1,lengh_snake):
            new_positions[i] = snake_position[i - 1]
        self.position = new_positions
        self.draw_snake()

    def goes_left(self):
        snake_position = self.position
        lengh_snake = len(snake_position)
        new_positions = snake_position.copy()
        new_positions[0] = (snake_position[0][0] - 1, snake_position[0][1])
        for i in range(1,lengh_snake):
            new_positions[i] = snake_position[i - 1]
        self.position = new_positions
        self.draw_snake()

    def draw_snake(self):
        for i in range(len(self.position)):
            pygame.draw.circle(screen, "blue", (self.position[i][0] * 20 - 10,self.position[i][1] * 20 - 10), 9.5)

    def refresh(self):
        for i in range(len(self.position)):
            self.position[i] = [self.position[i][0] % 20, self.position[i][1] % 15]


def game():
    clock = pygame.time.Clock()
    snake_position = Snake([[7, 10],[6, 10],[5, 10]])
    loc = Fruit([3,3])
    score = 0
    last_input = pygame.K_RIGHT
    last_move = pygame.K_RIGHT
    pygame.display.update()
    loc.draw_fruit()

    while True:

        clock.tick(10)

        for event in pygame.event.get():
            screen = pygame.display.set_mode((400, 300))
            if event.type == pygame.KEYDOWN:
                last_input = event.key
            if last_input == pygame.K_ESCAPE:
                pygame.quit()
            if last_input == pygame.K_UP and last_move != pygame.K_DOWN :
                snake_position.goes_up()
            if last_input == pygame.K_DOWN and last_move != pygame.K_UP:
                snake_position.goes_down()
            if last_input == pygame.K_LEFT and last_move != pygame.K_RIGHT:
                snake_position.goes_left()
            if last_input == pygame.K_RIGHT and last_move != pygame.K_LEFT:
                snake_position.goes_right()
            last_move = last_input
            if snake_position.position[0] == loc:
                snake_position.eats_fruit()
                loc.spawn_fruit(snake_position)
                loc.draw_fruit()
                score += 1
            if snake_position.position[0] in snake_position.position[1:]:
                pygame.quit()
        pygame.display.update()

game()