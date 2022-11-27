###############################################################################
# File Name  : spriteSheet.py
# Date       : 11/12/2022
# Description: Sprite Sheet Class
###############################################################################

import pygame
import data.constants as const


class SpriteSheet:
    def __init__(self, image):
        self.sheet = image
        print()

    def extract_image(self, x_pos, y_pos, width, height):
        image = pygame.Surface([width, height])
        rect = image.get_rect()
        image.blit(self.sheet, (0, 0), (x_pos, y_pos, width, height))
        image.set_colorkey((0, 0, 50))
        image = pygame.transform.scale(image, (int(rect.width * const.SIZE_MULTIPLIER), int(rect.height * const.SIZE_MULTIPLIER)))
        return image

    def get_image(self, frame, x_pos, y_pos, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((x_pos + (frame * width)), y_pos, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
