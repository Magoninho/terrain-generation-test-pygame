"""

Perlin noise is a little bit hard on python
So, if you know how to implement it, send a pull request :)

"""

import pygame
import random

TILESIZE = 16
GWIDTH = 32
GHEIGHT = 16
WIDTH = GWIDTH * TILESIZE
HEIGHT = GHEIGHT * TILESIZE

#######################################
# settings #

max_height = 12
amplitude = 2

#######################################


# colors
WHITE = (255, 255, 255)

colors = (
    (255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255)
)

# display
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def lerp(v0, v1, t: float):
    return (1-t)*v0 + t*v1


def get_heights(amplitute: int):
    random_values = []

    for h in range(max(GWIDTH, 4) // 2):
        random_values.append(random.randint(0, max_height))
    final_heights = []  # to be returned

    for h in range(len(random_values) - 1):
        final_heights.append(random_values[h])
        for l in range(4):
            interpolated = int(
                lerp(
                    random_values[h], random_values[h +
                                                    1], ((l+1) * amplitute) / 10
                )
            )
            final_heights.append(interpolated)
            # print(round(interpolated), ((l+1) * amplitute) / 10)
    print(random_values)
    print(final_heights)
    return final_heights


heights = get_heights(amplitude)


def draw_terrain():
    for x in range(GWIDTH):
        for h in range(heights[x]):
            pygame.draw.rect(
                screen,
                colors[random.randint(0, len(colors) - 1)],
                (x * TILESIZE,
                 HEIGHT - h * TILESIZE,
                 TILESIZE - 1,
                 TILESIZE - 1)
            )


clock = pygame.time.Clock()
while True:

    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    screen.fill((0, 0, 0))
    draw_terrain()

    pygame.display.update()
