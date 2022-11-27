###############################################################################
# File Name  : tools.py
# Date       : 11/27/2022
# Description: System control functions. Helper functions.
###############################################################################

import pygame
import data.constants as const
import data.mario

keybindings = {
    'action': pygame.K_s,
    'jump': pygame.K_a,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'down': pygame.K_DOWN
}


class Control:
    def __init__(self):
        # init control objects
        self.run_game = True

        # set up clock
        self.clock = pygame.time.Clock()

        # create screen with simple background
        self.screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        pygame.display.set_caption(const.MAIN_CAPTION)
        self.background_img = pygame.image.load(const.BACKGROUND_PNG_LOC).convert_alpha()
        self.background_img = pygame.transform.scale(self.background_img,
                                                     (const.SCREEN_WIDTH,
                                                      const.SCREEN_HEIGHT))

        # create game objects
        self.mario = data.mario.Mario()
        objects = [self.mario]


    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_game = False


    def main_loop(self):
        while self.run_game:
            self.process_gfx()
            self.event_handler()
            self.clock.tick(const.FPS)

    def process_gfx(self):
        self.mario.update_frame()
        self.screen.blit(self.background_img, (0, 0))
        self.screen.blit(self.mario.right_big_reg_frames[self.mario.frame_idx], (0, (1080/3)-40*4))
        pygame.display.update()
