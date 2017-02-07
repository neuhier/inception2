# ----------------------------------------------------+
# Menu Renderer
# Will draw the menu for a given menu-state on a
# surface. This might include drawing menu-items
# or user-input-dialogs, e.g. for key-configuration.
# ----------------------------------------------------+
class MenuRenderer(object):
    def renderMenu(self, menu):
        if menu.menuState == "mainMenu":
            for i in menu.items:
                if i.isSelected:
                    printtext = "(*)"
                else:
                    printtext = "( )"
                print printtext + i.text
        elif menu.menuState == "quitGame":
            pass
        elif menu.menuState == "setName":
            pass
        elif menu.menuState == "keyConfig":
            pass
