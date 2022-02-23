import pygame, sys
from pygame.locals import *

class MainProcess:
    thermometer = None
    user_input = None
    selector = None

    def __init__(self):
        # Instance for screen set up
        self.__screen = pygame.display.set_mode((290, 415))
        # Set up window title
        pygame.display.set_caption("Thermometer")
        # windows color
        self.__screen.fill((244, 236, 203))

    def __close(self):
       pygame.quit()
       sys.exit()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__close()
            # Update the contents of the entire display
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    script = MainProcess()
    script.start()
