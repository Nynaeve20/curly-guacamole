from classes.Pet import Pet

class Mammal(Pet):
    def __init__(self, edate, exdate, price, food, name, breed):
        super().__init__(edate, exdate, price, food)
        self.name = name
        self.breed = breed

    