import threading


class Ingredient(threading.Thread):
    def __init__(self, name, quantity, unit):
        threading.Thread.__init__(self)
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def run(self):
        name = self.name
        quantity = self.quantity
        unit = self.unit
        print(f"\t J'ajoute {quantity}{unit} de {name}")


class Oeuf(Ingredient):
    def __init__(self, quantity):
        super().__init__("Oeuf", quantity, "pièces")


class Chocolat(Ingredient):
    def __init__(self, quantity):
        super().__init__("Chocolat", quantity, "grammes")
