import pygame as pg

# general
CAPTION = "GPD-4X"
FPS = 60
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 0, 0
BGCOLOR = "black"

# Tile
TILE_SIZE = TILE_WIDTH, TILE_HEIGHT = 16, 16

# Camera
CAMERA_SPEED = 300

# Shortcuts
CAMERA_SHORTCUTS = {
    "Move up": pg.K_w,
    "Move down": pg.K_s,
    "Move left": pg.K_a,
    "Move right": pg.K_d,
}
