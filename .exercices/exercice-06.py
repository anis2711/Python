import random

# Liste de mots disponibles
mots = ["python", "programmation", "ordinateur", "algorithme", "variable", "fonction", "internet", "informatique"]

def afficher_etat(mot_secret, lettres_trouvees, lettres_essayees, vies):
    """Affiche l'état actuel du jeu"""
    print("\n" + "="*50)
    print(f"Nombre de vies restantes: {vies}")
    
    # Affiche les lettres déjà essayées, triées pour une meilleure lisibilité
    print(f"Lettres déjà essayées: {sorted(lettres_essayees)}")
    
    
    # Afficher le mot avec les lettres trouvées, en remplaçant les lettres non encore trouvées par des underscores
    mot_affiche = ""
    for lettre in mot_secret:
        if lettre in lettres_trouvees:
            mot_affiche += lettre + " "
        else:
            mot_affiche += "_ "
    print(f"Mot à trouver: {mot_affiche.strip()}")
    print("="*50 + "\n")


def jouer_pendu():
    """Fonction principale du jeu du pendu"""
    # Sélectionner aléatoirement un mot
    mot_secret = random.choice(mots).lower()
    
    
    # Initialiser les variables
    lettres_trouvees = set()
    lettres_essayees = set()
    vies = 6
    victoire = False
    
    print("\n🎮 Bienvenue au jeu du PENDU! 🎮")
    print(f"Un mot de {len(mot_secret)} lettres a été choisi...")
    
    
    # Boucle principale du jeu
    while vies > 0 and not victoire:
        afficher_etat(mot_secret, lettres_trouvees, lettres_essayees, vies)
        
        
        # Demander une lettre
        while True:
            lettre = input("Quelle lettre voulez-vous essayer? ").strip().lower()
            
            # Validation
            if len(lettre) != 1 or not lettre.isalpha():
                print(" Erreur: veuillez entrer une seule lettre valide.")
                continue
            
            if lettre in lettres_essayees:
                print(f"  Vous avez déjà essayé '{lettre}'.")
                continue
            
            break
        
        
        # Ajouter la lettre aux essayées
        lettres_essayees.add(lettre)
        
        # Vérifier si la lettre est dans le mot
        if lettre in mot_secret:
            lettres_trouvees.add(lettre)
            print(f" Bravo! La lettre '{lettre}' est dans le mot!")
            
            
            # Vérifier si le mot est complètement trouvé
            if lettres_trouvees == set(mot_secret):
                victoire = True
        else:
            vies -= 1
            print(f" La lettre '{lettre}' n'est pas dans le mot. Vies perdues!")
    
    
    
    # Affichage final
    afficher_etat(mot_secret, lettres_trouvees, lettres_essayees, vies)
    
    if victoire:
        print(f" VICTOIRE! Le mot était: {mot_secret.upper()}")
    else:
        print(f" DÉFAITE! Le mot était: {mot_secret.upper()}")
    
    return victoire


# Programme principal
if __name__ == "__main__":
    victoire = jouer_pendu()
    
    while True:
        rejouer = input("\nVoulez-vous rejouer? (oui/non): ").strip().lower()
        if rejouer in ["oui", "o", "yes", "y"]:
            victoire = jouer_pendu()
        elif rejouer in ["non", "n", "no"]:
            print("Merci d'avoir joué! Au revoir! ")
            break
        else:
            print("Veuillez répondre par 'oui' ou 'non'.")