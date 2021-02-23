import pygame
import random

TILESIZE = 8
GWIDTH = 16
GHEIGHT = 16
WIDTH = GWIDTH * TILESIZE
HEIGHT = GHEIGHT * TILESIZE

# colors
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

amplitute = 2


def lerp(v0, v1, t: float):
    return v0 + t * (v1 - v0)


# for h in range(GWIDTH // 2):
#     random_values.append(random.randint(0, 8))
# random_values = [3, 6, 7, 4, 0, 3, 6, 6]
random_values = [3, 15, 7, 4]
print(random_values)


final_heights = []  # to be returned after

i = 0

for h in range(len(random_values) - 1):
    final_heights.append(random_values[h])
    for l in range(4):
        interpolated = round(
            lerp(
                random_values[h], random_values[h+1], ((l+1) * amplitute) / 10
            )
        )
        final_heights.append(interpolated)
        print(final_heights)
        # print(round(interpolated), ((l+1) * amplitute) / 10)
l = 0.0
x = 0
y = 0


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

    pygame.draw.rect(screen, WHITE, (x, y, TILESIZE, TILESIZE))

    pygame.display.update()
