# Contains functions to generate a random level, objects, etc.
import random

from gameObjects.level import Level
from gameObjects.villian import Villian
from itemGenerators import generateTree, generateSpeedBoostPanel, generateGoal


# --------------------------------------------------------------------------------------------------------------+
# Generate a random map - JUST FOR TESTING
# --------------------------------------------------------------------------------------------------------------+
def initRandomLevel(theme, width, height, game):
    game.level = Level(theme, width, height)  # New empty level

    # -------------------------+
    # Add some zombies
    # -------------------------+
    for i in range(0, 5):
        game.level.chars.add(
            Villian("zombie", game.imgMngr, [random.randint(1, width - 1), random.randint(1, height - 1)]))

    # -------------------------+
    # Generate Texture grid
    # -------------------------+
    n_tex = len(game.imgMngr.all_textures)  # How many different textures are there
    for i in range(width - 1):
        for j in range(height - 1):
            game.level.texture_grid[i, j] = random.randint(0, n_tex - 1)
    # -------------------------+
    # Add items
    # -------------------------+
    nitems = width * height / 150
    for i in range(0, nitems):
        game.level.items.add(generateTree(game))

    # Boosts
    game.level.items.add(generateSpeedBoostPanel(game))

    # Goal
    game.level.items.add(generateGoal(game, [width - 10, height - 10]))
