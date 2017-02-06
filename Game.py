#------------------------------+
# Game class
#------------------------------+
import pygame

from util import Constants


class Game(object):

    lvl     = None      # The currently played level. Is generated whenever player selects "start game" in main menu.
    screen  = None      # Screen to render the game on
    state   = "mainMenu"# Game state: mainMenu, ...
    keys    = {}        # A dictionary representing the key bindings

    #-----------------------------------------------+
    # Initialize a new game.
    #-----------------------------------------------+
    def __init__(self):

        self.load_settings()                # Load the current game settings
        pygame.init()                       # Initialize pygame engine
        clock = pygame.time.Clock()         # Used to manage how fast the screen updates
        screen = pygame.display.set_mode((self.screen_w, self.screen_h))        # Set up the screen
        pygame.display.set_caption(Constants.game_title)

        # Start the game loop
        while True:
            screen.fill(Constants.BLACK)                                # Start with a clear screen every time
            #--------------------------------------------+
            # Recognise keyboard input
            #--------------------------------------------+
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
            if ev.type == pygame.KEYDOWN:
                self.keyListen(ev)
            #--------------------------------------------+
            # Render stuff depending on game state
            #--------------------------------------------+
            if self.state == "mainMenu":
                pass
            elif self.state == "playing":
                pass
            #--------------------------------------------+
            # Draw on screen
            #--------------------------------------------+
            clock.tick(60)
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
        self.keys        = {"up": Constants.up, "down": Constants.down, "left": Constants.left, "right": Constants.right,
                       "fire": Constants.fire, "next_w": Constants.next_w, "prev_w": Constants.prev_w}
        self.screen_w   = Constants.screen_width
        self.screen_h   = Constants.screen_height

    #-----------------------------------------------------+
    # InputListener: React to keyboard events (joystick?)
    #-----------------------------------------------------+
    def keyListen(self, evt):
        if self.state == "mainMenu":
            print "Main Menu: " + evt.unicode
        elif self.state == "playing":
            print "Playing: " + evt.unicode
