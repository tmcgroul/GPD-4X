import pygame as pg

from src.game_objects.abstract.clickable_object import ClickableSprite


class Tile(ClickableSprite):
    def __init__(self, pos, size, color):
        super().__init__()
        self.image = pg.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
