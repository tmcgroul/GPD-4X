import pygame as pg

from src.camera import Camera
from src.game_objects.tile import Tile
from src.graphics import SpriteSheet
from src.main_loop import MainLoop
from src.map import Map
from src.constants import *
from src.path import *


class GameCore(MainLoop):
    def __init__(self):
        super().__init__(CAPTION, SCREEN_SIZE, FPS)

        self.image_manager = SpriteSheet()
        self.create_objects()
        self.mouse_handlers.append(self.handle_mouse_event)

    def create_objects(self):
        self._create_test_map()
        self._create_camera()

    def _create_camera(self):
        self.camera = Camera(self.map.width, self.map.height, ACTIVATE_SCROLLING_BORDERS)
        for key in CAMERA_SHORTCUTS.values():
            self.add_up_down_key_handlers(self.camera, key)

    def _draw_grid(self):
        width, height = self.main_surface.get_size()
        for x in range(0, width, TILE_WIDTH):
            pg.draw.line(self.main_surface, "darkgrey", (x, 0), (x, height))
        for y in range(0, height, TILE_HEIGHT):
            pg.draw.line(self.main_surface, "darkgrey", (0, y), (width, y))

    def _create_test_map(self):
        self.map = Map(TEST_MAP)
        for row, tiles in enumerate(self.map.get_data):
            for column, tile in enumerate(tiles):
                if tile == "1":
                    self.visible_sprites.add(Tile((column, row), self.image_manager.get_image("grass")), layer=0)
                if tile == "0":
                    self.visible_sprites.add(Tile((column, row), self.image_manager.get_image("water")), layer=0)
                if tile == "9":
                    self.visible_sprites.add(Tile((column, row), self.image_manager.get_image("grass")), layer=0)
                    self.visible_sprites.add(Tile((column, row), self.image_manager.get_image("village")), layer=1)

    def handle_mouse_event(self, type_, pos):
        if type_ == pg.MOUSEMOTION:
            pass
        elif type_ == pg.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type_ == pg.MOUSEBUTTONUP:
            pass

    def handle_mouse_down(self, mouse_pos):
        for sprite in self.visible_sprites:
            if sprite.check_click(mouse_pos) is True:
                print(sprite.rect.topleft)

    def draw(self):
        for sprite in self.visible_sprites:
            self.main_surface.blit(sprite.image, self.camera.apply(sprite))

        if ACTIVATE_TEST_GRID is True:
            self._draw_grid()

    def update(self):
        self.main_surface.fill(BG_COLOR)
        super().update()
        self.camera.update()


if __name__ == '__main__':
    GameCore().run()
