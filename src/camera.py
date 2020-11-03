from src.constants import *


class Camera:
    def __init__(self, width, height):
        self.x = self.y = 0
        self.xv = self.yv = 0
        self.width = width
        self.height = height
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

    def handle_key_up(self, key):
        if key == CAMERA_SHORTCUTS["Move up"]:
            self.yv = 0
        if key == CAMERA_SHORTCUTS["Move down"]:
            self.yv = 0

        if key == CAMERA_SHORTCUTS["Move left"]:
            self.xv = 0
        if key == CAMERA_SHORTCUTS["Move right"]:
            self.xv = 0

    def update(self):
        self.x += self.xv
        self.y += self.yv
        self.camera = pg.Rect(self.x, self.y, self.width, self.height)
