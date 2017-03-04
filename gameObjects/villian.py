# ------------------------------------------------------------------------------+
# Villian Class
#
# Villians are characters very similar like players. The main difference is
# that they are controlled by the game.
#
# ------------------------------------------------------------------------------+

import pygame

from Functions import getMovingVector
from gameObjects.character import Character
from weaponGenerators import generateGun


class Villian(Character):

    # Constructor
    def __init__(self, name, imgMgr, position):
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites
        self.baseimage = imgMgr.all_images[name]  # Load the right image
        self.image = self.baseimage
        self.rect = self.image.get_rect()
        self.position = position

        self.name = "zombie"  # Determines used image and behaviour(?)
        self.angle = 0  # Angle of view
        self.viewing_range = 10  # When does the villian react to the player? texture grid dimension
        self.inventory = []  # Available weapons
        self.equiped_weapon = 0  # Currently used weapon

        # By default add a gun to the inventory
        self.inventory.append(generateGun())
        self.hitpoints = [100, 100]

        self.turning_speed = 5
        self.speed = 0.01

    # ------------------------------------+
    # Function to move the villian
    # -----------------------------------+
    def move(self, lvl):
        v = getMovingVector(self)
        new_x = self.position[0] + v[0] * self.speed
        new_y = self.position[1] + v[1] * self.speed
        if 0 < new_x <= len(lvl.texture_grid) - 1 and 0 < new_y <= len(
                lvl.texture_grid[0]) - 1:  # Cannot go outside the level
            self.position = [new_x, new_y]