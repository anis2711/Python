"""
Programme de commande de nourriture - Version très simple (3 articles)
---------------------------------------------------------------------------
"""

# Affiche un message d'accueil pour l'utilisateur
print("=== Bienvenue dans le programme de commande de nourriture ===")

# Définition des prix de chaque article
prix_eau = 1.00
prix_sandwitch = 4.50
prix_boisson = 2.00

# Demande à l'utilisateur combien d'argent il a dans son porte-monnaie
porte_monnaie = float(input("Combien d'argent avez-vous dans votre porte-monnaie (€) ? "))

# Initialise le total de la commande et les quantités de chaque article
total_commande = 0.0
qte_eau = 0
qte_sandwitch = 0
qte_boisson = 0

# Affiche le solde disponible avant de commencer les achats
print("")
print("Solde disponible :", porte_monnaie, "€")

# --- Boucle principale de sélection d'articles ---
# L'utilisateur peut ajouter des articles jusqu'à ce qu'il choisisse de valider
while True:
    print("")
    print("--- MENU ---")
    print("1. Eau       -", prix_eau, "€")
    print("2. Sandwitch -", prix_sandwitch, "€")
    print("3. Boisson   -", prix_boisson, "€")
    print("q. Valider la commande")
    print("------------")

    choix = input("Choisissez un article (numéro) ou 'q' pour valider : ")

    match choix:
        case "q":
            # Quitte la boucle et passe au récapitulatif
            break

        case "1":
            # Ajoute une eau si l'utilisateur a assez d'argent
            if total_commande + prix_eau > porte_monnaie:
                print(" Vous n'avez pas assez d'argent pour ajouter Eau")
            else:
                total_commande = total_commande + prix_eau
                qte_eau = qte_eau + 1
                print(" Eau ajouté au panier")
                print("Total du panier actuel :", total_commande, "€")
                print("Solde restant si vous validez maintenant :", porte_monnaie - total_commande, "€")

        case "2":
            # Ajoute un sandwitch si l'utilisateur a assez d'argent
            if total_commande + prix_sandwitch > porte_monnaie:
                print(" Vous n'avez pas assez d'argent pour ajouter Sandwitch")
            else:
                total_commande = total_commande + prix_sandwitch
                qte_sandwitch = qte_sandwitch + 1
                print(" Sandwitch ajouté au panier")
                print("Total du panier actuel :", total_commande, "€")
                print("Solde restant si vous validez maintenant :", porte_monnaie - total_commande, "€")

        case "3":
            # Ajoute une boisson si l'utilisateur a assez d'argent
            if total_commande + prix_boisson > porte_monnaie:
                print(" Vous n'avez pas assez d'argent pour ajouter Boisson")
            else:
                total_commande = total_commande + prix_boisson
                qte_boisson = qte_boisson + 1
                print(" Boisson ajouté au panier")
                print("Total du panier actuel :", total_commande, "€")
                print("Solde restant si vous validez maintenant :", porte_monnaie - total_commande, "€")

        case _:
            # Gère les entrées incorrectes
            print(" Choix invalide, veuillez réessayer.")

# --- Récapitulatif final de la commande ---
print("")
print("=== Récapitulatif de la commande ===")

if total_commande == 0:
    # Si aucun article n'a été ajouté, informer l'utilisateur
    print("Votre panier est vide.")
else:
    # Affiche la quantité et le coût de chaque article acheté
    if qte_eau > 0:
        print("Eau       x", qte_eau, "=", qte_eau * prix_eau, "€")
    if qte_sandwitch > 0:
        print("Sandwitch x", qte_sandwitch, "=", qte_sandwitch * prix_sandwitch, "€")
    if qte_boisson > 0:
        print("Boisson   x", qte_boisson, "=", qte_boisson * prix_boisson, "€")

    print("-------------------------------------")
    print("TOTAL A PAYER :", total_commande, "€")

    # Demande la confirmation finale de l'achat
    confirmation = input("Voulez-vous valider cette commande ? (o/n) : ").strip().lower()

    match confirmation:
        case "o":
            # Si l'utilisateur confirme, on soustrait le total du porte-monnaie
            porte_monnaie = porte_monnaie - total_commande
            print(" Commande validée ! Merci pour votre achat.")
            print("Nouveau solde de votre porte-monnaie :", porte_monnaie, "€")
        case _:
            # Annule la commande si l'utilisateur ne confirme pas
            print(" Commande annulée. Votre solde reste inchangé.")

print("")
print("Merci de votre visite ! Au revoir !")


