import pygame as pg

from src.settings.constants import TILE_SIZE


class Tile(pg.sprite.Sprite):
    def __init__(self, coordinate, image):
        super().__init__()
        self.coordinate = coordinate
        self.position = self.get_position()

        self.image = image
        self.rect = self.image.get_rect(topleft=self.position)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.position=}, {self.coordinate=}, {self.image.get_size()=})"

    def get_coordinate(self):
        return self.coordinate

    def get_position(self):
        """Transforms tile coordinates in the grid into absolute position"""
        return self.coordinate * TILE_SIZE

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
