from Modele.Joueur import Joueur
from Modele.Paquet import Paquet
from Modele.Defausse import Defausse


class Game:
    # Constantes
    NOMBRE_CARTE_DEPART = 5
    SCORE_MAX = 100

    joueurs: [Joueur]
    joueur_courant: [Joueur]
    paquet: Paquet
    defausse: Defausse

    def start(self, nb_joueur: int):
        if nb_joueur > 10:
            print("Trop de joueur ... ")
            return

        # création des joueurs
        self.joueurs = []
        noms_joueurs = []
        for j in range(nb_joueur):
            noms_joueurs.append(input("Quel est votre nom de joueur"))
        for nom_j in noms_joueurs:
            self.joueurs.append(Joueur(nom_j))

        # création de la table
        self.paquet = Paquet()
        self.paquet.melanger()
        carte_depart = self.paquet.tire()
        self.defausse = Defausse()
        self.defausse.poser(carte_depart)

        # distribution des 5 cartes de départ
        for k in range(self.NOMBRE_CARTE_DEPART):
            for j in self.joueurs:
                j.piocher(self.paquet)

        # Tour des joueurs
        while not self.es_la_fin():
            for j in self.joueurs:
                if j.jouer(self.paquet):
                    break

    def end(self):  # TODO
        pass

    def es_la_fin(self) -> bool:
        for j in self.joueurs:
            if j.score > self.SCORE_MAX:
                return True
        return False
