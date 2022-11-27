###############################################################################
# File Name  : mario.py
# Date       : 11/25/2022
# Description: Mario data
###############################################################################

import pygame
import data.constants as const
import states.spriteSheet as ss


class Mario(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite_sheet = pygame.image.load(const.MARIO_SPRITE_SHEET_LOC).convert_alpha()
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

        # Get images for right side small mario
        self.right_small_reg_frames.append(sprite_tool.extract_image(80, 32, 16, 16))
        self.right_small_reg_frames.append(sprite_tool.extract_image(80+16, 32, 16, 16))
        self.right_small_reg_frames.append(sprite_tool.extract_image(80+16+16, 32, 16, 16))

        # Create images for left side mall mario
        for frame in self.right_small_reg_frames:
            new_image = pygame.transform.flip(frame, True, False)
            self.left_small_reg_frames.append(new_image)

        self.reg_small_frames = [self.right_small_reg_frames, self.left_small_reg_frames]


    def process(self):
        # update animation
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.last_update
        if delta_time >= const.ANIMATION_COOLDOWN:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.right_small_reg_frames):
                self.frame = 0
