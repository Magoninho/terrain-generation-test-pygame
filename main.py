"""

Perlin noise is a little bit hard on python
So, if you know how to implement it, send a pull request :)

"""

import pygame
import random

TILESIZE = 16
GWIDTH = 60
GHEIGHT = 40
WIDTH = GWIDTH * TILESIZE
HEIGHT = GHEIGHT * TILESIZE

# colors
WHITE = (255, 255, 255)

# display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

heights = [random.randint(0, GHEIGHT - 1)
           for h in range(GWIDTH)
           ]

print(heights)


def draw_terrain():
    for x in range(GWIDTH):
        for h in range(heights[x]):
            pygame.draw.rect(
                screen,
                WHITE,
                (x * TILESIZE,
                 HEIGHT - h * TILESIZE,
                 TILESIZE - 1,
                 TILESIZE - 1)
            )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    draw_terrain()

    pygame.display.update()
