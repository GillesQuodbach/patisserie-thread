class Appareil:
    def __init__(self, nom):
        self.nom = nom
        self.ingredients = []

    def ajouter_ingredient(self, ingredient):
        """Ajoute un ingredient à l'appareil"""
        self.ingredients.append(ingredient)
        print(f"{ingredient} ajouté à l'appareil {self.nom}")

    def afficher_ingredients(self):
        """Affiche la liste des ingredients de l'appareil"""
        if not self.ingredients:
            print(f"L'appareil {self.nom} est vide.")
        else:
            print(f"Composition de l'appareil {self.nom}:")
            for ingredient in self.ingredients:
                print(f"- {ingredient}")

    def est_pret(self):
        """Vérifie si l'appareil contient des ingredients et est prêt"""
        return len(self.ingredients) > 0
    