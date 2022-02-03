import pygame, sys, random
from pygame.locals import *


class Competitor:
    __costumes = ("turtle", "fish", "prawn", "moray", "octopus")

    def __init__(self, x_axis=0, y_axis=0):
        costume_index = random.randint(0, 4)

        self.costume = pygame.image.load(
            "images/{}.png".format(self.__costumes[costume_index])
        )
        self.position = [x_axis, y_axis]
        self.name = ""


class Game:
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Animal race.")

        self.competitor = Competitor(320, 240)

    def start(self):
        here_is_a_winner = False
        while not here_is_a_winner:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.competitor.position[1] -= 5
                    elif event.key == K_DOWN:
                        self.competitor.position[1] += 5
                    elif event.key == K_LEFT:
                        self.competitor.position[0] -= 5
                    elif event.key == K_RIGHT:
                        self.competitor.position[0] += 5
                    else:
                        pass

            self.__screen.blit(self.__background, (0, 0))
            self.__screen.blit(self.competitor.costume, self.competitor.position)

            pygame.display.flip()


print("My name is{}.".format(__name__))

if __name__ == "__main__":
    script = Game()
    pygame.init()
    script.start()
