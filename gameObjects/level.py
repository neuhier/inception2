# ------------------------------------------------------------------------------+
# Level Class
#
# The level is the central class of the game. It contains information
# about the level itself and everything that is in the level.
#
# ------------------------------------------------------------------------------+
import datetime
import os

import numpy
import pygame

import Functions
from gameObjects.projectile import Projectile


class Level():
    # -----------------------------------------------------------------------+
    # Constructor
    # -----------------------------------------------------------------------+
    def __init__(self, theme, width, height, screen_h):

        self.theme = theme  # Set the theme

        self.texture_grid = numpy.zeros((width, height))  # Set level dimension
        self.all_textures = {}  # A dictionary storing all texture that will be used in the level (which depends on theme)
        self.all_images = {}  # A dictionary of all images used for objects, items, etc.
        self.texture_size = []  # The dimension of textures in pixels (widht, height)

        self.load_imgs()
        self.rescale_images(screen_h)

        self.items = pygame.sprite.Group()  # A spriteGroup containing all items in the level
        self.render_items = pygame.sprite.Group()  # A spriteGroup that contains only the items that should be rendered

        self.player = []  # The sprite representing the player

        self.chars = pygame.sprite.Group()  # All villians on the map
        self.render_chars = pygame.sprite.Group()  # All the villians that are currently visible

        self.projectiles = pygame.sprite.Group()
        self.render_projectiles = pygame.sprite.Group()  # A separate group managing the projectiles

    # -----------------------------------------------------------------------+
    # Generate a projectile whenever a player fires a shot
    # -----------------------------------------------------------------------+
    def char_fire(self, char):
        # Check reload_time
        loading_time = (datetime.datetime.now() - char.last_shot).total_seconds()
        if loading_time > char.get_current_weapon().reload_time:
            # Generate a projectile
            proj = Projectile(self, char)
            self.projectiles.add(proj)
            char.last_shot = datetime.datetime.now()
            return proj

    # -----------------------------------------------------------------------+
    # Function to be called by the game loop.
    # Will move projectiles and villians
    # -----------------------------------------------------------------------+
    def update(self):
        for i in self.projectiles:
            i.move_me()

    # -----------------------------------------------------------------------+
    # Load all relevant textures/images for the level - based on its' theme
    # -----------------------------------------------------------------------+
    def load_imgs(self):
        # get a list of all files in according directory
        txtr_files = os.listdir("resources/imgs/" + self.theme + "/")
        for i in txtr_files:
            if i[0] != ".":
                this_name = i[3:(
                    len(
                        i) - 4)]  # Remove the leading indicator if image is texture or not and remove the image file ending
                if "bg_" in i:
                    texture = Functions.load_img("resources/imgs/" + self.theme + "/" + i)
                    texture = pygame.transform.scale(texture, (32, 32))  # Rescale to 32x32px
                    self.all_textures[this_name] = texture
                else:
                    img = Functions.load_img("resources/imgs/" + self.theme + "/" + i)
                    img = pygame.transform.scale(img, (img.get_width() * 32 / img.get_height(), 32))
                    self.all_images[this_name] = img
        # Update the texture size
        self.texture_size = self.all_textures[self.all_textures.keys()[0]].get_rect().size

    # -----------------------------------------------------------------------+
    # Rescale all images for a given screen resolution.
    # -----------------------------------------------------------------------+
    def rescale_images(self, screen_h):
        # Basis is 32x32 pixels for texture tiles at 800x600 screen resolution
        newImgHeight = int(screen_h / 9)
        self.texture_size = [newImgHeight, newImgHeight]
        for i in self.all_textures:
            self.all_textures[i] = pygame.transform.scale(self.all_textures[i], (newImgHeight, newImgHeight))
        for i in self.all_images:
            newImgWidth = int(self.all_images[i].get_width() * (
            float(newImgHeight) / self.all_images[i].get_height()))  # There needs to be a player-img always
            self.all_images[i] = pygame.transform.scale(self.all_images[i], (newImgWidth, newImgHeight))
