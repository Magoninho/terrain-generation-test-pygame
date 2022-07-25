"""

Perlin noise is a little bit hard on python
So, if you know how to implement it, send a pull request :)

"""

import pygame
import random

TILESIZE = 16
GWIDTH = 80  # Grid width
GHEIGHT = 30  # Grid height
WIDTH = GWIDTH * TILESIZE  # Window width
HEIGHT = GHEIGHT * TILESIZE  # Window height

bgs = ["terraria.png", "terraria2.png", "terraria3.png"]


bg = pygame.image.load(bgs[random.randint(0, len(bgs) - 1)])


#######################################
# settings #

max_height = 15
stone_max_height = max_height // 2
amplitude = 2  # its a very limited amplitude lol

#######################################


# colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
color = ()

# colors = (
#     (255, 255, 255),
#     (255, 0, 0),
#     (0, 255, 0),
#     (0, 0, 255)
# )

# display
pygame.display.set_caption("terraria lmao")
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# the lerp function used in linear interpolation
def lerp(v0, v1, t: float):
    return (1 - t) * v0 + t * v1


# using linear interpolation (lerp()) for generating the terrain
def get_heights(amplitute: int, max_height: int):
    random_values = []  # storing random values (heights) in this array
    for h in range(max(GWIDTH, 4)):  # the minimum value for GWIDTH is 4
        random_values.append(random.randint(0, max_height))

    # the heights to be returned with the random values + their interpolation values
    final_heights = []  # to be returned

    # doing a very weird interpolation between values of the array
    for h in range(len(random_values) - 1):
        final_heights.append(random_values[h])
        for l in range(4):
            interpolated = int(
                lerp(
                    random_values[h],
                    random_values[h + 1],
                    ((l + 1) * amplitute) / 10,  # TODO: fix this later because is weird
                )
            )
            final_heights.append(interpolated)
    return final_heights


def create_tree(x, y):
    log_height = 4  # measured in blocks
    offset = 0
    # creates tree log
    for _ in range(log_height):
        pygame.draw.rect(
            screen,
            (100, 0, 0),
            (x * TILESIZE, (y - offset) * TILESIZE, TILESIZE, TILESIZE),
        )
        offset += 1

    # creates the leafs
    leaf_height = 4
    leaf_width = 3
    for h in range(leaf_height):
        pygame.draw.rect(
            screen,
            (0, 100, 0),
            (x * TILESIZE, (y - offset) * TILESIZE, TILESIZE, TILESIZE),
        )
        if leaf_height - h == 1:
            leaf_width -= 1

        for w in range(leaf_width):
            pygame.draw.rect(
                screen,
                (0, 100, 0),
                ((x + w) * TILESIZE, (y - offset) * TILESIZE, TILESIZE, TILESIZE),
            )
            pygame.draw.rect(
                screen,
                (0, 100, 0),
                ((x - w) * TILESIZE, (y - offset) * TILESIZE, TILESIZE, TILESIZE),
            )

        offset += 1


heights = get_heights(amplitude, max_height)

stone_height = get_heights(3, stone_max_height)

def generate_tree_positions(probability, heights):
    tree_positions = []
    for x in range(GWIDTH):
        y = GHEIGHT - heights[x]
        if random.randint(0, 100) < probability:

            tree_positions.append([x, y])

            # create_tree(x, GHEIGHT - heights[x])
            
    return tree_positions


tree_positions = generate_tree_positions(10, heights)
print(tree_positions)
def draw_trees():
    for position in tree_positions:
        create_tree(position[0], position[1])


def draw_terrain():
    h = 0

    for x in range(GWIDTH):
        for h in range(heights[x]):
            if h < stone_height[x]:
                pygame.draw.rect(
                    screen,
                    (149, 148, 139),  # gray (stone)
                    (x * TILESIZE, HEIGHT - h * TILESIZE, TILESIZE, TILESIZE),
                )
            else:
                pygame.draw.rect(
                    screen,
                    (155, 118, 83),  # brown (dirt)
                    (x * TILESIZE, HEIGHT - h * TILESIZE, TILESIZE, TILESIZE),
                )

        pygame.draw.rect(
            screen,
            (34, 139, 34),  # green (grass)
            (x * TILESIZE, HEIGHT - h * TILESIZE, TILESIZE, TILESIZE),
        )

        # if random.randint(0, 100) < 10:
        #     create_tree(x, GHEIGHT - heights[x])
            


def restart():
    global heights, stone_height, tree_positions
    heights = get_heights(amplitude, max_height)
    stone_height = get_heights(3, stone_max_height)
    tree_positions = generate_tree_positions(10, heights)
    draw_terrain()


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
            if event.key == pygame.K_SPACE:
                restart()

    screen.blit(bg, (0, 0))
    # create_tree(16, 16)
    draw_terrain()
    draw_trees()
    pygame.display.update()
