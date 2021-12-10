class Pet:
    def __init__(self, edate, exdate, price, food):
        self.entrydate = edate
        self.exitdate = exdate
        self.price = price
        self.food = food

    def printname(self):
        print(self.entrydate, self.exitdate, self.price, self.food)

