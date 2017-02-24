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
def listen(event, lvl):
    pressed = pygame.key.get_pressed()
    if pressed[Constants.left]:
        lvl.player.turn(-Constants.player_default_turn_speed)
    if pressed[Constants.right]:
        lvl.player.turn(Constants.player_default_turn_speed)
    if pressed[Constants.up]:
        lvl.player.move(1, lvl)
    if pressed[Constants.down]:
        lvl.player.move(-1, lvl)
    if pressed[Constants.next_w]:
        lvl.player.next_weapon()
    if pressed[Constants.prev_w]:
        lvl.player.previous_weapon()
    if pressed[Constants.fire]:
        lvl.char_fire(lvl.player)  # Let player fire
