# --------------------------------------------------------------------------------+
#
#  The mainMenu listener deals with user inputs when the game is in mainMenu-game-state.
# <Up> and <down> cursors will select menu entries. <Enter> is used to confirm.
# --------------------------------------------------------------------------------+
import sys

import pygame

import Constants


def menuListen(evt, menu, game):
    pressed = pygame.key.get_pressed()
    if evt.type == pygame.KEYDOWN:
        if pressed[Constants.up]:
            menu.select(False)
        if pressed[Constants.down]:
            menu.select(True)
        if pressed[Constants.fire]:
            if menu.get_selected() == "startGame":
                game.state = "playing"
            elif menu.get_selected() == "quitGame":
                sys.exit()  # Shut down
