"""
Jeu du Bonneteau (version simple)
==================================
Une balle est cachée sous l'un des gobelets numérotés.
Le joueur doit deviner sous lequel elle se trouve.
La position de la balle change entre chaque tentative.
"""

import random

NB_GOBELETS = 5
NB_VIES = 3


def demander_gobelet():
    """Demande un numéro de gobelet valide à l'utilisateur."""
    while True:
        try:
            choix = int(input(f"Choisissez un gobelet (1-{NB_GOBELETS}) : "))
            if 1 <= choix <= NB_GOBELETS:
                return choix
            print(f"Merci de choisir un nombre entre 1 et {NB_GOBELETS}.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def jouer():
    print("=" * 40)
    print("Bienvenue au BONNETEAU !")
    print(f"{NB_GOBELETS} gobelets, une balle cachée sous l'un d'eux.")
    print(f"Vous avez {NB_VIES} vies.")
    print("=" * 40)

    position_balle = random.randint(1, NB_GOBELETS)
    vies = NB_VIES
    manche = 1

    while vies > 0:
        print(f"\n--- Manche {manche} (vies restantes : {vies}) ---")
        print("On mélange les gobelets...")

        choix = demander_gobelet()

        if choix == position_balle:
            print("\n Bravo ! Vous avez trouvé la balle !")
            print(f"Vous avez gagné en {manche} manche(s).")
            return
        else:
            vies -= 1
            print(f" Perdu ! La balle n'était pas sous le gobelet {choix}.")
            if vies == 0:
                print(f"La balle était sous le gobelet {position_balle}.")
                print(" Plus de vies... Partie terminée !")
                return

        # Nouvelle position de la balle pour la manche suivante
        nouvelle_position = position_balle
        while nouvelle_position == position_balle:
            nouvelle_position = random.randint(1, NB_GOBELETS)
        position_balle = nouvelle_position
        manche += 1


def rejouer():
    reponse = input("\nVoulez-vous rejouer ? (o/n) : ").strip().lower()
    return reponse in ("o", "oui")


if __name__ == "__main__":
    continuer = True
    while continuer:
        jouer()
        continuer = rejouer()
    print("\nMerci d'avoir joué au Bonneteau !")