import pygame as pg

from src.game_objects.abstract.clickable_object import ClickableSprite
import src.constants as c


class Tile(ClickableSprite):
    def __init__(self, coordinate, size, color):
        super().__init__()
        self.coordinate = coordinate
        self.pos = self.GetPosition()

        self.image = pg.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=self.pos)

    def GetPosition(self):
        return self.coordinate[0] * c.TILE_WIDTH, self.coordinate[1] * c.TILE_HEIGHT

    # def update(self, *args, **kwargs):
    #     super().update()
    #     self.rect.topleft = self.pos
