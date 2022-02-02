import pygame, sys, random


class Competitor:
    def __init__(self, x_axis=0, y_axis=0):
        self.costume = pygame.image.load("images/turtle.png")
        self.position = [x_axis, y_axis]
        self.name = "Turtle"

    def move_forward(self):
        self.position[0] += random.randint(1, 6)


class Game:
    competitors = []
    __start_line = 5
    __finish_line = 620

    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Animal race.")

        first_competitor = Competitor(self.__start_line, 240)
        first_competitor.name = "Chimborazo"
        self.competitors.append(first_competitor)

    def compete(self):
        there_is_a_winner = False
        while not there_is_a_winner:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    there_is_a_winner = True

            self.competitors[0].move_forward()

            if self.competitors[0].position[0] >= self.__finish_line:
                print("{} has won the race.".format(self.competitors[0].name))
                there_is_a_winner = True

            self.__screen.blit(self.__background, (0, 0))
            self.__screen.blit(
                self.competitors[0].costume, self.competitors[0].position
            )

            pygame.display.flip()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    script = Game()
    pygame.init()
    script.compete()
