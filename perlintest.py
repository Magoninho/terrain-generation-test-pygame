from __future__ import annotations

import pygame
import time
import random
import math

from typing import Tuple
from dataclasses import dataclass

@dataclass
class Vec2:
    x: float
    y: float

    def __truediv__(self, rhs):
        if isinstance(rhs, Vec2):
            return Vec2(
                self.x / rhs.x,
                self.y / rhs.y,
            )
        elif isinstance(rhs, (int, float)):
            return Vec2(
                self.x / rhs,
                self.y / rhs,
            )
        else:
            raise ValueError(f"Don't know how to divide Vec2({type(self.x)}, {type(self.y)}) by {type(rhs)}")

    def __add__(self, rhs):
        if isinstance(rhs, Vec2):
            return Vec2(
                self.x + rhs.x,
                self.y + rhs.y,
            )
        elif isinstance(rhs, (int, float)):
            return Vec2(
                self.x + rhs,
                self.y + rhs,
            )
        else:
            raise ValueError(f"Don't know how to add Vec2({type(self.x)}, {type(self.y)}) with {type(rhs)}")

    def copy(self) -> Vec2:
        try:
            new_x = self.x.copy()
        except AttributeError:
            new_x = self.x

        try:
            new_y = self.y.copy()
        except AttributeError:
            new_y = self.y

        return Vec2(
            new_x,
            new_y,
        )

    def to_tup(self):
        return (self.x, self.y)

SCREEN_SIZE = Vec2(800, 600)
SCREEN_CENTER = SCREEN_SIZE / 2
FRAMERATE = 60

# colors
WHITE = (255, 255, 255)

# display
screen = pygame.display.set_mode(SCREEN_SIZE.to_tup())

def draw_rect_at(
    screen,
    color: Tuple[int, int, int],
    position: Vec2,
    size: Vec2,
    centered: bool = False,
):
    position = position.copy()

    if centered:
        position.x -= (size.x / 2)
        position.y -= (size.y / 2)

    pygame.draw.rect(
        screen,
        color,
        pygame.Rect(
            position.to_tup(),
            size.to_tup(),
        ),
    )

@dataclass
class Box:
    speed: Vec2
    position: Vec2
    age: int = 0

    def is_out_of_screen(self, screen_size: Vec2) -> bool:
        p = self.position

        return (
            p.x < 0 or
            screen_size.x < p.x or
            p.y < 0 or
            screen_size.y < p.y
        )

gangle = 0
boxes = []

running = True
while running:
    frame_start = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))

    draw_rect_at(
        screen,
        color=(80, 70, 170),
        position=SCREEN_CENTER,
        size=Vec2(35, 35),
        centered=True,
    )

    if True:
        SPD = 10
        GAP = 50
        AMOUNT = 32 # use isso aqui pra aumentar a qualidade do círculo

        for i in range(AMOUNT):
            boxes.append(Box(
                position=Vec2(
                    x=(SCREEN_CENTER.x + GAP * math.cos(gangle + math.radians(i * 360 / AMOUNT))),
                    y=(SCREEN_CENTER.y + GAP * -math.sin(gangle + math.radians(i * 360 / AMOUNT))),
                ),
                speed=Vec2(
                    x=(SPD * math.cos(gangle)),
                    y=(SPD * -math.sin(gangle)),
                ),
            ))

    # LIMIT = 400
    # if len(boxes) > LIMIT:
    #     del boxes[:len(boxes) - LIMIT]

    i = 0
    while i < len(boxes):
        box = boxes[i]

        box.position += box.speed
        box.speed.y += 0.1

        AGE_ADD = 4
        box.age += AGE_ADD

        if (box.position.y > SCREEN_SIZE.y and box.speed.y > 0) or (box.position.y < 0 and box.speed.y < 0):
            box.speed.y *= -1

        if (box.position.x > SCREEN_SIZE.x and box.speed.x > 0) or (box.position.x < 0 and box.speed.x < 0):
            box.speed.x *= -1

        MAX_AGE = 255 # aumente isso para os rectangulos demorarem mais de spawnar

        if box.age > MAX_AGE:
            del boxes[i]
            continue

        color_mode = "Basic" # pode trocar entre "Mad" e "Basic". "Basic" funciona melhor com MAX_AGE=255, "Mad" com MAX_AGE=255*3

        if color_mode == "Mad":
            agg = box.age

            a1 = min(agg, 255)
            agg -= a1

            a2 = min(agg, 255)
            agg -= a2

            a3 = min(agg, 255)
            agg -= a3

            color = (
                255 - a1,
                255 - a2,
                255 - a3,
            )
        elif color_mode == "Basic":
            color = (max(MAX_AGE - box.age, 0),) * 3
        else:
            assert False

        draw_rect_at(
            screen,
            color=color,
            position=box.position,
            size=Vec2(20, 20),
            centered=True,
        )

        i += 1

    pygame.display.update()

    elapsed = time.time() - frame_start
    if elapsed < (1.0 / FRAMERATE):
        time.sleep(1.0 / FRAMERATE - elapsed)

    gangle += (1 / 50.0) # aumente esse valor à direita pra deixar a rotação mais lenta

pygame.quit()