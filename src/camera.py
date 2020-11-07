from pygame.math import Vector2
from src.constants import *


class Camera:
    def __init__(self, width, height, activate_borders):
        self.velocity = Vector2(0, 0)
        self.position = Vector2(0, 0)
        self.width = width
        self.height = height
        self.activate_borders = activate_borders

        self.camera = pg.Rect(self.position.x, self.position.y, self.width, self.height)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.position=})"

    def apply(self, entity):
        if isinstance(entity, Vector2):
            return entity - self.position
        else:
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
        self.position.x = min(0.0, self.position.x)  # left
        self.position.y = min(0.0, self.position.y)  # top
        self.position.x = max(-(self.width - SCREEN_WIDTH), self.position.x)  # right
        self.position.y = max(-(self.height - SCREEN_HEIGHT), self.position.y)  # bottom

    def update(self):
        self.position += self.velocity

        if self.activate_borders is True:
            self._scrolling_limit()

        self.camera = pg.Rect(self.position.x, self.position.y, self.width, self.height)
