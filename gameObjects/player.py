# ------------------------------------------------------------------------------+
# Player Class
#
# The player class contains all information about the player.
#
# ------------------------------------------------------------------------------+
import datetime

import pygame

import Constants
from Functions import getMovingVector
from gameObjects.character import Character
from weaponGenerators import generateGun, generateRifle


class Player(Character):
    def __init__(self, name, ImgMgr):
        # Global attributes
        self.name = name
        self.ltKills = 0
        self.ltBoosts = 0
        self.ltDeath = 0
        self.ltShots = 0
        self.ltCoins = 0
        self.ltLevelFinishes = 0

        # Ingame attributes
        self.inventory = []  # Player's weapons
        self.equiped_weapon = 0  # Which weapon in the inventory is currently equiped
        self.angle = 0
        self.last_shot = datetime.datetime.now()
        self.moving_dir = 1  # postive number represent moving to the front, negative number show we last moved back
        self.position = [0, 0]  # Player's position in the level (x, y)
        self.speed = Constants.player_default_speed  # Players current speed
        self.hitpoints = [Constants.player_default_hitpts,
                          Constants.player_default_hitpts]  # A list with 2 items. Current_hitpoints and max_hittpoints
        self.medipacks = Constants.player_default_medikits  # Number of available medipacks

        # other stuff
        pygame.sprite.Sprite.__init__(self)  # needed for subclasses of sprites
        self.baseimage = ImgMgr.all_images[Constants.player_img]
        self.image = self.baseimage
        self.rect = self.image.get_rect()
        self.rect.centerx = pygame.display.Info().current_w / 2
        self.rect.centery = pygame.display.Info().current_h / 2

        # By default add a gun to the inventory
        self.inventory.append(generateGun())
        self.inventory.append(generateRifle())

    # ------------------------------------+
    # Function to move the player
    # -----------------------------------+
    def move(self, direction, lvl):
        v = getMovingVector(self)
        if direction > 0:
            new_x = self.position[0] + v[0] * self.speed
            new_y = self.position[1] + v[1] * self.speed
        else:
            new_x = self.position[0] - v[0] * self.speed
            new_y = self.position[1] - v[1] * self.speed
        if 0 <= new_x <= len(lvl.texture_grid) and 0 <= new_y <= len(
                lvl.texture_grid[0]):  # Cannot go outside the level
            self.position = [new_x, new_y]
        self.moving_dir = direction

    # ------------------------------------+
    # Bounce back method moves player to the
    # previous position. Used by non-passable
    # objects.
    # ------------------------------------+
    def bounce_back(self):
        v = getMovingVector(self)
        new_x = self.position[0] + v[0] * self.speed * self.moving_dir * (
        -1)  # Move just opposite to what we did before
        new_y = self.position[1] + v[1] * self.speed * self.moving_dir * (-1)
        self.position = [new_x, new_y]

    # ------------------------------------+
    # Return the currently used weapon
    # -----------------------------------+
    def get_current_weapon(self):
        return self.inventory[self.equiped_weapon]

    # ---------------------------------------+
    # Chose the next weapon in the inventory
    # ---------------------------------------+
    def next_weapon(self):
        if self.equiped_weapon == len(self.inventory) - 1:
            self.equiped_weapon = 0
        else:
            self.equiped_weapon += 1

    # ---------------------------------------+
    # Chose the previous weapon in the inventory
    # ---------------------------------------+
    def previous_weapon(self):
        if self.equiped_weapon == 0:
            self.equiped_weapon = len(self.inventory) - 1
        else:
            self.equiped_weapon -= 1

    # ---------------------------------------+
    # Function to save player in textfile
    # ---------------------------------------+
    def savePlayer(self):
        saveFile = open(self.name + ".txt", "w+")


# ---------------------------------------+
# Function to load player information
# ---------------------------------------+
def loadPlayer(name, ImgMngr):
    if name == "default":
        return Player("Neuhier", ImgMngr)
    else:
        return Player(name, ImgMngr)
