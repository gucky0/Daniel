import pygame, ctypes
from pygame.locals import *
BG_COLOR = (214,255,254)
filename_block = "../../Resources/block.jpg"
screensize = ctypes.windll.user32.GetSystemMetrics(78), ctypes.windll.user32.GetSystemMetrics(79)

# handling snake object
class Snake:
    # create block object
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load(filename_block).convert()
        self.x = 100
        self.y = 100
    def move_left(self):
        self.x -= 10
    def move_right(self):
        self.x += 10
    def move_up(self):
        self.y -= 10
    def move_down(self):
        self.y += 10
    # update snake position on the screen
    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
# handling pygame
class Game:
    # initialize starting screen
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(screensize)
        self.snake = Snake(self.surface) # create snake class and pass in screen object
        self.snake.draw()
    # template pygame event handler
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                # map key press to functions 
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
                    self.snake.draw()
# creating game class and running 
if __name__ == '__main__':
    game = Game()
    game.run()
