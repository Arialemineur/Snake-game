import pygame

pygame.init()

screen = pygame.display.set_mode( (640, 480) )

clock = pygame.time.Clock()

L = [[1,2,3], [1,1,1]]

while True:

    clock.tick(1)

    for event in pygame.event.get():
        pass

    screen.fill( (0, 255, 0) )

    for i in range(len(L[0])):
        pygame.draw.circle(screen, "blue", (L[0][i]*20-10,L[1][i]*20-10), 9.5)

    pygame.display.update()
