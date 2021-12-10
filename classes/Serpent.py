from classes.Reptile import Reptile

class Serpent(Reptile):
    def __init__(self, edate, exdate, price, food, name):
        super().__init__(edate, exdate, price, food, name)

    def printname(self):
        print("--------------------------")
        print("Esto es una serpiente")
        print("Nombre:", self.name, "Fecha de entrada:" ,self.entrydate, "Fecha de salida:" , self.exitdate, "Precio:", self.price, "Comida:", self.food)