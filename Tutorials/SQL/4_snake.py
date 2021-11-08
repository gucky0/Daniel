import pygame, ctypes, time
from pygame.locals import *
BG_COLOR = (214,255,254)
filename_block = "../../Resources/block.jpg"
filename_apple = "../../Resources/apple.jpg"
screensize = ctypes.windll.user32.GetSystemMetrics(78), ctypes.windll.user32.GetSystemMetrics(79)
SIZE = 40

class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(filename_block).convert()
        self.direction = 'down'
        self.length = length # initialise length
        self.x = [40]*length # set lengths for each segment
        self.y = [200, 160, 120, 80, 40] 

    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1): # [4,3,2,1]
            self.x[i] = self.x[i-1]         # [3,2,1,0]
            self.y[i] = self.y[i-1]
        # update head position
        if self.direction == 'left':
            self.x[0] -= SIZE # shift by 1 segment size each time
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        self.draw()

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        # create snake segments
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface, 5) # set starting snake length
        self.snake.draw()
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
            self.snake.walk()
            time.sleep(.2)

if __name__ == '__main__':
    game = Game()
    game.run()

