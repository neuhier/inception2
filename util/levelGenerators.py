# Contains functions to generate a random level, objects, etc.
import random

from gameObjects.item import Item
from gameObjects.level import Level
from gameObjects.player import Player
from gameObjects.villian import Villian
from itemGenerators import generateTree, generateSpeedBoostPanel


# ----------------------------------------------+
# Goal-Object: Reach the goal to win.
# ----------------------------------------------+


def goal_touched(game):
    # TODO: Present Statistics, high scores, allow user to enter name,...
    game.state = "mainMenu"


def generateGoal(lvl, pos):
    thisGoal = Item("teleporter", lvl, pos, [64, 64], goal_touched, False)
    return thisGoal

# --------------------------------------------------------------------------------------------------------------+
# Generate a random map - JUST FOR TESTING
# --------------------------------------------------------------------------------------------------------------+
def initRandomLevel(theme, width, height):
    lvl = Level(theme, width, height)  # New empty level
    lvl.load_textures(True)  # Load textures
    # -------------------------+
    # Add player
    # -------------------------+
    player = Player("Imadummy", lvl)  # Add a dummy player
    player.position = [1, 1]
    lvl.player = player
    lvl.render_chars.add(player)
    # -------------------------+
    # Add some zombies
    # -------------------------+
    for i in range(0, 5):
        lvl.chars.add(Villian("zombie", lvl, [random.randint(1, width - 1), random.randint(1, height - 1)]))

    # -------------------------+
    # Generate Texture grid
    # -------------------------+
    n_tex = len(lvl.all_textures)  # How many different textures are there
    for i in range(width - 1):
        for j in range(height - 1):
            lvl.texture_grid[i, j] = random.randint(0, n_tex - 1)
    # -------------------------+
    # Add items
    # -------------------------+
    nitems = width * height / 150
    for i in range(0, nitems):
        lvl.items.add(generateTree(lvl, 36, 48))

    # Boosts
    lvl.items.add(generateSpeedBoostPanel(lvl))

    # Goal
    lvl.items.add(generateGoal(lvl, [width - 10, height - 10]))
    return lvl
