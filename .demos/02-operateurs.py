nombre_un = 5
nombre_deux = 10
nombre_trois = 4

#les opérateurs arithmétiques
la_somme = 5 + 10
la_somme_variables = nombre_un + nombre_deux

la_concatenation = "5" + "10" # "510"

la_difference = nombre_un - nombre_deux # -5

le_quotient = nombre_deux / nombre_trois # 2.5

le_quotient_euclidien = nombre_deux // nombre_trois # 2

le_reste = nombre_deux % nombre_trois # 2

le_produit = nombre_un * nombre_trois # 20

la_multiplication_texte = "ABC" * 3 # "ABCABCABC"

#la caractère espace, pour un ordinateur => \0

la_puissance = nombre_deux ** nombre_un # 100 000

#Les opérateurs de comparaison

egalite = 10 == 11 # False

difference = 10 != 11 # True

superiorite = 10 > 5 # True

inferiorite = 10 < 5 # False

superiorite_egalite = 10 >= 5 # True

inferiorite_egalite = 10 <= 5 # False

inferiorite_ou_egalite = 10 <= 10 # True

#les opérateurs logiques
possede_carte_bibliotheque = True
age =int(input("Quel est votre âge ? "))

acces_bibliotheque = age >= 12 and possede_carte_bibliotheque

acces_avec_paiement_possible_2_euros = argent >= 2 and age >= 2 or possede_carte_bibliotheque

est_mineur = not (age >= 18)

age_entre_10_et_18_compris = age >= 10 and age <= 18
age_entre_10_et_18_compris = 10 <= age <= 18
