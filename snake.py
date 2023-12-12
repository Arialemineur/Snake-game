import pygame

pygame.init()

screen = pygame.display.set_mode( (400, 300) )

clock = pygame.time.Clock()

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
    L.append((L[len(L)-1][0]+X[0],L[len(L)-1][1]+X[1])
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
    if L[0] in L[1:]:
        pygame.quit()


    screen.fill( (0, 255, 0) )

    pygame.display.update()

