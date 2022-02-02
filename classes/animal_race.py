import turtle, random


class Race_track:
    competitors = []
    __start_position_y_axis = (-30, -10, 10, 30)
    __turtle_color = ("red", "blue", "green", "orange")

    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        self.__start_line = -width / 2 + 20
        self.__finish_line = width / 2 - 20

        self.__create_competitors()

    def __create_competitors(self):
        for competitor in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__turtle_color[competitor])
            new_turtle.shape("turtle")
            new_turtle.penup()
            new_turtle.setposition(
                self.__start_line, self.__start_position_y_axis[competitor]
            )

            self.competitors.append(new_turtle)

    def compete(self):
        there_is_a_winner = False

        # While loop for iteration that make each competitor move forward.
        while not there_is_a_winner:
            for competitor in self.competitors:
                move_forward = random.randint(1, 6)
                competitor.forward(move_forward)

                # If statement that check if the competitor is on the finish line.
                if competitor.position()[0] >= self.__finish_line:
                    there_is_a_winner = True
                    print("The {} turtle is the winner.".format(competitor.color()[0]))
                    break


if __name__ == "__main__":
    script = Race_track(640, 480)
    script.compete()
