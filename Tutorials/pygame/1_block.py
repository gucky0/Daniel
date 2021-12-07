import pygame
from pygame.locals import *
BG_COLOR = (214,255,254)
filename_block = "../../Resources/block.jpg"

# update snake position on the screen
def draw_block():
    # wipe the screen
    surface.fill(BG_COLOR)
    # insert object 
    surface.blit(block, (block_x, block_y))
    # update the screen
    pygame.display.flip()

if __name__ == '__main__':
    # template pygame initialise
    pygame.init()
    surface = pygame.display.set_mode((500, 500))
    # get block object
    block = pygame.image.load(filename_block).convert()
    block_x, block_y = 100, 100
    # initialise starting screen
    surface.fill(BG_COLOR)
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()
    # template pygame event handler
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
                    block_x -= 10
                if event.key == K_RIGHT:
                    block_x += 10
                if event.key == K_UP:
                    block_y -= 10
                if event.key == K_DOWN:
                    block_y += 10
                draw_block()


            