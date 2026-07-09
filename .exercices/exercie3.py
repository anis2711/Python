# Ce code permet de réaliser un jeu multijoueur en python
#Choix du nombre à trouver entre 0 et 100 (compris) pour le joueur 1
import random
nombre_a_trouver = random.randint(0, 100)
#Entre un nombre entre 0 et 100 (compris) pour le joueur 2
nombre_choisi = int(input("Joueur 2, entrez un nombre entre 0 et 100 (compris) : "))
# Le programme doit afficher 'TROP BAS' et redemander le nombre si jamais celui-ci est plus grand que le nombre choisi par l'utilisateur 1
while nombre_choisi != nombre_a_trouver:
    if nombre_choisi < nombre_a_trouver:
        print("TROP BAS")
    else:
        print("TROP HAUT")
    nombre_choisi = int(input("Joueur 2, entrez un nombre entre 0 et 100 (compris) : "))
    