from pygame.math import Vector2
from src.constants import *


class Camera:
    def __init__(self, width, height, activate_borders):
        self.velocity = Vector2(0, 0)
        self.pos = Vector2(0, 0)
        self.width = width
        self.height = height
        self.activate_borders = activate_borders

        self.camera = pg.Rect(self.pos.x, self.pos.y, self.width, self.height)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def handle_key_down(self, key):
        if key == CAMERA_SHORTCUTS["Move up"]:
            self.velocity.y = CAMERA_SPEED
        if key == CAMERA_SHORTCUTS["Move down"]:
            self.velocity.y = -CAMERA_SPEED

        if key == CAMERA_SHORTCUTS["Move left"]:
            self.velocity.x = CAMERA_SPEED
        if key == CAMERA_SHORTCUTS["Move right"]:
            self.velocity.x = -CAMERA_SPEED

        if key == CAMERA_SHORTCUTS["Activate/deactivate borders"]:
            self.activate_borders = not self.activate_borders

    def handle_key_up(self, key):
        if key == CAMERA_SHORTCUTS["Move up"]:
            self.velocity.y = 0
        if key == CAMERA_SHORTCUTS["Move down"]:
            self.velocity.y = 0

        if key == CAMERA_SHORTCUTS["Move left"]:
            self.velocity.x = 0
        if key == CAMERA_SHORTCUTS["Move right"]:
            self.velocity.x = 0

    def _scrolling_limit(self):
        """Limit scrolling to map size"""
        self.pos.x = min(0.0, self.pos.x)  # left
        self.pos.y = min(0.0, self.pos.y)  # top
        self.pos.x = max(-(self.width - SCREEN_WIDTH), self.pos.x)  # right
        self.pos.y = max(-(self.height - SCREEN_HEIGHT), self.pos.y)  # bottom

    def update(self):
        self.pos += self.velocity

        if self.activate_borders is True:
            self._scrolling_limit()

        self.camera = pg.Rect(self.pos.x, self.pos.y, self.width, self.height)
