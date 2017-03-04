# --------------------------------------------------------------------------------+
#
#  The mainMenu listener deals with user inputs when the game is in mainMenu-game-state.
# <Up> and <down> cursors will select menu entries. <Enter> is used to confirm.
# --------------------------------------------------------------------------------+
import re
import sys

import pygame

import Constants
from gameObjects.message import Message
from gameObjects.player import Player
from levelGenerators import initRandomLevel


def menuListen(evt, menu, game):
    pressed = pygame.key.get_pressed()
    if evt.type == pygame.KEYDOWN:
        if menu.menuState == "enteringPlayerName":
            key_value = evt.unicode
            if (re.match("^[A-Za-z0-9_-]*$", key_value)):
                menu.playerName += key_value

        if pressed[Constants.up]:
            menu.select(False)

        if pressed[Constants.down]:
            menu.select(True)

        if pressed[Constants.fire]:
            if menu.get_selected() == "startGame":
                initRandomLevel("classic", 30, 30, game)
                game.level.render_chars.add(game.player)
                game.musicControl.play(False)
                game.activeMessages.append(Message("Find the teleporter! Fast!", 3))
                game.state = "playing"
            elif menu.get_selected() == "newPlayer":
                if menu.menuState == "enteringPlayerName":
                    game.player = Player(menu.playerName, game.imgMngr)
                    menu.menuState = "mainMenu"
                else:
                    menu.menuState = "enteringPlayerName"
                    menu.playerName = ""
            elif menu.get_selected() == "quitGame":
                sys.exit()  # Shut down