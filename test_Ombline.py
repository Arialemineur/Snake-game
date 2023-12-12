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
        T[0] = (self.position[0][0], self.position[0][1]+1)
        for i in range(1,n):
            T[i]=self.position[i-1]
        self.position = T
        draw_snake(self)

    def goes_down(self):
        L = self.position
        n= len(self.position)
        T=self.position.copy()
        T[0] = (self.position[0][0], self.position[0][1]-1)
        for i in range(1,n):
            T[i]=self.position[i-1]
        self.position = T
        draw_snake(self)

    def eats_fruit(self):
        X = (self.position[len(self.position)-2][0]-self.position[len(self.position)-1][0],self.position[len(self.position)-2][0]-self.position[len(self.position)-1][1])
        L = self.position
        L.append((self.position[len(self.position)-1][0]+X[0],self.position[len(self.position)-1][1]+X[1]))
        self.position = L

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


def game():
    L = Snake([[7, 10],[6, 10],[5, 10]])
    loc = Fruit([3,3])
    score = 0
    last_input = pygame.K_RIGHT
    last_move = pygame.K_RIGHT
    pygame.display.update()

    while True:

        clock.tick(1)

    for event in pygame.event.get():
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
