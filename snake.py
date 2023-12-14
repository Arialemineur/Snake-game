import pygame
import random as rd 

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((400, 300))


#pygame.init()

#screen = pygame.display.set_mode((400, 300))


"""
def affichage(L):
    if 
"""

class Fruit():
    def __init__(self, L):
        self.position = L

    def draw_fruit(self):
        for i in range(len(self.position)):
            pygame.draw.circle(screen, "red", (self.position[0]*20-10,self.position[1]*20-10), 9.5)

    def spawn_fruit(self):
        x= rd.randint(0,20)
        y = rd.randint(0,15)
        loc = [x,y]
        if not(loc in self.position):
            self.position = loc
            draw_fruit()
        else:
            spawn_fruit(self.position)


class Snake():
    def __init__(self, L):
        self.position = L

    def goes_up(self):
        L = self.position
        n= len(self.position)
        T=self.position.copy()
        T[0] = (self.position[0][0], self.position[0][1]-1)
        for i in range(1,n):
            T[i]=self.position[i-1]
        self.position = T
        self.draw_snake()
        
    def goes_down(self):
        L = self.position
        n= len(self.position)
        T=self.position.copy()
        T[0] = (self.position[0][0], self.position[0][1]+1)
        for i in range(1,n):
            T[i]=self.position[i-1]
        self.position = T
        self.draw_snake()

    def eats_fruit(self):
        X = (self.position[len(self.position)-2][0]-self.position[len(self.position)-1][0],self.position[len(self.position)-2][0]-self.position[len(self.position)-1][1])
        L = self.position
        L.append((self.position[len(self.position)-1][0]+X[0],self.position[len(self.position)-1][1]+X[1]))
        self.position = L
        self.draw_snake()

    def goes_right(self):
        L = self.position
        n= len(L)
        T=L.copy()
        T[0] = (L[0][0]+1, L[0][1])
        for i in range(1,n):
            T[i]=L[i-1]
        self.position = T
        self.draw_snake()

    def goes_left(self):
        L = self.position
        n= len(L)
        T=L.copy()
        T[0] = (L[0][0]-1, L[0][1])
        for i in range(1,n):
            T[i]=L[i-1]
        self.position = T
        self.draw_snake()

    def draw_snake(self):
        for i in range(len(self.position)):
            pygame.draw.circle(screen, "blue", (self.position[i][0]*20-10,self.position[i][1]*20-10), 9.5)

    def refresh(self):
        for i in range(len(self.position)):
            self.position[i] = [self.position[i][0]%20, self.position[i][1]%15]


def game():
    clock = pygame.time.Clock()
    L = Snake([[7, 10],[6, 10],[5, 10]])
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
                L.goes_up()
            if last_input == pygame.K_DOWN and last_move != pygame.K_UP:
                L.goes_down()
            if last_input == pygame.K_LEFT and last_move != pygame.K_RIGHT:
                L.goes_left()
            if last_input == pygame.K_RIGHT and last_move != pygame.K_LEFT:
                L.goes_right()
            last_move = last_input
            if L.position[0] == loc:
                L.eats_fruit()
                loc.spawn_fruit(L)
                loc.draw_fruit()
                score += 1
            if L.position[0] in L.position[1:]:
                pygame.quit()
        pygame.display.update()

game()