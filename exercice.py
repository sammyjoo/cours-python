# Exercice 1 :
# Afficher un "Hello World" dans le terminal
print("Hello world")
print("----------")
# Exercice 2 :
# Modifier le code pour calculer la moyenne des notes
note_maths = 15
note_francais = 12
note_histoire_geo = 9
total = note_maths+note_francais+note_histoire_geo
moyenne = total / 3
print('La moyenne est de '+str(moyenne)+' / 20.')

print("-------------")
# Exercice 3 :
"""
Avec une boucle FOR, affichez 15 fois "J'adore le Python"
avec le numéro de la ligne à coté
"""
like = 1
while like <= 10:
    print("J'adore le Python"+" "+str(like))
    like += 1

print("-----------")
# Exercice 4 :
"""
Imaginons : on a un budget de 1500€ et on souhaite 
acheter un produit à 1800€. Afficher si le budget le
permet en le vérifiant avec une condition IF
"""
budget = 1500
produit = 1800

if budget > produit :
    print("vous avez le budget hihih")

elif budget== produit:
    print("vous avez le juste prix")

else:
    print("vous avez pas assez d'argent :(")


print("------------")
# Exercice 5 :
#Afficher le 3ème élément de cette liste
fruits = ['papaye', 'mangue', 'litchi', 'kaki', 'avocat']

print(fruits[2])

print("------------")
# Exercice 6 :
"""
Compléter la fonction qui permet de convertir
des euros en dollars pour un prix donné
"""


def converDollar(prixEnEuros):
    prixEnDollar = 1.17*prixEnEuros
    return prixEnDollar

euros = 20

print(converDollar(euros))