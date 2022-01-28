class Thermometer():
    def __init__(self):
        self.__temperature_scale = 'celsius'
        self.__degree = 0

    def __str__(self):
        return "{}° {}".format(self.__degree, self.__temperature_scale)

    def getter_temperature_scale(self, getter_temperature_scale = None):
        if getter_temperature_scale == None:
            return self.__temperature_scale
        else:
            if getter_temperature_scale == 'fahrenheit' or getter_temperature_scale == 'celsius':
                self.__temperature_scale = getter_temperature_scale

    def setter_temperature_convert(self, degree = None):
        if degree == None:
            return self.__degree
        else:
            self.__degree = degree

    def __converter(self, degree, scale):
        if scale == 'celsius':
            return "{}° Fahrenheit".format(degree * 9 / 5 + 32)
        elif scale == 'fahrenheit':
            return "{}° Celsius".format((degree - 32) * 5 / 9)
        else:
            return "Wrong scale."

    def measures(self, getter_temperature_scale = None):
        if getter_temperature_scale == None or getter_temperature_scale == self.__temperature_scale:
            return self.__str__()
        else:
            if getter_temperature_scale == 'fahrenheit' or getter_temperature_scale == 'celsius':
                return self.__converter(self.__degree, self.__temperature_scale)
            else:
                return self.__str__()
