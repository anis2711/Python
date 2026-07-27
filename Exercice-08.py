# Liste des animaux
animaux = [
    {"nom": "Mimi", "type": "Chat", "age": 2, "adopte": False},
    {"nom": "Rex", "type": "Chien", "age": 5, "adopte": True},
    {"nom": "Nino", "type": "Rongeur", "age": 1, "adopte": False}
]

# -----------------------------
# Fonctions
# -----------------------------

def afficher_animaux():
    print("\nListe des animaux")
    print("-" * 45)
    print(f"{'N°':<3} {'Nom':<10} {'Type':<10} {'Age':<5} {'Adopté'}")

    for i, animal in enumerate(animaux):
        statut = "Oui" if animal["adopte"] else "Non"
        print(f"{i:<3} {animal['nom']:<10} {animal['type']:<10} {animal['age']:<5} {statut}")


def inventaire():
    compteur = {}

    for animal in animaux:
        espece = animal["type"]

        if espece in compteur:
            compteur[espece] += 1
        else:
            compteur[espece] = 1

    print("\nInventaire des espèces")
    for espece, nombre in compteur.items():
        print(f"{espece} : {nombre}")


def ajouter_animal():
    nom = input("Nom : ")
    type_animal = input("Type : ")
    age = int(input("Age : "))

    animal = {
        "nom": nom,
        "type": type_animal,
        "age": age,
        "adopte": False
    }

    animaux.append(animal)
    print("Animal ajouté.")


def supprimer_animal():
    afficher_animaux()
    indice = int(input("Numéro de l'animal à supprimer : "))

    if 0 <= indice < len(animaux):
        animaux.pop(indice)
        print("Animal supprimé.")
    else:
        print("Numéro invalide.")


def changer_statut():
    afficher_animaux()
    indice = int(input("Numéro de l'animal : "))

    if 0 <= indice < len(animaux):
        animaux[indice]["adopte"] = not animaux[indice]["adopte"]
        print("Statut modifié.")
    else:
        print("Numéro invalide.")


# -----------------------------
# Programme principal
# -----------------------------

choix = -1

while choix != 0:

    print("""
=== MENU PRINCIPAL ===
1. Voir les animaux
2. Faire l'inventaire des espèces animales
3. Ajouter un animal
4. Retirer un animal
5. Changer le statut d'adoption d'un animal
0. Quitter
""")

    choix = int(input("Votre choix : "))

    if choix == 1:
        afficher_animaux()

    elif choix == 2:
        inventaire()

    elif choix == 3:
        ajouter_animal()

    elif choix == 4:
        supprimer_animal()

    elif choix == 5:
        changer_statut()

    elif choix == 0:
        print("Au revoir !")

    else:
        print("Choix invalide.")