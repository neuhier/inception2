#------------------------------+
# Game class
#------------------------------+
import datetime

import pygame

from ai.theBrain import commandVillians
from eventHandlers import menuListener
from eventHandlers.gameListener import listen
from gameObjects.item import Item
from gameObjects.player import loadPlayer
from mainMenu import menu
from sounds.musicLibrary import MusicController
from ui import menuRenderer
from ui.gameRenderer import renderTextures, renderItems
from ui.hudRenderer import renderHUD
from ui.imageManager import ImageManager
from ui.messageRenderer import renderMessages
from ui.statsRenderer import renderStats
from util import Constants



class Game(object):

    #-----------------------------------------------+
    # Initialize a new game.
    #-----------------------------------------------+
    def __init__(self):

        self.load_settings()  # Load the current game settings

        pygame.init()  # Initialize pygame engine
        pygame.display.set_caption(Constants.game_title)

        self.clock = pygame.time.Clock()  # Used to manage how fast the screen updates
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))  # Set up the screen

        self.state = "mainMenu"  # Game state: mainMenu, ...
        self.level = None

        self.menuFont = pygame.font.Font("resources/fonts/kenvector_future.ttf", int(self.screen_h / 12))
        self.smallMenuFont = pygame.font.Font("resources/fonts/kenvector_future.ttf", int(self.screen_h / 20))
        self.ingameFont = pygame.font.Font("resources/fonts/kenvector_future.ttf", int(self.screen_h / 18.75))

        self.imgMngr = ImageManager("classic")
        self.imgMngr.rescale_images(self.screen_h)
        self.player = loadPlayer("Neuhier", self.imgMngr)

        self.activeBoosts = []
        self.activeMessages = []

        self.musicControl = MusicController("classic")
        self.musicControl.play(True)

        mM = menu.Menu(self)

        # Start the game loop
        self.isPaused = False
        while not self.isPaused:

            self.screen.fill(Constants.BLACK)  # Start with a clear screen every time

            #--------------------------------------------+
            # Recognise keyboard input
            #--------------------------------------------+
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
            if self.state == "mainMenu":
                menuListener.menuListen(ev, mM, self)
            elif self.state == "levelEnd":
                if ev.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[Constants.fire]:
                        self.state = "mainMenu"
            elif self.state == "playing":
                # --------------------------------------------+
                # The Brain controls villians here
                # --------------------------------------------+
                commandVillians(self)

                # Move projectiles
                self.level.update()

                # Input listener for keyboard (should be gamepad later as well)
                listen(ev, self)

                # Collosion detection and handling
                touched = pygame.sprite.spritecollide(self.player, self.level.items, False)
                for i in touched:
                    if type(i) is Item:
                        i.when_touched(self)

                # Check if projectiles hit villians
                char_got_hit = pygame.sprite.groupcollide(self.level.chars, self.level.render_projectiles, False, False)
                for i in char_got_hit:
                    i.get_hit(char_got_hit[i][0], self)

                # --------------------------------------------+
                # Manage active boosts
                # --------------------------------------------+
                for i in self.activeBoosts:
                    if (datetime.datetime.now() - i.start).total_seconds() >= i.duration:
                        i.endEffect(self)
                        # TODO: Add message when boost ends
                        self.activeBoosts.remove(i)
                # --------------------------------------------+
                # Manage messages
                # --------------------------------------------+
                for i in self.activeMessages:
                    if i.isDone():
                        self.activeMessages.remove(i)
            #--------------------------------------------+
            # Render stuff depending on game state
            #--------------------------------------------+
            if self.state == "mainMenu":
                menuRenderer.renderMenu(mM, self)
            elif self.state == "playing":
                renderTextures(self)
                renderItems(self)
                renderHUD(self)
                renderMessages(self, self.screen, self.screen_w, self.screen_h, self.ingameFont)
            elif self.state == "levelEnd":
                renderStats(self)
            #--------------------------------------------+
            # Draw on screen
            #--------------------------------------------+
            self.clock.tick(60)
            pygame.display.flip()

    # -----------------------------------------------+
    # Load game paramters from local textfile.
    # Parameters are:
    # - Player name
    # - Key condfiguration, Screen resolution, ...
    # - (High-Scores?)
    # -----------------------------------------------+
    def load_settings(self):
        #TODO: check if settings.txt exists, if it does => load content
        self.keys = {"up": Constants.up,
                     "down": Constants.down,
                     "left": Constants.left,
                     "right": Constants.right,
                     "fire": Constants.fire,
                     "next_w": Constants.next_w,
                     "prev_w": Constants.prev_w}
        self.screen_w   = Constants.screen_width
        self.screen_h   = Constants.screen_height