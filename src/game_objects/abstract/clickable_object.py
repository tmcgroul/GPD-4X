from src.game_objects.abstract.empty_sprite import DummySprite


class ClickableSprite(DummySprite):
    def __init__(self):
        super().__init__()

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
