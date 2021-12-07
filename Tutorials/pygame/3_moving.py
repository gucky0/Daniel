import pygame, ctypes, time
from pygame.locals import *
BG_COLOR = (214,255,254)
filename_block = "../../Resources/block.jpg"
screensize = ctypes.windll.user32.GetSystemMetrics(78), ctypes.windll.user32.GetSystemMetrics(79)

class Snake:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load(filename_block).convert()
        self.x = 100
        self.y = 100
        self.direction = 'down' # set default position
    # update snake direction
    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'
    # map snake direction to snake position
    def walk(self):
        if self.direction == 'left':
            self.x -= 10
        if self.direction == 'right':
            self.x += 10
        if self.direction == 'up':
            self.y -= 10
        if self.direction == 'down':
            self.y += 10
        self.draw()

    def draw(self):
        self.parent_screen.fill(BG_COLOR)
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface)
        self.snake.draw()
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
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
            # update position after a fixed interval
            time.sleep(.2)
            self.snake.walk()

if __name__ == '__main__':
    game = Game()
    game.run()

