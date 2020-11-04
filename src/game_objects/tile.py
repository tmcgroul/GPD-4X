import pygame as pg

from src.game_objects.abstract.clickable_object import ClickableSprite
from src.constants import *


class Tile(ClickableSprite):
    def __init__(self, coordinate, image):
        super().__init__()
        self.coordinate = coordinate
        self.pos = self.get_position()

        self.image = image
        self.rect = self.image.get_rect(topleft=self.pos)

    def get_position(self):
        return self.coordinate[0] * TILE_WIDTH, self.coordinate[1] * TILE_HEIGHT
