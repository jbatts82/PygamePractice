###############################################################################
# File Name  : mario.py
# Date       : 11/25/2022
# Description: Mario data
###############################################################################

import pygame
import data.constants as const
import tools.spriteSheet as ss


class Mario(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        self.sprite_sheet = sprite_sheet
        # extract mario animations
        self.mario_animations = []
        self.mario_steps = [3]
        self.mario_action = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.load_images_from_sheet()

    def load_images_from_sheet(self):
        self.right_frames = []
        self.left_frames = []
        self.right_small_reg_frames = []
        self.right_big_reg_frames = []
        self.left_small_reg_frames = []
        self.left_big_reg_frames = []

        sprite_tool = ss.SpriteSheet(self.sprite_sheet)

        self.right_small_reg_frames.append(sprite_tool.extract_image(80, 32, 16, 16))
        self.right_small_reg_frames.append(sprite_tool.extract_image(80+16, 32, 16, 16))
        self.right_small_reg_frames.append(sprite_tool.extract_image(80+16+16, 32, 16, 16))


    def process(self):
        # update animation

        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.last_update

        if delta_time >= const.ANIMATION_COOLDOWN:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.right_small_reg_frames):
                self.frame = 0
