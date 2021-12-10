from classes.Dog import Dog
from classes.Cat import Cat
from classes.Iguana import Iguana
from classes.Serpent import Serpent
from classes.Canary import Canary
from classes.Parakeet import Parakeet

if __name__ == "__main__":

    dog = Dog("10-12-2021", "24-12-2021", 1234.56, "Dog Chow", "Rocco", "Schnauzer")
    dog.printname()

    cat = Cat("11-11-2000", "11-11-2001", 225.69, "Pescado", "Small Cat", "Persian Cat")
    cat.printname()

    iguana = Iguana("12-08-1996", "12-09-1996", 300.05, "Hojas", "Felix")
    iguana.printname()

    serpent = Serpent("15-04-1998", "18-08-1999", 50000.00, "Personas", "Python")
    serpent.printname()

    canary = Canary("12-12-2012", "13-01-2013", 25.99, "Semillas")
    canary.printname()

    canary = Parakeet("01-01-2001", "02-02-2002", 25.99, "Papas Dulces")
    canary.printname()