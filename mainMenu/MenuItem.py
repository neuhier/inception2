# ----------------------------------------------------+
# Menu.py Item class
# A mainMenu item is just a title, image and a command.
# The command changes the mainMenu state so that the
# renderer will react to user input.
# ----------------------------------------------------+
class MenuItem(object):
    def __init__(self, text, menuState):
        self.text = text  # Button text
        self.menuState = menuState  # The mainMenu state that is used when the button is activated
