# ----------------------------------------------------+
# Menu Item class
# A menu item is just a title, image and a command.
# The command changes the menu state so that the
# renderer will react to user input.
# ----------------------------------------------------+
class MenuItem(object):
    def __init__(self, text, menuState):
        self.text = text  # Button text
        self.menuState = menuState  # The menu state that is used when the button is activated
        self.isSelected = False
