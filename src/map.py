from src.constants import *


class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, "r") as f:
            for line in f:
                self.data.append(line.strip())

        self.width = len(self.data[0]) * TILE_SIZE
        self.height = len(self.data) * TILE_SIZE

    @property
    def get_data(self):
        return self.data
