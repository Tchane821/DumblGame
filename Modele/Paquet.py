from Modele.Carte import Carte
from Modele.Valeur import Valeur
from Modele.Couleur import Couleur
import random as pif


class Paquet:
    les_cartes: [Carte]

    def __init__(self):
        self.les_cartes = []
        for c in range(1, 5):
            for v in range(13):
                self.les_cartes.append(Carte(Valeur(v), Couleur(c)))

    def tire(self):
        if len(self.les_cartes) > 0:
            return self.les_cartes.pop()
        else:
            return None

    def melanger(self):
        pif.shuffle(self.les_cartes)
