# ----------------------------------------------+
# Function to generate a tree on the level
# ----------------------------------------------+
import random

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

    thistree = Item(type, lvl, [x, y], [w, h], tree_touched, False)

    return thistree
