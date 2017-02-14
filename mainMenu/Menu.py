#------------------------------+
# Main Menu.py class
#------------------------------+
from mainMenu.MenuItem import MenuItem


class Menu(object):
    def __init__(self):
        self.menuState = "mainMenu"
        self.items = [MenuItem("Start Game", "startGame"),
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
