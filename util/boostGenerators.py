# -----------------------------+
# Function to generate boosts
# -----------------------------+


import random

from gameObjects.boost import Boost


# Speedboost
def generateSpeedBoost():
    speedInc = random.randint(2, 2) / 20.0
    duration = random.randint(5, 10)

    def increasePlayerSpeed(level):
        level.player.speed += speedInc

    def decreasePlayerSpeed(level):
        level.player.speed -= speedInc

    message = "You just got a " + str(duration) + " second speed boost! Say 'Thank you!'"

    speedBoost = Boost(duration, increasePlayerSpeed, decreasePlayerSpeed, message)

    return speedBoost
