import pygame as pg


class DummySprite(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((0, 0))
        self.rect = self.image.get_rect()
