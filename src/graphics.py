from random import choice
import pygame as pg
from src.constants import *
from src import path


class SpriteSheet:
    """Image manager. Load sprite images from a sprite sheets"""
    def __init__(self):
        self.source_image = pg.image.load(path.TILE_SHEET).convert_alpha()
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

        if name == "grass":
            grass_cords = [(0, 0), (0, 1), (0, 2), (0, 3)]
            xi, yi = choice(grass_cords)
            x, y, width, height = self.sprites[xi][yi]
        if name == "water":
            water_cords = [(24, 0), (24, 1), (24, 2), (24, 3)]
            xi, yi = choice(water_cords)
            x, y, width, height = self.sprites[xi][yi]

        if None in (x, y, width, height):
            # if sprite didn't found
            x, y, width, height = self.sprites[45][4]

        return x, y, width, height
