from src.constants import *
from src.game_objects.abstract.tile import Tile


class StaticTile(Tile):
    def __init__(self, coordinate, image):
        super().__init__(coordinate, image)
