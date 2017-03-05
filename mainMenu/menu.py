#------------------------------+
# Main menu.py class
#------------------------------+
from mainMenu.menuItem import MenuItem


class Menu():
    def __init__(self, game):
        self.menuState = "mainMenu"
        self.playerName = game.player.name
        self.items = [MenuItem("Start Game", "startGame"),
                      MenuItem("New Player", "newPlayer"),
                      MenuItem("Load Player", "loadPlayer"),
                      MenuItem("Quit Game", "quitGame")]
        self.selected = 0

    # Select next or previous menu item
    def select(self, next):
        if next:
            if (self.selected + 1) < len(self.items):
                self.selected += 1
            else:
                self.selected = 0
        else:
            if self.selected == 0:
                self.selected = len(self.items) - 1
            else:
                self.selected -= 1

    # Get the command of the currently selected item
    def get_selected(self):
        return self.items[self.selected].menuState

    # Get the text of the previous menu item
    def getPrev(self):
        if len(self.items) == 1:
            return "---"
        elif len(self.items) > 1:
            if self.selected == 0:
                return self.items[len(self.items) - 1].text
            else:
                return self.items[self.selected - 1].text
        else:
            return "---"

    def getNext(self):
        if len(self.items) == 1:
            return "---"
        elif len(self.items) > 1:
            if self.selected == len(self.items) - 1:
                return self.items[0].text
            else:
                return self.items[self.selected + 1].text
        else:
            return "---"
