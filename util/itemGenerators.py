import random

from boostGenerators import generateSpeedBoost
from gameObjects.item import Item


# ----------------------------------------------+
# Function to generate a tree on the level
# ----------------------------------------------+
def tree_touched(game):
    game.player.bounce_back()


def generateTree(game):
    # Generate a name for the object ==> defines skin
    treeSkins = {}
    for key, value in game.imgMngr.all_images.items():
        if 'tree' in str(key):
            treeSkins[key] = value
    type = treeSkins.keys()[random.randint(0, len(treeSkins.keys()) - 1)]

    # Random position in the level
    x = random.randint(0, len(game.level.texture_grid) - 1)
    y = random.randint(0, len(game.level.texture_grid[0]) - 1)

    thistree = Item(type, game.imgMngr, [x, y], tree_touched, False)

    return thistree


# ----------------------------------------------+
# Function to generate a speedboost-panel
# ----------------------------------------------+
def generateSpeedBoostPanel(game):
    def panelTouched(game):
        sb = generateSpeedBoost()
        game.player.ltBoosts += 1
        game.activeBoosts.append(sb)
        game.activeMessages.append(sb.message)
        sb.startEffect(game)

    # Random position in the level
    x = random.randint(0, len(game.level.texture_grid) - 1)
    y = random.randint(0, len(game.level.texture_grid[0]) - 1)

    thisBoost = Item("speedboost", game.imgMngr, [x, y], panelTouched, True)

    return thisBoost


# ----------------------------------------------+
# Goal-Object: Reach the goal to win.
# ----------------------------------------------+
def goal_touched(game):
    # TODO: Present Statistics, high scores, allow user to enter name,...
    game.musicControl.play(True)
    game.player.resetIngameAttributes()
    game.player.ltLevelFinishes += 1
    game.player.savePlayer()
    game.activeMessages = []
    game.activeBoosts = []
    game.state = "levelEnd"


def generateGoal(game, pos):
    thisGoal = Item("teleporter", game.imgMngr, pos, goal_touched, False)
    return thisGoal
