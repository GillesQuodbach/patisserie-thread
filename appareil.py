import threading
from ingredient import Ingredient

class Appareil(threading.Thread):
    def __init__(self, ingredients: list[Ingredient]):
        threading.Thread.__init__(self)
        self.ingredients = ingredients

    def run(self):
        print("Préparation de l'appareil...")
        threads = []

        for ingredient in self.ingredients:
            ingredient.start()
            threads.append(ingredient)

        for thread in threads:
            thread.join()

        print("L'appareil est prêt !")
