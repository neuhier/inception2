# Contains functions to generate a random level, objects, etc.
import random

from gameObjects.item import Item
from gameObjects.level import Level
from gameObjects.player import Player
from gameObjects.villian import Villian
from gameObjects.weapon import Weapon


# ----------------------------------------------+
# Function to generate a tree on the level
# ----------------------------------------------+


def tree_touched(game):
    game.level.player.bounce_back()


def generateTree(lvl, w, h):
    # Generate a name for the object ==> defines skin
    treeSkins = {}
    for key, value in lvl.all_images.items():
        if 'tree' in str(key):
            treeSkins[key] = value
    type = treeSkins.keys()[random.randint(0, len(treeSkins.keys()) - 1)]

    # Random position in the level
    x = random.randint(0, len(lvl.texture_grid) - 1)
    y = random.randint(0, len(lvl.texture_grid[0]) - 1)

    # No rescaling of images
    # w           = treeSkins[type].get_rect().size[0]
    # h           = treeSkins[type].get_rect().size[1]

    thistree = Item(type, lvl, [x, y], [w, h], tree_touched, False)

    return thistree


# ----------------------------------------------+
# Goal-Object: Reach the goal to win.
# ----------------------------------------------+
def goal_touched(game):
    # TODO: Present Statistics, high scores, allow user to enter name,...
    game.state = "mainMenu"


def generateGoal(lvl, pos):
    thisGoal = Item("teleporter", lvl, pos, [64, 64], goal_touched, False)
    return thisGoal


# ----------------------------------------------+
# Function to create the basic weapon: Gun
# ----------------------------------------------+
def generate_gun_dmg():
    dmg = random.randint(10, 30)
    return dmg


def generateGun():
    wpn = Weapon("gun", 5, 0.3, generate_gun_dmg)
    return wpn


# --------------------------------------------------------------------------------------------------------------+
# Generate a random map - JUST FOR TESTING
# --------------------------------------------------------------------------------------------------------------+
def initRandomLevel(theme, width, height):
    lvl = Level(theme, width, height)  # New empty level
    lvl.load_textures()  # Load textures
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

    lvl.items.add(generateGoal(lvl, [width - 10, height - 10]))
    return lvl
