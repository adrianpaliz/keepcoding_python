import pygame, sys, random


class Competitor:
    __costumes = ("turtle", "fish", "prawn", "moray", "octopus")

    def __init__(self, x_axis=0, y_axis=0):
        costume_index = random.randint(0, 4)

        self.costume = pygame.image.load(
            "images/{}.png".format(self.__costumes[costume_index])
        )
        self.position = [x_axis, y_axis]
        self.name = ""

    def move_forward(self):
        self.position[0] += random.randint(1, 6)


class Game:
    competitors = []
    __start_position_y_axis = (160, 200, 240, 280)
    __names = ("Percanta", "Tarzan", "Inty", "Chimborazo")
    __start_line = 5
    __finish_line = 620

    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Animal race.")

        for chosen_one in range(4):
            competitor = Competitor(
                self.__start_line, self.__start_position_y_axis[chosen_one]
            )
            competitor.name = self.__names[chosen_one]
            self.competitors.append(competitor)

    def close(self):
        pygame.quit()
        sys.exit()

    def compete(self):
        there_is_a_winner = False
        while not there_is_a_winner:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    there_is_a_winner = True

            for competitor in self.competitors:
                competitor.move_forward()
                if competitor.position[0] >= self.__finish_line:
                    print("{} has won the race.".format(competitor.name))
                    there_is_a_winner = True

            self.__screen.blit(self.__background, (0, 0))

            for competitor in self.competitors:
                self.__screen.blit(competitor.costume, competitor.position)

            pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()


if __name__ == "__main__":
    script = Game()
    pygame.init()
    script.compete()
