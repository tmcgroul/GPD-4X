from src.constants import *


class Tile(pg.sprite.Sprite):
    def __init__(self, coordinate, image):
        super().__init__()
        self.coordinate = coordinate
        self.position = self.get_position()

        self.image = image
        self._origin_image = image.copy()
        self.rect = self.image.get_rect(topleft=self.position)

        self.selected = False

    def get_coordinate(self):
        return self.coordinate

    def get_position(self):
        """Transforms tile coordinates in the grid into absolute position"""
        return self.coordinate * TILE_SIZE

    def switch_selection(self):
        if self.selected is False:
            self._draw_selection_box()
        else:
            self._remove_selection_box()
        self.selected = not self.selected

    def _remove_selection_box(self):
        self.image = self._origin_image

    def _draw_selection_box(self):
        w, h = self.rect.size
        d = SELECTION_BOX_WIDTH
        pts = [(d, d), (w - d, d), (w - d, h - d), (d, h - d)]
        box = pg.Surface(self.rect.size, pg.SRCALPHA)
        pg.draw.lines(box, SELECTION_BOX_COLOR, True, pts, d)

        self.image.blit(box, (0, 0))

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
