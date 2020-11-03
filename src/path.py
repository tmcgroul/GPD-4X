from os import path

PROJECT_DIRECTORY = path.abspath("./")

REQUIREMENTS = path.join(PROJECT_DIRECTORY, "requirements.txt")

# Assets
ASSETS_DIRECTORY = path.join(PROJECT_DIRECTORY, "assets")
TILE_SHEET = path.join(ASSETS_DIRECTORY, "Tile-set - Toen's Medieval Strategy (16x16) - v.1.0.png")

# Source code
SRC_DIRECTORY = path.join(PROJECT_DIRECTORY, "src")
TEST_MAP = path.join(SRC_DIRECTORY, "test_map.txt")
