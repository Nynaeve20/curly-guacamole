from classes.Pet import Pet

class Bird(Pet):
    def __init__(self, edate, exdate, price, food):
        super().__init__(edate, exdate, price, food)