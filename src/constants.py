import pygame as pg
# TODO: remove this import

# general
CAPTION = "GPD-4X"
FPS = 60
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1680, 1050  # 0, 0 == fullscreen
BG_COLOR = "black"
TILE_SIZE = 32
SH_TILE_SIZE = 16
ACTIVATE_TEST_GRID = False

SELECTION_BOX_COLOR = "red"
SELECTION_BOX_WIDTH = 1

# Camera
CAMERA_SPEED = 100
ACTIVATE_SCROLLING_BORDERS = True

# Shortcuts
CAMERA_SHORTCUTS = {
    "Move up": pg.K_w,
    "Move down": pg.K_s,
    "Move left": pg.K_a,
    "Move right": pg.K_d,
    "Activate/deactivate borders": pg.K_c,
}

# SHOW_GRID = pg.K_g
