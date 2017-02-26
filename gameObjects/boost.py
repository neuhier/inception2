# ------------------------------------------------------+
# Class to represent a temporary boost for the player
# ------------------------------------------------------+
import datetime


class Boost():
    def __init__(self, duration, startEffect, endEffect, message):
        self.start = datetime.datetime.now()
        self.duration = duration
        self.startEffect = startEffect
        self.endEffect = endEffect
        self.message = message
