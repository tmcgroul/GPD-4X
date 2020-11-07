from src.constants import *


class SelectionBox(pg.sprite.Sprite):
    def __init__(self, target):
        super().__init__()
        self.color = SELECTION_BOX_COLOR
        self._target = target

        self.image = pg.Surface(self._target.rect.size, pg.SRCALPHA)
        w, h = self._target.rect.size
        d = SELECTION_BOX_WIDTH
        pts = [(d, d), (w - d, d), (w - d, h - d), (d, h - d)]
        pg.draw.lines(self.image, self.color, True, pts, d)
        self.rect = self.image.get_rect(center=self._target.rect.center)

    @property
    def target(self):
        return self._target

    def update(self, *args):
        if self._target.groups():
            self.rect.center = self._target.rect.center
        # if target was killed
        else:
            self.kill()
