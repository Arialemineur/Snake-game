import pygame
<<<<<<< HEAD
import random  

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode( (400, 300) )
pygame.draw.rect(screen, red, (50, 100, 100, 50))
=======
import random as rd

pygame.init()

screen = pygame.display.set_mode((400, 300))
>>>>>>> b049be3c71cf92ff29acce8692edf15eee1bc1b4


"""
def affichage(L):
    if 
"""
clock = pygame.time.Clock()


class fruit():
    def __init__(self, L):
        self.position = L

    def draw_fruit(self):
        for i in range(len(self.position)):
            pygame.draw.circle(screen, "red", (self.position[0]*20-10,self.position[1]*20-10), 9.5)
        return None

    def spawn_fruit(self):
        x= rd.randint(0,20)
        y = rd.randint(0,15)
        loc = [x,y]
        if not(loc in self.position):
            return loc
        else:
            spawn_fruit(self.position)

class snake():
    def __init__(self, L):
        self.position = L

    def goes_up(self):
        L = self.position
        n= len(self.position)
        T=self.position.copy()
        T[0] = (self.position[0][0], self.position[0][1]+1)
        for i in range(1,n):
            T[i]=self.position[i-1]
        self.position = T

    def goes_down(self):
        L = self.position
        n= len(self.position)
        T=self.position.copy()
        T[0] = (self.position[0][0], self.position[0][1]-1)
        for i in range(1,n):
            T[i]=self.position[i-1]
        self.position = T

    def eats_fruit(self):
        X = (self.position[len(self.position)-2][0]-self.position[len(self.position)-1][0],self.position[len(self.position)-2][0]-self.position[len(self.position)-1][1])
        self.position.append((self.position[len(self.position)-1][0]+X[0],self.position[len(self.position)-1][1]+X[1]))
        return self.position

    def goes_right(self):
        L = self.position
        n= len(L)
        T=L.copy()
        T[0] = (L[0][0]+1, L[0][1])
        for i in range(1,n):
            T[i]=L[i-1]
        self.position = T

    def goes_left(self):
        L = self.position
        n= len(L)
        T=L.copy()
        T[0] = (L[0][0]-1, L[0][1])
        for i in range(1,n):
            T[i]=L[i-1]
        self.position = T

    def draw_snake(L):
    for i in range(len(L)):
        pygame.draw.circle(screen, "blue", (L[i][0]*20-10,L[i][1]*20-10), 9.5)

    def refresh(self):
        for i in range(L):
            [L[i][0], L[i][1]] = [L[i][0]%20, L[i][1]%15]

L=[[7, 10],[6, 10],[5, 10]]
loc = spawn_fruit(L)
last_input = pygame.K_RIGHT
last_move = pygame.K_RIGHT
draw_snake(L)
draw_fruit(loc)
pygame.display.update()

while True:

    clock.tick(1)

    for event in pygame.event.get():
<<<<<<< HEAD
        pass

    screen.fill( (0, 255, 0) )

    pygame.display.update()

pygame.quit()

=======
        if event.type == pygame.KEYDOWN:
            last_input = event.key
        if last_input == pygame.K_ESCAPE:
            pygame.quit()
        if last_input == pygame.K_UP and last_move != pygame.K_DOWN :
            L=goes_up(L)
        if last_input == pygame.K_DOWN and last_move != pygame.K_UP:
            L=goes_down(L)
        if last_input == pygame.K_LEFT and last_move != pygame.K_RIGHT:
            L=goes_left(L)
        if last_input == pygame.K_RIGHT and last_move != pygame.K_LEFT:
            L=goes_right(L)
        last_move = last_input
        if L[0] == loc:
            L = eats_fruit(L)
            loc = spawn_fruit(L)
            draw_fruit(L)
        if L[0] in L[1:]:
            pygame.quit()
        L.refresh()
        draw_snake(L)
    pygame.display.update()
>>>>>>> b049be3c71cf92ff29acce8692edf15eee1bc1b4
