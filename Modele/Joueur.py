from Modele.Carte import Carte
from Modele.Valeur import Valeur
from Modele.Paquet import Paquet
from Controleur.ControleurDeChoix import choix_de_jeu


class Joueur:
    nom: "" = ""
    main_joueur: [Carte] = []
    score: int = 0

    def __init__(self, nom):
        self.nom = nom

    # les action du joueur

    def jouer(self, paquet: Paquet) -> bool:
        # 0 dum / 1 next
        action = choix_de_jeu()
        if action == 0:
            self.dumble()
            return True
        else:
            self.piocher(paquet)
            self.poser()
        return False

    def piocher(self, paquet: Paquet, ):  # TODO
        # self.main_joueur.append(paquet.tire())
        # self.main_joueur.append(defauce[-1:])
        # defauce = defauce[:-1]
        pass

    def poser(self):  # TODO
        pass

    def dumble(self):  # TODO
        pass

    def valeur_main(self) -> int:
        val = 0
        for c in self.main_joueur:
            print(c, c.valeur.value)
            if c.valeur is Valeur.Joker:
                val -= 1
            elif c.valeur in [Valeur.Roi, Valeur.Dame, Valeur.Valet]:
                val += 10
            else:
                val += c.valeur.value
        return val
