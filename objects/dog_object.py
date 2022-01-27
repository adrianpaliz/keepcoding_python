class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight >= 8:
            print("GUAU GUAU")
        else:
            print("guau, guau")

    def __str__(self):
        return "Dog name {}, age: {}, weight: {}.".format(self.name, self.age, self.weight)
