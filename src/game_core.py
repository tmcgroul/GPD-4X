from pygame.math import Vector2

from src.camera import Camera
from src.game_objects.abstract.tile import Tile
from src.game_objects.movable_tile import MovableTile
from src.game_objects.selection_box import SelectionBox
from src.game_objects.static_tile import StaticTile
from src.graphics import SpriteSheet
from src.main_loop import MainLoop
from src.map import Map
from src.constants import *
from src.path import *


class GameCore(MainLoop):
    def __init__(self):
        super().__init__(CAPTION, SCREEN_SIZE, FPS)

        self.image_manager = SpriteSheet()
        self.selection_box = pg.sprite.GroupSingle()

        self.nature_tiles = pg.sprite.Group()
        self.player1_villages = pg.sprite.Group()
        self.player1_units = pg.sprite.Group()

        self.search_order = [
            self.nature_tiles,
            self.player1_villages,
            self.player1_units,
        ]

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
        for x in range(0, width, TILE_SIZE):
            pg.draw.line(self.main_surface, "darkgrey", (x, 0), (x, height))
        for y in range(0, height, TILE_SIZE):
            pg.draw.line(self.main_surface, "darkgrey", (0, y), (width, y))

    def _create_test_map(self):
        self.map = Map(TEST_MAP)
        for row, tiles in enumerate(self.map.get_data):
            for column, tile in enumerate(tiles):
                if tile == "1":
                    t = StaticTile(Vector2(column, row), self.image_manager.get_image("grass"))
                    self.nature_tiles.add(t)
                    self.visible_sprites.add(t, layer=0)
                if tile == "0":
                    t = StaticTile(Vector2(column, row), self.image_manager.get_image("water"))
                    self.nature_tiles.add(t)
                    self.visible_sprites.add(t, layer=0)
                if tile == "8":
                    t = StaticTile(Vector2(column, row), self.image_manager.get_image("grass"))
                    self.nature_tiles.add(t)
                    self.visible_sprites.add(t, layer=0)

                    t = MovableTile(Vector2(column, row), self.image_manager.get_image("farmer"))
                    self.player1_units.add(t)
                    self.visible_sprites.add(t, layer=2)
                if tile == "9":
                    # TODO: Remove double sprite on one coordinate
                    t = StaticTile(Vector2(column, row), self.image_manager.get_image("grass"))
                    self.nature_tiles.add(t)
                    self.visible_sprites.add(t, layer=0)

                    t = Tile(Vector2(column, row), self.image_manager.get_image("village"))
                    self.player1_villages.add(t)
                    self.visible_sprites.add(t, layer=1)

    def handle_mouse_event(self, type_, pos, button=0):
        pos = self.camera.apply(pos)

        if type_ == pg.MOUSEMOTION:
            pass
        elif type_ == pg.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos, button)
        elif type_ == pg.MOUSEBUTTONUP:
            pass

    def left_click(self, clicked_sprite):
        # select
        if self.selection_box.sprite is None:
            sb = SelectionBox(clicked_sprite)
            self.selection_box.add(sb)
            self.visible_sprites.add(sb)

        # unselect
        elif self.selection_box.sprite.target is clicked_sprite:
            self.selection_box.sprite.kill()

    def right_click(self, clicked_sprite):
        if self.selection_box.sprite is not None:
            if isinstance(self.selection_box.sprite.target, MovableTile):
                self.selection_box.sprite.target.move_to(clicked_sprite)

    def handle_mouse_down(self, mouse_pos, mouse_button):
        clicked_sprite = None

        for group in self.search_order:
            for sprite in group:
                if sprite.check_click(mouse_pos) is True:
                    clicked_sprite = sprite
                    break

        if clicked_sprite is not None:
            if mouse_button == 1:
                self.left_click(clicked_sprite)
            if mouse_button == 3:
                self.right_click(clicked_sprite)

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
