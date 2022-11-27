###############################################################################
# File Name  : constants.py
# Date       : 11/25/2022
# Description: Mario constant data
###############################################################################

# screen constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

MAIN_CAPTION = 'Mario Lab'

# system constants
FPS = 60
SIZE_MULTIPLIER = 8
ANIMATION_COOLDOWN = 150

# images
MARIO_SPRITE_SHEET_LOC = 'resources/graphics/mario_bros.png'
BACKGROUND_PNG_LOC = 'resources/graphics/simple_bg.png'

# colors
# (R,G,B)
GRAY = (100, 100, 100)
NAVY_BLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FOREST_GREEN = (31, 162, 35)
BLUE = (0, 0, 255)
SKY_BLUE = (39, 145, 251)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
NEAR_BLACK = (19, 15, 48)
COM_BLUE = (233, 232, 255)
GOLD = (255, 215, 0)

# mario constants
MARIO_SPEED = 2

# mario states
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
SMALL_TO_BIG = 'small to big'
BIG_TO_SMALL = 'big to small'

# mario Forces
WALK_ACCEL = .15
RUN_ACCEL = 20

# general forces
GRAVITY = 1.01
