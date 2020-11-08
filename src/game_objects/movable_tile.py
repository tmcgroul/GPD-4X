from src.game_objects.abstract.tile import Tile


class MovableTile(Tile):
    def __init__(self, coordinate, image):
        super().__init__(coordinate, image)

    def move_to(self, target):
        self.rect.topleft = target.rect.topleft
