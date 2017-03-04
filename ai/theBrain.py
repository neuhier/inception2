# ---------------------------------------------+
# THE BRAIN controls all villians in a level.
# ---------------------------------------------+

import numpy


def commandVillians(game):
    # Move all villians in direction of the player
    for i in game.level.chars:
        rotation_degree = direction(game.player, i) * i.turning_speed
        if abs(rotation_degree) > 0:
            i.turn(rotation_degree)
        i.move(game.level)


# Get the angle in which direction the player stands
def get_angle(player, villian):
    return numpy.arctan2(player.position[0] - villian.position[0],
                         player.position[1] - villian.position[1]) * 180 / numpy.pi  # X


# Determine in which direction to turn so that the villian tries to look at the player
def direction(player, villian):
    tgt_angle = get_angle(player, villian)  # Get direction of player
    if tgt_angle < 0:
        tgt_angle = abs(tgt_angle) + 180
    else:
        tgt_angle = abs(tgt_angle - 180)
    # Get the direction to turn into
    angle_diff = tgt_angle - villian.angle
    if angle_diff > 3:
        if angle_diff < 180:
            return 1
        else:
            return -1
    elif angle_diff < -3:
        if angle_diff > -180:
            return -1
        else:
            return 1
    else:
        return 0
