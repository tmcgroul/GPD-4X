from random import choice

import pygame as pg

from src.settings import paths
from src.settings.constants import TILE_SIZE, SH_TILE_SIZE


class SpriteSheet:
    """Image manager. Load sprite images from a sprite sheets"""
    def __init__(self):
        self.source_image = pg.image.load(paths.TILE_SHEET).convert_alpha()
        self.source_image.set_colorkey("white")
        self.width, self.height = self.source_image.get_size()

        TL = SH_TILE_SIZE
        self.sprites = {row: [(col * TL, row * TL, TL, TL) for col in range(self.width // TL)]
                        for row in range(self.height // TL)}

    def __repr__(self):
        return f"{self.__class__.__name__}('{paths.TILE_SHEET}', {len(self.sprites)=})"

    def get_image(self, name):
        x, y, width, height = self._name_to_coordinate(name)
        source_area = pg.Rect(x, y, width, height)
        sprite = pg.Surface((width, height), pg.SRCALPHA)
        sprite.blit(self.source_image, (0, 0), source_area)

        if SH_TILE_SIZE != TILE_SIZE:
            sprite = self._scale(sprite)

        return sprite

    @staticmethod
    def _scale(sprite):
        return pg.transform.scale(sprite, (TILE_SIZE, TILE_SIZE))

    def _name_to_coordinate(self, name):
        image_data = None

        # TODO: Add json file with: name: data
        images = {
            "grass": [(0, i) for i in range(4)],
            "water": [(24, i) for i in range(4)],
            "farmer": [(13, 6), (14, 5)],
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
