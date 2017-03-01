# ----------------------------------------------+
# Function to generate a tree on the level
# ----------------------------------------------+
import random

from boostGenerators import generateSpeedBoost
from gameObjects.item import Item


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

    thistree = Item(type, lvl, [x, y], 2, tree_touched, False)

    return thistree


# ----------------------------------------------+
# Function to generate a speedboost-panel
# ----------------------------------------------+

def generateSpeedBoostPanel(level):
    def panelTouched(game):
        sb = generateSpeedBoost()
        game.activeBoosts.append(sb)
        game.activeMessages.append(sb.message)
        sb.startEffect(game.level)

    # Random position in the level
    x = random.randint(0, len(level.texture_grid) - 1)
    y = random.randint(0, len(level.texture_grid[0]) - 1)

    # No rescaling
    w = level.all_images["speedboost"].get_rect().size[0]
    h = level.all_images["speedboost"].get_rect().size[1]

    thisBoost = Item("speedboost", level, [x, y], 1, panelTouched, True)

    return thisBoost


# ----------------------------------------------+
# Goal-Object: Reach the goal to win.
# ----------------------------------------------+


def goal_touched(game):
    # TODO: Present Statistics, high scores, allow user to enter name,...
    game.musicControl.play(True)
    game.state = "mainMenu"


def generateGoal(lvl, pos):
    thisGoal = Item("teleporter", lvl, pos, 2.5, goal_touched, False)
    return thisGoal
