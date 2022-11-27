###############################################################################
# File Name  : main.py
# Date       : 11/25/2022
# Description: Main Loop
###############################################################################

import sys
import pygame
import states.tools

# init pygame library and game controller
pygame.init()
controller = states.tools.Control()

# game loop
controller.main_loop()

# if game loop broke
pygame.quit()
sys.exit()
