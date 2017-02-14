# ----------------------------------------------------+
# menu.py Renderer
# Will draw the mainMenu for a given mainMenu-state on a
# surface. This might include drawing mainMenu-items
# or user-input-dialogs, e.g. for key-configuration.
# ----------------------------------------------------+
import Constants


def renderMenu(menu, game):
    for i in range(0, len(menu.items)):
        if i == menu.selected:
            printtext = "(+)"
        else:
            printtext = "(   )"
        txt = game.font.render(printtext + menu.items[i].text, True, Constants.WHITE)
        game.screen.blit(txt, (10, i * txt.get_height() + i * 20))
