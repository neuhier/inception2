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
        txt = game.menuFont.render(printtext + menu.items[i].text, True, Constants.WHITE)
        game.screen.blit(txt,
                         (game.screen_w / 2 - txt.get_width() / 2, game.screen_h / 4 + i * txt.get_height() + i * 20))
