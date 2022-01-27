class Another_dog():
    def __init__(self):
        self.name = ""
        self.age = None
        self.weight = None

    def bark(self):
        if self.weight == None:
            print("I'm a gosht.")

        if self.weight >= 8:
            print("GUAU, GUAU.")
        else:
            print("guau, guau.")

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight >= 8:
            print("GUAU, GUAU.")
        else:
            print("guau, guau.")

    def __str__(self):
        return "Dog name {}, age: {}, weight: {}.".format(self.name, self.age, self.weight)

class Assistance_dog(Dog):
    def __init__(self, name, age, weight, owner):
        Dog.__init__(self, name, age, weight)
        self.owner = owner
        self.__working = False

    def __str__(self):
        return "Assistance dog of {}.".format(self.owner)

    def walk(self):
        print("OK, I {} help my owner, {} to walk".format(self.name, self.owner))

    def bark(self):
        if self.__working:
            print("Shhhh, I can't bark")
        else:
            Dog.bark(self)

    def working(self, value = None):
        if value == None:
            return self.__working
        else:
            self.__working = value
