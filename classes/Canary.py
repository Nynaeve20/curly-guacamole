from classes.Bird import Bird

class Canary(Bird):
    def __init__(self, edate, exdate, price, food):
        super().__init__(edate, exdate, price, food)

    def printname(self):
        print("--------------------------")
        print("Este es un Canario")
        print("Fecha de entrada:" ,self.entrydate, "Fecha de salida:" , self.exitdate, "Precio:", self.price, "Comida:", self.food)