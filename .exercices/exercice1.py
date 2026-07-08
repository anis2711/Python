#demande des information aux utilisateurs
nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))

#demande des informations sur la naissance

date_naissance = "27/11/1990"
lieu_naissance = "Tunis"
print("Vous êtes né en " + date_naissance + " à " + lieu_naissance + ".")

#Afficher la date d'aujourd'hui
from datetime import date
aujourdhui = date.today()

#Afficher un message de bienvenue à l'utilisateur
print("Bonjour " + prenom + " " + nom + ", vous avez " + str(age) + " ans.")
print("Aujourd'hui, nous sommes le " + str(aujourdhui) + ".")