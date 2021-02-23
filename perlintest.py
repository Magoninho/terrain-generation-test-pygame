"""
This is for testing a noise library, but this library doesn't have a seed system, so it's useless for a random terrain generator
There is a pull request on the library's repository that adds this functionality (https://github.com/caseman/noise/pull/22)
But I'm not going to deal with that since I'm lazy lol
"""
import pygame
import random
import noise

# colors
WHITE = (255, 255, 255)
# display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


x = 0
y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    x += 0.1

    y = noise.pnoise1(x * 0.01, repeat=99)

    pygame.draw.rect(screen, WHITE, (x, HEIGHT - int(y * 100.0) - 10, 10, 10))

    pygame.display.update()
