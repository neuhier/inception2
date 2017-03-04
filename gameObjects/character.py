# ------------------------------------------------------------------------------+
# Character Class
#
# Parent class for Players and Villians.
# ------------------------------------------------------------------------------+
import pygame


class Character(pygame.sprite.Sprite):

    # ------------------------------------+
    # Function to change the angle
    # and adjust the image accordingly
    # -----------------------------------+
    def turn(self, degree):
        if self.angle + degree > 360:
            self.angle = self.angle - 360 + degree
        elif self.angle + degree < 0:
            self.angle = self.angle + 360 + degree
        else:
            self.angle += degree
        orig_xy = self.rect.center  # Save the original position on screen// pygame moves the image when rotating
        self.image = pygame.transform.rotate(self.baseimage, -(self.angle))  # Rotate
        self.rect.center = orig_xy  # Center around the original position

