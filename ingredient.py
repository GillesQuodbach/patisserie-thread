from abc import ABC


class Ingredient(ABC):
    def __init__(self, nom, quantite, unite):
        self.nom = nom
        self.quantite = quantite
        self.unite = unite

    def __str__(self):
        return f"{self.quantite} {self.unite} de {self.nom}"


class Oeuf(Ingredient):
    def __init__(self, quantite):
        super().__init__("Oeuf", quantite, "")


class Chocolat(Ingredient):
    def __init__(self, quantite):
        super().__init__("Chocolat", quantite, "g")
