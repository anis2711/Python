#Affiche un menu et demander d'entrer un choix

import random

notes = []

def afficher_menu():
    print("\n====Menu_notes====")
    print("1. Entrer une nouvelle note")
    print("2. Consulter la liste des notes")
    print("3. Afficher la plus grande note")
    print("4. Afficher la plus petite note")
    print("5. Afficher la moyenne des notes")
    print("6. Sortir du programme")



def Entrer_note():
    try:
        note = float(input("Entrer une note : "))
        notes.append(note)
        print("note ajouter avec succes.")
    except ValueError:
        print("Erreur : veuiller entrer un nombre valide")



def Consulter_notes():
    if len(notes) == 0:
        print("Aucune note n'a encore entrer")

    else:
        print("notes entrer :")
        for note in notes:
            print("-", note)


def Affiche_plus_petite_note():
    if len(notes) == 0:
        print("impossible pas de note dans la liste")

    else:
        print("la plus petite note et :", min(notes))

def Affiche_plus_grande_note():
    if len(notes) == 0:
        print("impossible pas de note dans la liste")

    else:
        print("la plus grande note et :", max(notes))

def Affiche_la_moyenne():
    if len(notes) == 0:
        print("impossible pas de note dans la liste")

    else:
        moyenne = sum(notes) / len(notes)
        print("la moyenne des notes est :", moyenne)

def programme_notes():
    choix = ""  
    while choix != "0":
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1" :
            Entrer_note()
        elif choix == "2" :
            Consulter_notes()
        elif choix == "3" :
            Affiche_plus_petite_note()
        elif choix == "4" :
            Affiche_plus_grande_note()
        elif choix == "5" :
            Affiche_la_moyenne()
        elif choix == "0" :
            print("Au revoir !")
        else: 
            print("Choix invalide. veuiller recommencer") 


programme_notes()                   





