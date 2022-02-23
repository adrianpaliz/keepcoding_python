import pygame, sys
from pygame.locals import *

class Thermometer:
    def __init__(self):
        self.interface = pygame.image.load("images/thermometer.png")

    def convert(self, degree, to_scale):
        result = 0
        if to_scale == 'F':
            result = degree * 9 / 5 + 32
        elif to_scale == 'C':
            result = (degree - 32) * 5 / 9
        else:
            result = degree
        return "{:10.2f}".format(result)


class Selector:
    __temperature_scale = None

    def __init__(self, scale = "C"):
        self.__switch_skin = []
        self.__switch_skin.append(pygame.image.load("images/degree_fahrenheit.png"))
        self.__switch_skin.append(pygame.image.load("images/degree_celsius.png"))

        self.__temperature_scale = scale

    def switch_skin_changer(self):
        if self.__temperature_scale == 'F':
            return self.__switch_skin[0]
        else:
            return self.__switch_skin[1]

    def scale_change(self):
        if self.__temperature_scale == 'F':
            self.__temperature_scale = 'C'
        else:
            self.__temperature_scale = 'F'

    def scale(self):
        return self.__temperature_scale

class NumberInput:
    __value = 0
    __string_value = ""
    __position = [0, 0]
    __size = [0, 0]
    __dots_count = 0

    def __init__(self, value = 0):
        self.__font = pygame.font.SysFont("Arial", 24)

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__string_value) < 10 or (event.unicode == '.' and self.__dots_count ==0):
                self.__string_value += event.unicode
                self.value(self.__string_value)
                if event.unicode == '.':
                    self.__dots_count += 1
            elif event.key == K_BACKSPACE:
                if self.__string_value[-1] == '.':
                    self.__dots_count -= 1
                self.__string_value = self.__string_value[0 : -1]
                self.value(self.__string_value)

    def render(self):
        text_block = self.__font.render(self.__string_value, True, (74, 74, 74))
        rectangle = text_block.get_rect()
        rectangle.left = self.__position[0]
        rectangle.top = self.__position[1]
        rectangle.size = self.__size

        return (rectangle, text_block)

    def value(self, entered_value = None):
        if entered_value == None:
            return self.__value
        else:
            entered_value = str(entered_value)
            try:
                self.__value = float(entered_value)
                self.__string_value = entered_value
                if '.' in self.__string_value:
                    self.__dots_count = 1
                else:
                    self.__dots_count = 0
            except:
                pass

    def width(self, entered_value = None):
        if entered_value == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(entered_value)
            except:
                pass

    def height(self, entered_value = None):
        if entered_value == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(entered_value)
            except:
                pass

    def size(self, entered_value = None):
        if entered_value == None:
            return self.__size
        else:
            try:
                self.__size = [int(entered_value[0]), int(entered_value[1])]
            except:
                pass

    def x_axis(self, entered_value = None):
        if entered_value == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(entered_value)
            except:
                pass

    def y_axis(self, entered_value = None):
        if entered_value == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(entered_value)
            except:
                pass

    def coordinate_point(self, entered_value = None):
        if entered_value == None:
            return self.__position
        else:
            try:
                self.__position = [int(entered_value[0]), int(entered_value[1])]
            except:
                pass

class MainProcess:
    thermometer = None
    user_input = None
    selector = None

    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Thermometer")


        self.thermometer = Thermometer()
        self.user_input = NumberInput(0)
        self.user_input.coordinate_point((106, 58))
        self.user_input.size((133, 28))

        self.selector = Selector()


    def __close(self):
        pygame.quit()
        sys.exit()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__close()

                self.user_input.on_event(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.scale_change()
                    degree = self.user_input.value()
                    new_scale = self.selector.scale()

                    temperature = self.thermometer.convert(degree, new_scale)
                    self.user_input.value(temperature)

            # We draw the screen background.
            self.__screen.fill((244, 236, 203))

            # We draw the thermometer on his position.
            self.__screen.blit(self.thermometer.interface, (50, 34))

            # We draw the text box.
            text = self.user_input.render() # We obtain the white rectangle and text draw and we assing them to "text".
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0]) # We created the white rectangle with his data (position and size).
            self.__screen.blit(text[1], self.user_input.coordinate_point()) # We locate the text drew.

            # We draw the selector.
            self.__screen.blit(self.selector.switch_skin_changer(), (112, 153))

            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    script = MainProcess()
    script.start()
