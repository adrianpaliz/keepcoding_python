import pygame, sys, random


class Competitor:
    '''
    __players_info is a list of tuples.
    The elements of each tuple is:
        (<Competitor Name>, <Start Position>, <Costume>)
    '''
    __players_info = [
        ("Percanta", "turtle"),
        ("Tarzan", "fish"),
        ("Inty", "prawn"),
        ("Chimborazo", "octopus"),
    ]

    __start_positions = [160, 200, 240, 280]

    def __init__(self, x_axis=0, y_axis=0):
        choice = random.choice(self.__players_info)
        self.__players_info.remove(choice)

        self.costume = pygame.image.load(
            "images/{}.png".format(choice[1])
        )

        start_position = random.choice(self.__start_positions)
        self.__start_positions.remove(start_position)

        self.position = [x_axis, y_axis or start_position]
        self.name = choice[0]

    def move_forward(self):
        self.position[0] += random.random() * 3


class Game:
    competitors = []
    num_competitors = 4
    __start_line = 5
    __finish_line = 620
    screen_width = 640
    screen_height = 480

    def __init__(self):
        self.__screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Animal race.")

        self.competitors = [Competitor(self.__start_line) for competitor in range(self.num_competitors)]

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
