from Modele.Couleur import Couleur
from Modele.Valeur import Valeur


class Carte:
    valeur: Valeur
    couleur: Couleur

    def __init__(self, valeur: Valeur, couleur: Couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self) -> str:
        return f"{self.valeur.name} - {self.couleur.name}"
