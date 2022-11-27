###############################################################################
# File Name  : game_objects.py
# Date       : 11/27/2022
# Description: Base classes for mario and other game objects
###############################################################################

import pygame
import data.constants as const


class GameObject(pygame.sprite.Sprite):
    def __init__(self, images=None, height=None, speed=None):
        super().__init__()
        self.speed = speed
        self.images = images
        self.pos = images.get_rect().move(0, height)

    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0
