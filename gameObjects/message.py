# ------------------------------------------------------+
# Class that represents messages.
# ------------------------------------------------------+
import datetime


class Message():
    def __init__(self, text, duration):
        self.text = text
        self.icon = "default_message"
        self.duration = duration
        self.start = datetime.datetime.now()

    def isDone(self):
        if (datetime.datetime.now() - self.start).total_seconds() > self.duration:
            return True
        else:
            return False
