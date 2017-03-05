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
from gameObjects.player import Player, loadPlayerList, loadPlayer
from levelGenerators import initRandomLevel
from menu import Menu
from menuItem import MenuItem


def menuListen(evt, menu, game):
    pressed = pygame.key.get_pressed()
    if evt.type == pygame.KEYDOWN:
        if menu.menuState == "enteringPlayerName":
            key_value = evt.unicode
            if (re.match("^[A-Za-z0-9_-]*$", key_value)):
                menu.playerName += key_value
                # TODO: Backspace => Delete char
        if pressed[Constants.up]:
            if menu.menuState == "mainMenu":
                menu.select(False)
            elif menu.menuState == "chosingPlayer":
                menu.submenu.select(False)
        if pressed[Constants.down]:
            if menu.menuState == "mainMenu":
                menu.select(True)
            elif menu.menuState == "chosingPlayer":
                menu.submenu.select(True)
        if pressed[Constants.fire]:
            # ----------------------+
            # MAIN MENU
            #----------------------+
            if menu.get_selected() == "startGame":
                initRandomLevel("classic", 30, 30, game)
                game.level.render_chars.add(game.player)
                game.musicControl.play(False)
                game.activeMessages.append(Message("Find the teleporter! Fast!", 3))
                game.state = "playing"
            # ----------------------+
            # New Player
            #----------------------+
            elif menu.get_selected() == "newPlayer":
                if menu.menuState == "enteringPlayerName":
                    game.player = Player(menu.playerName, game.imgMngr)
                    menu.menuState = "mainMenu"
                else:
                    menu.menuState = "enteringPlayerName"
                    menu.playerName = ""
            # ----------------------+
            # Load Player
            # ----------------------+
            elif menu.get_selected() == "loadPlayer":
                if menu.menuState == "chosingPlayer":
                    menu.menuState = "mainMenu"
                    game.player = loadPlayer(menu.submenu.items[menu.submenu.selected].text, game.imgMngr)
                    menu.playerName = game.player.name
                elif menu.menuState == "mainMenu":
                    menu.submenu = Menu(game)
                    menu.submenu.items = []
                    for i in loadPlayerList():
                        menu.submenu.items.append(MenuItem(i, i))
                    menu.menuState = "chosingPlayer"
            # ----------------------+
            # Quit Game
            #----------------------+
            elif menu.get_selected() == "quitGame":
                sys.exit()  # Shut down