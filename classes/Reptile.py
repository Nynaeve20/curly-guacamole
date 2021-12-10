from classes.Pet import Pet

class Reptile(Pet):
    def __init__(self, edate, exdate, price, food, name):
        super().__init__(edate, exdate, price, food)
        self.name = name