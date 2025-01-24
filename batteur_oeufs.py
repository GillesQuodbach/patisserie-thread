import time
from ingredient import Oeuf


from commis import Commis


class BatteurOeufs(Commis):
    def __init__(self, nom, recipient):
        super().__init__(nom)
        self.recipient = recipient

    def run(self):
        if not self.recipient.contenu:
            print(f"{self.nom}: Le {self.recipient.type_recipient} est vide, rien à battre")
            return

        if not isinstance(self.recipient.contenu, Oeuf):
            print(f"{self.nom}: Je peux battre uniquement des oeufs")
            return

        nb_tours = self.recipient.contenu.quantite * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"\t{self.nom}: Je bats {self.recipient.contenu} dans le {self.recipient.type_recipient}, tour n°{no_tour}")
            time.sleep(0.5)  # temps supposé d'un tour de batteur
