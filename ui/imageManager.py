# -----------------------------------------------------------------------+
# Load all relevant textures/images for the level - based on its' theme
# -----------------------------------------------------------------------+
import os

import pygame

import Functions


class ImageManager():
    def __init__(self, theme):
        self.all_textures = {}
        self.all_images = {}
        self.load_imgs(theme)
        self.texture_size = self.all_textures[self.all_textures.keys()[0]].get_rect().size

    def load_imgs(self, theme):
        # get a list of all files in according directory
        txtr_files = os.listdir("resources/imgs/" + theme + "/")
        for i in txtr_files:
            if i[0] != ".":
                this_name = i[3:(
                    len(
                        i) - 4)]  # Remove the leading indicator if image is texture or not and remove the image file ending
                if "bg_" in i:
                    texture = Functions.load_img("resources/imgs/" + theme + "/" + i)
                    texture = pygame.transform.scale(texture, (32, 32))  # Rescale to 32x32px
                    self.all_textures[this_name] = texture
                else:
                    img = Functions.load_img("resources/imgs/" + theme + "/" + i)
                    img = pygame.transform.scale(img, (img.get_width() * 32 / img.get_height(), 32))
                    self.all_images[this_name] = img

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
