import datetime

import pygame

import Constants
import util


# --------------------------------------------------+
# Render how long it will take to load the weapon
# --------------------------------------------------+
def renderLoadingTime(game):
    pygame.draw.rect(game.screen, Constants.WHITE, (Constants.reload_bar_width,
                                                    Constants.reload_bar_height / 2,
                                                    Constants.reload_bar_width,
                                                    Constants.reload_bar_height), 0)
    # Calculate loading time left
    max_loading_time = game.player.get_current_weapon().reload_time
    time_left = max_loading_time - (datetime.datetime.now() - game.player.last_shot).total_seconds()
    if time_left > 0:
        pygame.draw.rect(game.screen, Constants.BLACK, (Constants.reload_bar_width + 2,
                                                        Constants.reload_bar_height / 2 + 2,
                                                        Constants.reload_bar_width - 4,
                                                        Constants.reload_bar_height / (
                                                        max_loading_time) * time_left - 4))


def renderWeapon(game):
    # Show equiped weapon
    wpn_img = game.imgMngr.all_images[game.player.get_current_weapon().name]
    game.screen.blit(wpn_img, (Constants.reload_bar_width * 2.5, Constants.reload_bar_height / 2))


# Return the position of the text displayed on the top right corner
def textPosition(text, n, screen_w):
    new_x = screen_w - text.get_width()
    new_y = 0 + text.get_height() * n + (n + 1) * 10
    return [new_x, new_y]


def renderHUD(game):
    # Render player info
    player_htps = game.ingameFont.render(
        "Hitpoints: " + str(game.player.hitpoints[0]) + "/" + str(game.player.hitpoints[1]),
        True, util.Constants.WHITE)
    game.screen.blit(player_htps, textPosition(player_htps, 0, game.screen_w))

    renderWeapon(game)
    renderLoadingTime(game)
