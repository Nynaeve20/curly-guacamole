from classes.Mammal import Mammal

class Dog(Mammal):
    def __init__(self, edate, exdate, price, food, name, breed):
        super().__init__(edate, exdate, price, food, name, breed)

    def printname(self):
        print("--------------------------")
        print("Este es un perro")
        print("Nombre:", self.name, "Raza:" , self.breed, "Fecha de entrada:" ,self.entrydate, "Fecha de salida:" , self.exitdate, "Precio:", self.price, "Comida:", self.food)