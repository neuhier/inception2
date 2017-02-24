# ------------------------------------------------+
# Collection of usefull functions
# ------------------------------------------------+

import math
import os

import pygame


# Load an image (assumes images are in a subfolder of the script itself
def load_img(path):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, path)
    this_img = pygame.image.load(abs_file_path).convert()
    return this_img


# Function that returns the "v"-vector on the level grid when something is moving
def getMovingVector(movingthing):
    return (math.cos((movingthing.angle - 90) * math.pi / 180), math.sin((movingthing.angle - 90) * math.pi / 180))
