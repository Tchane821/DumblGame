from Vue.Terminal import print_choix_dumble_or_next


# 0 dum / 1 next
def choix_de_jeu() -> int:
    reponse_user = print_choix_dumble_or_next()
    while reponse_user not in [0, 1]:
        print("Erreur de saisie, recomencer...")
        reponse_user = print_choix_dumble_or_next()
    return reponse_user

