###############################################################################
# File Name  : main.py
# Date       : 11/25/2022
# Description: Main Loop
###############################################################################

import sys
import pygame
import data.constants as const
import data.mario

# create screen
screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption('Sprite Lab')

# set up clock
clock = pygame.time.Clock()

# get mario sprite sheet
sprite_sheet_loc = 'resources/graphics/mario_bros.png'
sprite_sheet_image = pygame.image.load(sprite_sheet_loc).convert_alpha()

mario = data.mario.Mario(sprite_sheet_image)


run_game = True
while run_game:

    screen.fill(const.BG)

    mario.process()

    screen.blit(mario.right_small_reg_frames[mario.frame], (0, 0))


    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    clock.tick(const.FPS)
    pygame.display.update()

# if not run
pygame.quit()
sys.exit()
