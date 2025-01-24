class Recipient:
    def __init__(self, type_recipient, contenu=None):
        """
        Initialise le récipient avec un type et éventuellement un contenu (ingrédient ou appareil).
        :param type_recipient: Nom du récipient (ex: "Cul de poule")
        :param contenu: Un ingrédient ou un appareil
        """
        self.type_recipient = type_recipient
        self.contenu = contenu

    def ajouter_contenu(self, contenu):
        """Ajoute un contenu (ingredient ou appareil) au recipient."""
        self.contenu = contenu
        print(f"{contenu} ajouté dans le {self.type_recipient}")

    def afficher_contenu(self):
        """Affiche le contenu du récipient."""
        if self.contenu:
            print(f"{self.type_recipient} contient: {self.contenu}")
        else:
            print(f"Le {self.type_recipient} est vide")
    def ajouter(self, quantite):
        if hasattr(self.contenu, 'quantite'):
            self.contenu.quantite += quantite
        else:
            raise TypeError("Impossible d'ajouter une quantité à ce type d'ingrédient.")