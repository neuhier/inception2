# ----------------------------------------------+
# Managing background music
# ----------------------------------------------+
# Load all available tracks from the resources
import os
import random

import pygame


class MusicController():
    def __init__(self, theme):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        self.theme = theme

    def play(self, menu):
        pygame.mixer.music.stop()
        if menu:
            self.loadMenuSound()
            pygame.mixer.music.play(-1)
        else:
            self.loadRandomTrack()
            pygame.mixer.music.play(-1)

    def loadMenuSound(self):
        scriptPath = os.path.dirname(__file__)
        path = os.path.join(scriptPath, "../resources/music/MenuSound.ogg")
        pygame.mixer.music.load(path)

    def loadRandomTrack(self):
        scriptPath = os.path.dirname(__file__)
        dirPath = os.path.join(scriptPath, "../resources/music/" + self.theme + "/")
        allTracks = os.listdir(dirPath)
        trackNr = random.randint(0, len(allTracks) - 1)
        trackPath = os.path.join(dirPath, allTracks[trackNr])
        pygame.mixer.music.load(trackPath)
