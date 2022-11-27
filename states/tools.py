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

        # create screen
        self.screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        pygame.display.set_caption(const.MAIN_CAPTION)

        # create mario
        self.mario = data.mario.Mario()

    def main_loop(self):
        print("main_loop")
        while self.run_game:
            self.process()
            self.event_handler()
            pygame.display.update()
            self.clock.tick(const.FPS)


    def process(self):
        self.screen.fill(const.BG)
        self.mario.process()
        self.screen.blit(self.mario.right_small_reg_frames[self.mario.frame], (0, 0))


    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_game = False
