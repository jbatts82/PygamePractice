###############################################################################
# File Name  : main.py
# Date       : 11/25/2022
# Description: Main Loop
###############################################################################

print("Hello, Main Loop")

import pygame
import tools.spriteSheet
import data.constants as const

# create screen
screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption('Sprite Lab')

# get sprite sheet
sprite_sheet_loc = 'resources/graphics/mario_bros.png'
sprite_sheet_image = pygame.image.load(sprite_sheet_loc).convert_alpha()

# set up clock
clock = pygame.time.Clock()

run = True
while run:
    screen.fill(const.BG)


    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
