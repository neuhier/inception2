# -----------------------------+
# Function to generate boosts
# -----------------------------+


import random

from gameObjects.boost import Boost
from gameObjects.message import Message


def generateSpeedBoost():
    speedInc = random.randint(2, 2) / 20.0
    duration = random.randint(5, 10)

    def increasePlayerSpeed(game):
        game.player.speed += speedInc

    def decreasePlayerSpeed(game):
        game.player.speed -= speedInc

    message = Message(str(duration) + " second speed boost!", 2)

    speedBoost = Boost(duration, increasePlayerSpeed, decreasePlayerSpeed, message)

    return speedBoost
