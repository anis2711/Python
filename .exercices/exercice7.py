#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
================================================================================
 DONJON SIMPLE - Version light de Donjons et Dragons
================================================================================
Le joueur affronte des creatures les unes apres les autres.
- Il attaque en lancant un de
- La creature riposte en lancant un de
- Le combat continue jusqu'a ce qu'un des deux camps n'ait plus de PV
- Chaque victoire rapporte de l'or (le score final du joueur)
- Le joueur peut choisir de sortir du donjon a tout moment
- S'il meurt, il ne garde que la moitie de son or
================================================================================
"""

import random


# ==============================================================================
# 1. LANCER DE DES
# ==============================================================================

def lancer_de(nb_faces):
    """Simule le lancer d'un de a 'nb_faces' faces (ex: 6 pour un d6)."""
    return random.randint(1, nb_faces)


# ==============================================================================
# 2. LE JOUEUR
# ==============================================================================
# On represente le joueur avec un simple dictionnaire :
# ==============================================================================

joueur = {
    "pv": 30,
    "pv_max": 30,
    "or": 0,
}

# ==============================================================================
# 3. CREATION D'UNE CREATURE
# ==============================================================================
# Chaque creature a des PV et sa propre recompense en or a la mort.
# ==============================================================================

def creer_creature():
    """Genere une nouvelle creature avec des PV et une recompense aleatoires."""
    creature = {
        "nom": "Monstre",
        "pv": random.randint(10, 25),      # PV entre 10 et 25
        "or_recompense": random.randint(5, 15),  # or gagne si elle est vaincue
    }
    return creature

# ==============================================================================
# 4. UN TOUR DE COMBAT
# ==============================================================================

def tour_de_combat(creature):
    """
    Joue un tour : le joueur attaque, puis la creature riposte si elle
    est encore en vie. Modifie directement les PV du joueur et de la creature.
    """
    # --- Attaque du joueur ---
    degats_joueur = lancer_de(6)  # le joueur inflige entre 1 et 6 degats (1d6)
    creature["pv"] -= degats_joueur
    print(f"⚔️  Vous attaquez et infligez {degats_joueur} degats "
          f"(PV du {creature['nom']} : {max(creature['pv'], 0)})")

    # Si la creature est morte, elle ne riposte pas
    if creature["pv"] <= 0:
        return

    # --- Riposte de la creature ---
    degats_creature = lancer_de(4)  # la creature inflige entre 1 et 4 degats (1d4)
    joueur["pv"] -= degats_creature
    print(f"👹 Le {creature['nom']} riposte et vous inflige {degats_creature} degats "
          f"(vos PV : {max(joueur['pv'], 0)}/{joueur['pv_max']})")


# ==============================================================================
# 5. COMBAT COMPLET CONTRE UNE CREATURE
# ==============================================================================

def combat():
    """
    Fait combattre le joueur contre une nouvelle creature jusqu'a ce que
    l'un des deux tombe a 0 PV. Retourne True si le joueur gagne, False sinon.
    """
    creature = creer_creature()
    print(f"\nUn {creature['nom']} surgit devant vous ! (PV : {creature['pv']})")

    # Le combat continue tant que les deux camps sont en vie
    while joueur["pv"] > 0 and creature["pv"] > 0:
        input("Appuyez sur Entree pour attaquer...")
        tour_de_combat(creature)

    if joueur["pv"] > 0:
        # Victoire : le joueur recupere l'or de la creature
        joueur["or"] += creature["or_recompense"]
        print(f"🏆 Vous avez vaincu le {creature['nom']} ! "
              f"Vous gagnez {creature['or_recompense']} pieces d'or "
              f"(total : {joueur['or']})")
        return True
    else:
        print(f"💀 Vous avez ete vaincu par le {creature['nom']}...")
        return False


# ==============================================================================
# 6. BOUCLE PRINCIPALE DU DONJON
# ==============================================================================

def explorer_donjon():
    """
    Enchaine les combats jusqu'a ce que le joueur meure ou decide
    de sortir du donjon.
    """
    while True:
        print(f"\n--- PV : {joueur['pv']}/{joueur['pv_max']} | Or : {joueur['or']} ---")
        choix = input("1. Avancer et combattre\n2. Sortir du donjon\nVotre choix : ")

        if choix == "2":
            print(f"\n🚪 Vous sortez du donjon avec {joueur['or']} pieces d'or !")
            return

        victoire = combat()
        if not victoire:
            # Defaite : le joueur ne garde que la moitie de son or
            joueur["or"] = joueur["or"] // 2
            print(f"Une equipe de chercheurs recupere votre corps et facture "
                  f"ses services...\nIl ne vous reste que {joueur['or']} pieces d'or.")
            return


# ==============================================================================
# 7. PROGRAMME PRINCIPAL
# ==============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Bienvenue dans le DONJON")
    print("=" * 50)

    explorer_donjon()

    print(f"\nScore final : {joueur['or']} pieces d'or.")