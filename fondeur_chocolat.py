import math
import time
from ingredient import Chocolat
from commis import Commis


class FondeurChocolat(Commis):
    def __init__(self, nom, recipient):
        super().__init__(nom)
        self.recipient = recipient  # en grammes

    def run(self):
        if not self.recipient.contenu:
            print(f"{self.nom}: Le {self.recipient.type_recipient} est vide, rien à fondre")
            return

        if not isinstance(self.recipient.contenu, Chocolat):
            print(f"{self.nom}: Je ne peux que fondre du chocolat")
            return

        print(f"{self.nom}: Je mets de l'eau à chauffer dans une bouilloire.")
        time.sleep(8)
        print(f"{self.nom}: Je mets de l'eau dans une casserole")
        time.sleep(2)
        print(f"{self.nom}: J'y pose le bol rempli de chocolat dans le {self.recipient.type_recipient}.")
        time.sleep(1)
        nb_tours = self.recipient.contenu.quantite // 10
        for no_tour in range(1, nb_tours + 1):
            print(f"{self.nom}: Je mélange {self.recipient.contenu} dans le {self.recipient.type_recipient}, tour n°{no_tour}")
            time.sleep(1)
