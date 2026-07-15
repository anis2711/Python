
"""Carnet de notes"""

# Le programme permet d'afficher Un menu et demande d'entrer Votre choix

import random

notes = []


def afficher_menu():
    print("\n=== PROGRAMME NOTES ===")
    print("1. Entrer une nouvelle note")
    print("2. Consulter l'ensemble des notes")
    print("3. Connaitre la plus petite note")
    print("4. Connaitre la plus grande note")
    print("5. Connaitre la moyenne des notes")
    print("0. Quitter")


def entrer_note():
    try:
        note = float(input("Entrez une note : "))
        notes.append(note)
        print("Note ajoutee avec succes.")
    except ValueError:
        print("Erreur : veuillez entrer un nombre valide.")


def consulter_notes():
    if len(notes) == 0:
        print("Aucune note n'a encore ete entree.")
    else:
        print("Notes entrees :")
        for note in notes:
            print("-", note)


def afficher_plus_petite_note():
    if len(notes) == 0:
        print("Impossible : aucune note n'a encore ete entree.")
    else:
        print("La plus petite note est :", min(notes))


def afficher_plus_grande_note():
    if len(notes) == 0:
        print("Impossible : aucune note n'a encore ete entree.")
    else:
        print("La plus grande note est :", max(notes))


def afficher_moyenne():
    if len(notes) == 0:
        print("Impossible : aucune note n'a encore ete entree.")
    else:
        moyenne = sum(notes) / len(notes)
        print("La moyenne des notes est :", moyenne)


def programme_notes():
    choix = ""

    while choix != "0":
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            entrer_note()
        elif choix == "2":
            consulter_notes()
        elif choix == "3":
            afficher_plus_petite_note()
        elif choix == "4":
            afficher_plus_grande_note()
        elif choix == "5":
            afficher_moyenne()
        elif choix == "0":
            print("Au revoir !")
        else:
            print("Choix invalide. Veuillez recommencer.")


programme_notes()