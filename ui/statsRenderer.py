# ------------------------------------------------+
# Display the player stats at the end of a level
# ------------------------------------------------+
import Constants


def renderStats(game):
    # TODO: different messages depending on if the level was finished successfully or player died
    msg = game.menuFont.render("Level finished!", True, Constants.WHITE)
    game.screen.blit(msg, (game.screen_w / 2 - msg.get_width() / 2, 2 * msg.get_height()))

    # Stats
    msg_finishes = game.smallMenuFont.render("Lifetime Level Finishes:  " + str(game.player.ltLevelFinishes), True,
                                             Constants.WHITE)
    game.screen.blit(msg_finishes, (
    game.screen_w / 2 - msg_finishes.get_width() / 2, 4 * msg.get_height() + msg_finishes.get_height()))

    msg_kills = game.smallMenuFont.render("Lifetime Kills:  " + str(game.player.ltKills), True, Constants.WHITE)
    game.screen.blit(msg_kills, (
    game.screen_w / 2 - msg_kills.get_width() / 2, 4 * msg.get_height() + 2 * msg_finishes.get_height()))

    msg_death = game.smallMenuFont.render("Lifetime Deaths: " + str(game.player.ltDeath), True, Constants.WHITE)
    game.screen.blit(msg_death, (
    game.screen_w / 2 - msg_death.get_width() / 2, 4 * msg.get_height() + 3 * msg_finishes.get_height()))

    msg_shots = game.smallMenuFont.render("Lifetime Shots Fired:  " + str(game.player.ltShots), True, Constants.WHITE)
    game.screen.blit(msg_shots, (
    game.screen_w / 2 - msg_shots.get_width() / 2, 4 * msg.get_height() + 4 * msg_finishes.get_height()))

    msg_boosts = game.smallMenuFont.render("Lifetime Boosts Collected:  " + str(game.player.ltBoosts), True,
                                           Constants.WHITE)
    game.screen.blit(msg_boosts, (
    game.screen_w / 2 - msg_boosts.get_width() / 2, 4 * msg.get_height() + 5 * msg_finishes.get_height()))

    cont = game.smallMenuFont.render("<Press FIRE to continue>", True, Constants.WHITE)
    game.screen.blit(cont,
                     (game.screen_w / 2 - cont.get_width() / 2, 4 * msg.get_height() + 7 * msg_finishes.get_height()))
