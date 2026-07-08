# Menu des articles
articles = {
    "Café": 2.50,
    "Thé": 2.00,
    "Chocolat": 3.00,
    "Jus d'orange": 2.75,
    "Eau": 1.50,
    "Croissant": 1.80,
    "Pain au chocolat": 2.00,
    "Sandwich": 5.50,
    "Pâtisserie": 3.50,
    "Cookies": 1.20
}

#Voir les prix des articles
for article, prix in articles.items():
    print(" " + article + ": " + str(prix) + " €")

#Choisir un article et voir son prix
choix = input("Entrez le nom de l'article que vous souhaitez acheter : ")
if choix in articles:
    print("Le prix de " + choix + " est de " + str(articles[choix]) + " €.")
else:
    print("Désolé, cet article n'est pas disponible.")

