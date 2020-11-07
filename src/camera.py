from pygame.math import Vector2
from src.constants import *


class Camera:

    movement_keys = [
        CAMERA_SHORTCUTS["Move up"],
        CAMERA_SHORTCUTS["Move down"],
        CAMERA_SHORTCUTS["Move left"],
        CAMERA_SHORTCUTS["Move right"],
    ]

    def __init__(self, width, height, activate_borders):
        self.velocity = Vector2(0, 0)
        self.position = Vector2(0, 0)
        self.width = width
        self.height = height
        self.activate_borders = activate_borders

        self.camera = pg.Rect(self.position.x, self.position.y, self.width, self.height)
        self.pressed_keys = []

    def __repr__(self):
        return f"{self.__class__.__name__}({self.position=})"

    def apply(self, entity):
        if isinstance(entity, Vector2):
            return entity - self.position
        else:
            return entity.rect.move(self.camera.topleft)

    def handle_key_down(self, key):
        if key in self.movement_keys:
            self._move_camera(key)
            self.pressed_keys.append(key)

        if key == CAMERA_SHORTCUTS["Activate/deactivate borders"]:
            self.activate_borders = not self.activate_borders

    def handle_key_up(self, key):
        if key in self.movement_keys:
            self.pressed_keys.remove(key)

        if self.pressed_keys:
            previous_key = self.pressed_keys[-1]
            self._move_camera(previous_key)
        else:
            self._stop_camera()

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

    def _move_camera(self, key):
        """Move camera depends on passed key."""
        if key == CAMERA_SHORTCUTS["Move up"]:
            self.velocity.y = CAMERA_SPEED
        if key == CAMERA_SHORTCUTS["Move down"]:
            self.velocity.y = -CAMERA_SPEED

        if key == CAMERA_SHORTCUTS["Move left"]:
            self.velocity.x = CAMERA_SPEED
        if key == CAMERA_SHORTCUTS["Move right"]:
            self.velocity.x = -CAMERA_SPEED

    def _stop_camera(self):
        """Prevent camera moving."""
        self.velocity.x = 0
        self.velocity.y = 0
