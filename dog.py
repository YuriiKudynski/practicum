class Dog:
    mammal = True
    nature = "Loyal"
    breed = "Unknown"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Dog - {self.name}. Age - {self.age}"

    def golos(self):
        print(f"{self.name} say HAW")


class Beagle(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.breed = "Beagle"
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.breed} -> {self.name} -> {self.age}"


class Terrier(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.breed = "Terrier"
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.breed} -> {self.name} -> {self.age}"


class HouseDog(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.breed = "HouseDog"
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.breed} -> {self.name} -> {self.age}"