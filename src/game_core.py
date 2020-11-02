from src.main_loop import MainLoop
import src.constants as c


class GameCore(MainLoop):
    def __init__(self):
        super().__init__(c.CAPTION, c.SCREEN_SIZE, c.FPS)


if __name__ == '__main__':
    GameCore().run()
