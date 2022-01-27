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
        self.working = False

    def __str__(self):
        return "Dog name {}, is a assistance dog of {}.".format(self.name, self.owner)

    def walk(self):
        print("OK, I {} help my owner, {} to walk".format(self.name, self.owner))

    def bark(self):
        if self.working:
            print("Shhhh, I can't bark")
        else:
            Dog.bark(self)
