# ----------------------------------------------------+
# menu.py Renderer
# Will draw the mainMenu for a given mainMenu-state on a
# surface. This might include drawing mainMenu-items
# or user-input-dialogs, e.g. for key-configuration.
# ----------------------------------------------------+
import Constants


def renderMenu(menu, game):
    # ------------------+
    # Main Menu
    # ------------------+
    if menu.menuState == "mainMenu":
        playerName = game.menuFont.render("Player: " + menu.playerName, True, Constants.RED)
        game.screen.blit(playerName, (game.screen_w - playerName.get_width(), playerName.get_height() / 2))
        for i in range(0, len(menu.items)):
            if i == menu.selected:
                printtext = "(+)"
            else:
                printtext = "(   )"
            txt = game.menuFont.render(printtext + menu.items[i].text, True, Constants.WHITE)
            game.screen.blit(txt,
                             (game.screen_w / 2 - txt.get_width() / 2,
                              game.screen_h / 4 + i * txt.get_height() + i * 20))
    # ------------------+
    # Enter Player Name
    #------------------+
    elif menu.menuState == "enteringPlayerName":
        infoTxt = game.menuFont.render("Enter Name", True, Constants.WHITE)
        game.screen.blit(infoTxt,
                         (game.screen_w / 2 - infoTxt.get_width() / 2, game.screen_h / 2 - 3 * infoTxt.get_height()))
        playerName = game.menuFont.render(menu.playerName, True, Constants.RED)
        game.screen.blit(playerName, (
        game.screen_w / 2 - playerName.get_width() / 2, game.screen_h / 2 - playerName.get_height() / 2))
    # ------------------+
    # Load Player
    # ------------------+
    elif menu.menuState == "chosingPlayer":
        prevItem = game.menuFont.render(menu.submenu.getPrev(), True, Constants.WHITE)
        game.screen.blit(prevItem,
                         (game.screen_w / 2 - prevItem.get_width() / 2, game.screen_h / 2 - 2 * prevItem.get_height()))

        selectedItem = game.menuFont.render("* " + menu.submenu.items[menu.submenu.selected].text + " *", True,
                                            Constants.WHITE)
        game.screen.blit(selectedItem, (
        game.screen_w / 2 - selectedItem.get_width() / 2, game.screen_h / 2 - selectedItem.get_height() / 2))

        nextItem = game.menuFont.render(menu.submenu.getNext(), True, Constants.WHITE)
        game.screen.blit(nextItem,
                         (game.screen_w / 2 - nextItem.get_width() / 2, game.screen_h / 2 + 1 * nextItem.get_height()))
