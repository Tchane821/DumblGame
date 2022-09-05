from Modele.Carte import Carte
from Modele.Paquet import Paquet


class Defausse(Paquet):

    def poser(self, carte: Carte):
        self.les_cartes.append(carte)
