from random import choice
import pygame as pg
from src.constants import *
from src import path


class SpriteSheet:
    """Image manager. Load sprite images from a sprite sheets"""
    def __init__(self):
        self.source_image = pg.image.load(path.TILE_SHEET).convert_alpha()
        self.source_image.set_colorkey("white")
        self.width, self.height = self.source_image.get_size()

        self.sprites = {row: [(col * TILE_WIDTH, row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT) for col in
                              range(self.width // TILE_WIDTH)] for row in range(self.height // TILE_HEIGHT)}

    def get_image(self, name):
        x, y, width, height = self._name_to_coordinate(name)
        source_area = pg.Rect(x, y, width, height)
        sprite = pg.Surface((width, height), pg.SRCALPHA)
        sprite.blit(self.source_image, (0, 0), source_area)
        return sprite

    def _name_to_coordinate(self, name):
        x = y = width = height = None

        # TODO: Add json file with: name: coordinates
        images = {
            "grass": [(0, i) for i in range(4)],
            "water": [(24, i) for i in range(4)],
            "village": [*[(1, i) for i in range(3)], *[(2, i) for i in range(4)], (3, 0)],
        }

        for image_name, coordinates in images.items():
            if name == image_name:
                row, column = choice(coordinates)
                x, y, width, height = self.sprites[row][column]

        if None in (x, y, width, height):
            # if sprite didn't found
            x, y, width, height = self.sprites[45][4]

        return x, y, width, height
