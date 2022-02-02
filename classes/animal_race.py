import pygame, sys


class Game:
    competitors = []
    __start_line = 20
    __finish_line = 620

    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Animal race.")

    def compete(self):
        there_is_a_winner = False

        while not there_is_a_winner:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    there_is_a_winner = True

            self.__screen.blit(self.__background, (0, 0))

            pygame.display.flip()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    script = Game()
    pygame.init()
    script.compete()
