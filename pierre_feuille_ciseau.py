#import de librairie de générateur d'aléatoire
import random

#jeu : pierre, feuille, ciseau en python
p = "pierre"
f = "feuille"
c = "ciseau"
liste = ["pierre","feuille","ciseau"]

#EXEMPLE
# Si l'utilisateur séléctionne pierre, l'ordinateur séléctionne aléatoirement pierre, feuille ou ciseau
#si l'ordinateur séléctionne pierre affiché "match nul"
#si l'ordinateur séléctionne feuille "perdu"
#si l'ordinateur séléctionne ciseau "gagné"








#ETAPE 1 - demander à l’utilisateur de saisir une chaîne de caractères
utilisateur=input("Entrez pierre, feuille ou ciseau : ")
print(utilisateur)

# ETAPE 2 - demander à l'ordinateur de saisir aléatoirement pierre, feuille ou ciseau
robot = random.choice(liste)
print(robot)

# ETAPE 3 -  si l'utilisateur séléction pierre, feuille ou ciseau et l'ordinateur séléctionne pierre, feuille ou ciseau on affiche le résultat
if utilisateur == "pierre" and robot == "pierre":
    print("match nul")

if utilisateur == "pierre" and robot == "feuille":
    print("perdu")

if utilisateur == "pierre" and robot == "ciseau":
    print("gagner")

if utilisateur == "feuille" and robot == "feuille":
    print("match nul")

if utilisateur == "feuille" and robot == "ciseau":
    print("perdu")

if utilisateur == "feuille" and robot == "pierre":
    print("gagner")

if utilisateur == "ciseau" and robot == "ciseau":
    print("match nul")

if utilisateur == "ciseau" and robot == "feuille":
    print("gagner")

if utilisateur == "ciseau" and robot == "pierre":
    print("perdu")