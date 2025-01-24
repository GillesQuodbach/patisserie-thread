import threading
import time

from ingredient import Ingredient


class Verseur(threading.Thread):
    def __init__(self, nom, source, destination, rythme):
        """
        Initialise le verseur.
        :param nom: Nom du commis verseur.
        :param source: Récipient source contenant l'ingrédient à verser.
        :param destination: Récipient cible où verser l'ingrédient.
        :param rythme: Temps de pause entre chaque étape de versement.
        """
        threading.Thread.__init__(self)
        self.nom = nom
        self.source = source
        self.destination = destination
        self.rythme = rythme
        self.total_verse = 0

    def run(self):
        if not self.source.contenu or self.source.contenu.quantite == 0:
            print(f"{self.nom}: Le {self.source.type_recipient} est vide, rien à verser!")
            return

        print(
            f"{self.nom}: Je commence à verser le contenu du {self.source.type_recipient} vers le {self.destination.type_recipient}.")

        # Simuler le versement en plusieurs étapes
        quantite_a_verser_par_etape = self.source.contenu.quantite / 5
        for i in range(1, 6):  # Simulation de 5 étapes de versement
            print(f"{self.nom}: Versement étape {i}/5...")
            time.sleep(0.1)

            #si la quantité restant est trop petit
            if self.source.contenu.quantite >= quantite_a_verser_par_etape:
                self.source.contenu.quantite -= quantite_a_verser_par_etape
                #On verse l'ingredient dans le recipient final
                self.destination.ajouter_contenu(Ingredient(self.source.contenu.nom, quantite_a_verser_par_etape, self.source.contenu.unite))
                self.total_verse += quantite_a_verser_par_etape
                print(
                    f"{self.nom}: {quantite_a_verser_par_etape} {self.source.contenu.unite} de {self.source.contenu.nom} ajouté dans le {self.destination.type_recipient}.")

            else:
                # Si la quantité restante est inférieure à ce qu'on devait verser, on verse le reste
                self.destination.ajouter_contenu(
                    Ingredient(self.source.contenu.nom, self.source.contenu.quantite, self.source.contenu.unite))
                self.total_verse += self.source.contenu.quantite  # Ajouter la quantité restante
                print(
                    f"{self.nom}: {self.source.contenu.quantite} {self.source.contenu.unite} restants ajoutés dans le {self.destination.type_recipient}.")
                self.source.contenu.quantite = 0
                break

        print(f"{self.nom}: Versement terminé. Le contenu est maintenant dans le {self.destination.type_recipient}.")

        # Afficher la quantité totale versée dans le récipient destination
        print(
            f"{self.nom}: Quantité totale versée dans le {self.destination.type_recipient}: {self.total_verse} {self.source.contenu.unite} de {self.source.contenu.nom}.")

