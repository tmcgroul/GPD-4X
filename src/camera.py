from src.constants import *


class Camera:
    def __init__(self, width, height, activate_borders):
        self.x = self.y = 0
        self.xv = self.yv = 0
        self.width = width
        self.height = height
        self.activate_borders = activate_borders

        self.camera = pg.Rect(self.x, self.y, self.width, self.height)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def handle_key_down(self, key):
        if key == CAMERA_SHORTCUTS["Move up"]:
            self.yv = CAMERA_SPEED
        if key == CAMERA_SHORTCUTS["Move down"]:
            self.yv = -CAMERA_SPEED

        if key == CAMERA_SHORTCUTS["Move left"]:
            self.xv = CAMERA_SPEED
        if key == CAMERA_SHORTCUTS["Move right"]:
            self.xv = -CAMERA_SPEED

        if key == CAMERA_SHORTCUTS["Activate/deactivate borders"]:
            self.activate_borders = not self.activate_borders

    def handle_key_up(self, key):
        if key == CAMERA_SHORTCUTS["Move up"]:
            self.yv = 0
        if key == CAMERA_SHORTCUTS["Move down"]:
            self.yv = 0

        if key == CAMERA_SHORTCUTS["Move left"]:
            self.xv = 0
        if key == CAMERA_SHORTCUTS["Move right"]:
            self.xv = 0

    def _scrolling_limit(self):
        """Limit scrolling to map size"""
        self.x = min(0, self.x)  # left
        self.y = min(0, self.y)  # top
        self.x = max(-(self.width - SCREEN_WIDTH), self.x)  # right
        self.y = max(-(self.height - SCREEN_HEIGHT), self.y)  # bottom

    def update(self):
        self.x += self.xv
        self.y += self.yv

        if self.activate_borders is True:
            self._scrolling_limit()

        self.camera = pg.Rect(self.x, self.y, self.width, self.height)
