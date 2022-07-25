import pygame

COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, tilesize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)

        self.rect = self.image.get_rect()	
