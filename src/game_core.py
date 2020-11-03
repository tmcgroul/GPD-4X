import pygame as pg

from src.game_objects.tile import Tile
from src.main_loop import MainLoop
import src.constants as c


class GameCore(MainLoop):
    def __init__(self):
        super().__init__(c.CAPTION, c.SCREEN_SIZE, c.FPS)

        self._draw_grid()
        self._create_test_map()
        self.mouse_handlers.append(self.handle_mouse_event)

    def _draw_grid(self):
        width, height = self.main_surface.get_size()
        for x in range(0, width, c.TILE_WIDTH):
            pg.draw.line(self.main_surface, "lightgrey", (x, 0), (x, height))
        for y in range(0, height, c.TILE_HEIGHT):
            pg.draw.line(self.main_surface, "lightgrey", (0, y), (width, y))

    def _create_test_map(self):
        for i in range(5):
            for j in range(5):
                t = Tile((3 + i, 3 + j), c.TILE_SIZE, "green")
                self.visible_sprites.add(t)

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


if __name__ == '__main__':
    GameCore().run()
