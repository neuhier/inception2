# ------------------------------------------------------------------------------+
# Level Class
#
# The level is the central class of the game. It contains information
# about the level itself and everything that is in the level.
#
# ------------------------------------------------------------------------------+
import datetime

import numpy
import pygame

from gameObjects.projectile import Projectile


class Level():
    # -----------------------------------------------------------------------+
    # Constructor
    # -----------------------------------------------------------------------+
    def __init__(self, theme, width, height):

        self.theme = theme  # Set the theme

        self.texture_grid = numpy.zeros((width, height))  # Set level dimension
        self.all_textures = {}  # A dictionary storing all texture that will be used in the level (which depends on theme)
        self.all_images = {}  # A dictionary of all images used for objects, items, etc.
        self.texture_size = []  # The dimension of textures in pixels (widht, height)

        self.items = pygame.sprite.Group()  # A spriteGroup containing all items in the level
        self.render_items = pygame.sprite.Group()  # A spriteGroup that contains only the items that should be rendered

        self.chars = pygame.sprite.Group()  # All villians on the map
        self.render_chars = pygame.sprite.Group()  # All the villians that are currently visible

        self.projectiles = pygame.sprite.Group()
        self.render_projectiles = pygame.sprite.Group()  # A separate group managing the projectiles

    # -----------------------------------------------------------------------+
    # Generate a projectile whenever a player fires a shot
    # -----------------------------------------------------------------------+
    def playerShoot(self, game):
        # Check reload_time
        loading_time = (datetime.datetime.now() - game.player.last_shot).total_seconds()
        if loading_time > game.player.get_current_weapon().reload_time:
            # Generate a projectile
            proj = Projectile(game, game.player)
            self.projectiles.add(proj)
            game.player.last_shot = datetime.datetime.now()
            return proj

    # -----------------------------------------------------------------------+
    # Function to be called by the game loop.
    # Will move projectiles and villians
    # -----------------------------------------------------------------------+
    def update(self):
        for i in self.projectiles:
            i.move_me()