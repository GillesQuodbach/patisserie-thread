from batteur_oeufs import BatteurOeufs
from fondeur_chocolat import FondeurChocolat
from ingredient import Oeuf, Chocolat
from recipient import Recipient
from verseur import Verseur

if __name__ == "__main__":
    # Création des ingrédients
    oeufs = Oeuf(6)
    chocolat1 = Chocolat(200)
    chocolat2 = Chocolat(150)

    # Création des récipients
    cul_de_poule = Recipient("Cul de poule", oeufs)
    saladier = Recipient("Saladier")
    bol_chocolat1 = Recipient("Bol en inox", chocolat1)
    bol_chocolat2 = Recipient("Saladier", chocolat2)

    # Création des commis fondeurs de chocolat et batteur
    batteur = BatteurOeufs("Paul", cul_de_poule)
    fondeur1 = FondeurChocolat("Julie", bol_chocolat1)
    fondeur2 = FondeurChocolat("Luc", bol_chocolat2)

    # Démarrage des fondeurs / batteurs
    batteur.start()
    fondeur1.start()
    fondeur2.start()

    # Attendre la fin de la fonte du chocolat
    batteur.join()
    fondeur1.join()
    fondeur2.join()


    print("\nLe chocolat est fondu, les oeufs sont battu, place aux verseurs.\n")
    # Créer des verseurs pour verser le chocolat dans le Cul de poule
    verseur_chocolat = Verseur("Leo", bol_chocolat1, saladier, 1)
    verseur_chocolat2 = Verseur("Leo", bol_chocolat2, saladier, 1)

    verseur_chocolat.start()
    verseur_chocolat2.start()

    verseur_chocolat.join()
    verseur_chocolat2.join()

    print(f"Quantité total dans le saladier: {saladier.contenu}")
    # # Création des verseurs pour incorporer le chocolat fondu dans les œufs
    # verseur1 = Verseur("Emma", bol_chocolat1, cul_de_poule_oeufs, rythme=0.1)
    # verseur2 = Verseur("Leo", bol_chocolat2, cul_de_poule_oeufs, rythme=0.1)
    #
    # # Démarrage des verseurs en parallèle
    # verseur1.start()
    # verseur2.start()
    #
    # # Attente de la fin du versement
    # verseur1.join()
    # verseur2.join()

    # print(f"\nQuantité finale dans le {cul_de_poule_oeufs.type_recipient}: {cul_de_poule_oeufs.contenu}")
    # print("\nL'appareil est prêt pour la cuisson.")