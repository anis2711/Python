# Realiser un jeu de mystere en python
"""Jeux de mystère en python
Ce code permet de réaliser un jeu multijoueur en python"""

# Ce code permet de réaliser un jeu multijoueur en python
#Choix du nombre à trouver entre 0 et 100 (compris) pour le joueur UN
choix_nombre = int(input("Joueur UN, choisissez un nombre entre 0 et 100 (compris) : "))

#Entrer un nombre pour le joueur deux
Entrer_nombre = int(input("Joueur DEUX, entrez un nombre entre 0 et 100 (compris) : "))

# Le programme devra afficher 'TROP BAS' et redemander le nombre si jamais celui-ci est plus petit que le nombre choisi par le joueur UN.
while Entrer_nombre < choix_nombre:
    print("TROP BAS")
    Entrer_nombre = int(input("Joueur DEUX, entrez un nombre entre 0 et 100 (compris) : "))

    # Le programme devra afficher 'TROP HAUT' et redemander le nombre si jamais celui-ci est plus grand que le nombre choisi par le joueur UN.
while Entrer_nombre > choix_nombre:
    print("TROP HAUT")
    Entrer_nombre = int(input("Joueur DEUX, entrez un nombre entre 0 et 100 (compris) : "))

    #Le programme devra afficher 'FELICITATION' si jamais le nombre entré par le joueur DEUX est égal au nombre choisi par le joueur UN.
if Entrer_nombre == choix_nombre:
    print("FELICITATION ! Vous avez trouvé le nombre choisi par le joueur UN.")
    





    