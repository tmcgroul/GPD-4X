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

        self.sprites = {row: [(col * SH_TILE_SIZE, row * SH_TILE_SIZE, SH_TILE_SIZE, SH_TILE_SIZE) for col in
                              range(self.width // SH_TILE_SIZE)] for row in range(self.height // SH_TILE_SIZE)}

    def get_image(self, name):
        x, y, width, height = self._name_to_coordinate(name)
        source_area = pg.Rect(x, y, width, height)
        sprite = pg.Surface((width, height), pg.SRCALPHA)
        sprite.blit(self.source_image, (0, 0), source_area)

        if SH_TILE_SIZE != TILE_SIZE:
            sprite = self._scale(sprite)

        return sprite

    def _scale(self, sprite):
        return pg.transform.scale(sprite, (TILE_SIZE, TILE_SIZE))

    def _name_to_coordinate(self, name):
        image_data = None

        # TODO: Add json file with: name: data
        images = {
            "grass": [(0, i) for i in range(4)],
            "water": [(24, i) for i in range(4)],
            "village": [*[(1, i) for i in range(3)], *[(2, i) for i in range(4)], (3, 0)],
        }

        for image_name, coordinates in images.items():
            if name == image_name:
                row, column = choice(coordinates)
                image_data = self.sprites[row][column]

        if image_data is None:
            # if sprite didn't found
            image_data = self.sprites[45][4]

        return image_data
