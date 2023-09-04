# Example file showing a basic pygame "game loop"
import pygame
from logic import *
from shapes import space_ship

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
X, Y = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
BLOCKS = get_block_locations(space_ship(), X, Y)

# Need some state, say top left corner to store coordinates of things

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")
    for block in BLOCKS:
        pygame.draw.rect(
            screen, "black", pygame.Rect(block[0] - 10, block[1] + 10, 20, 20)
        )
    # flip() the display to put your work on screen
    pygame.display.flip()
    for block in BLOCKS:
        pygame.draw.rect(
            screen, "gray", pygame.Rect(block[0] - 10, block[1] + 10, 20, 20)
        )
    BLOCKS = center_blocks(cycle(BLOCKS), 720, 1280)

    # RENDER YOUR GAME HERE

    clock.tick(10)  # limits FPS to 60

pygame.quit()
