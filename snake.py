import pygame
import random as rd

pygame.init()

screen = pygame.display.set_mode( (400, 300) )

clock = pygame.time.Clock()

def spawn_fruit(L):
    x= rd.randint(399)
    loc = (x//20,x%20)
    if not(lox in L):
        return loc
    else:
        spawn_fruit(L)

def goes_up(L):
    n= len(L)
    T=L.copy()
    T[0] = (L[0][0], L[0][1]+1)
    for i in range(1,n):
        T[i]=L[i-1]
    return T

def goes_down(L):
    n= len(L)
    T=L.copy()
    T[0] = (L[0][0], L[0][1]-1)
    for i in range(1,n):
        T[i]=L[i-1]
    return T

def eats_fruit(L):
    X = (L[len(L)-2][0]-L[len(L)-1][0],L[len(L)-2][0]-L[len(L)-1][1])
    L.append((L[len(L)-1][0]+X[0],L[len(L)-1][1]+X[1]))
    return L

def goes_right(L):
    n= len(L)
    T=L.copy()
    T[0] = (L[0][0]+1, L[0][1])
    for i in range(1,n):
        T[i]=L[i-1]
    return T

def goes_left(L):
    n= len(L)
    T=L.copy()
    T[0] = (L[0][0]-1, L[0][1])
    for i in range(1,n):
        T[i]=L[i-1]
    return T


L=[(5, 10),(6, 10),(7, 10)]
loc = spawn_fruit(L)
last_input = pygame.K_RIGHT
last_move = pygame.K_RIGHT
while True:

    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            last_input = event.key
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
        if event.key == pygame.K_UP and last_move != pygame.K_DOWN :
            L=goes_up(L)
        if event.key == pygame.K_DOWN and last_move != pygame.K_UP:
            L=goes_down(L)
        if event.key == pygame.K_LEFT and last_move != pygame.K_RIGHT:
            L=goes_left(L)
        if event.key == pygame.K_RIGHT and last_move != pygame.K_LEFT:
            L=goes_right(L)
        last_move = last_input
    if L[0] == loc:
        L = eats_fruit(L)
        loc = spawn_fruit(L)
        draw_fruit(L)
    if L[0] in L[1:]:
        pygame.quit()


    screen.fill( (0, 255, 0) )

    pygame.display.update()



def draw_snake(L):
    for i in range(len(L[0])):
        pygame.draw.circle(screen, "blue", (L[0][i]*20-10,L[1][i]*20-10), 9.5)
    return None

def draw_fruit(L):
    for i in range(len(L[0])):
        pygame.draw.circle(screen, "red", (L[0][i]*20-10,L[1][i]*20-10), 9.5)