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

#Faire une commande complète avant de valider l'achat
commande = []
while True:
    article = input("Entrez le nom de l'article que vous souhaitez ajouter à votre commande (ou tapez 'fin' pour terminer) : ")
    if article == "fin":
        break
    elif article in articles:
        commande.append(article)
        print(article + " a été ajouté à votre commande.")
    else:
        print("Désolé, cet article n'est pas disponible.")

        #Ajouter une somme d'argent total que l'utilisateur peut dépenser et vérifier si le total de la commande est inférieur ou égal à cette somme
total = float(input("Entrez le montant total que vous pouvez dépenser : "))

#Calculer le total de la commande
    


