# ---------------------------------------------------------+
# React to user input (keyboard/joystick)
# ---------------------------------------------------------+
import pygame

import Constants


# ---------------------------------------------------------+
# Function to react to user input.
# Turns the player around, shoots, jumps, moves,...
# Returns true if player is moving, false when player stops
# moving.
# ---------------------------------------------------------+
def listen(event, game):
    pressed = pygame.key.get_pressed()
    if pressed[Constants.left]:
        game.player.turn(-Constants.player_default_turn_speed)
    if pressed[Constants.right]:
        game.player.turn(Constants.player_default_turn_speed)
    if pressed[Constants.up]:
        game.player.move(1, game.level)
    if pressed[Constants.down]:
        game.player.move(-1, game.level)
    if pressed[Constants.fire]:
        game.level.playerShoot(game)  # Let player fire
    if event.type == pygame.KEYDOWN:
        if pressed[Constants.next_w]:
            game.player.next_weapon()
        if pressed[Constants.prev_w]:
            game.player.previous_weapon()
