#------------------------------+
# Game class
#------------------------------+
import pygame

import MenuListener
import MenuRenderer
from mainMenu import Menu
from util import Constants


class Game(object):

    #-----------------------------------------------+
    # Initialize a new game.
    #-----------------------------------------------+
    def __init__(self):

        self.state = "mainMenu"  # Game state: mainMenu, ...
        self.load_settings()                # Load the current game settings
        pygame.init()                       # Initialize pygame engine
        self.font = pygame.font.Font("resources/fonts/kenvector_future.ttf", 32)
        self.clock = pygame.time.Clock()  # Used to manage how fast the screen updates
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))  # Set up the screen
        pygame.display.set_caption(Constants.game_title)

        mM = Menu.Menu()

        # Start the game loop
        while True:
            self.screen.fill(Constants.BLACK)  # Start with a clear screen every time
            #--------------------------------------------+
            # Recognise keyboard input
            #--------------------------------------------+
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
            if self.state == "mainMenu":
                MenuListener.menuListen(ev, mM, self)
            elif self.state == "playing":
                self.keyListen(ev)
            #--------------------------------------------+
            # Render stuff depending on game state
            #--------------------------------------------+
            if self.state == "mainMenu":
                MenuRenderer.renderMenu(mM, self)
            elif self.state == "playing":
                pass
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
        self.playername  = "Jeff"
        self.keys = {"up": Constants.up,
                     "down": Constants.down,
                     "left": Constants.left,
                     "right": Constants.right,
                     "fire": Constants.fire,
                     "next_w": Constants.next_w,
                     "prev_w": Constants.prev_w}
        self.screen_w   = Constants.screen_width
        self.screen_h   = Constants.screen_height

    #-----------------------------------------------------+
    # InputListener: React to keyboard events (joystick?)
    #-----------------------------------------------------+
    def keyListen(self, evt):
        pass
