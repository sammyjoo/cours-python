#import de librairie de générateur d'aléatoire
import random

from requests.sessions import PreparedRequest

#jeu : pierre, feuille, ciseau en python
p = "pierre"
f = "feuille"
c = "ciseau"
liste = ["pierre","feuille","ciseau"]
scoreUtilisateur    = 0
scoreRobot          = 0

#EXEMPLE
# Si l'utilisateur séléctionne pierre, l'ordinateur séléctionne aléatoirement pierre, feuille ou ciseau
#si l'ordinateur séléctionne pierre affiché "match nul"
#si l'ordinateur séléctionne feuille "perdu"
#si l'ordinateur séléctionne ciseau "gagné"






while True:

    #ETAPE 1 - demander à l’utilisateur de saisir une chaîne de caractères
    utilisateur=input("Entrez pierre, feuille ou ciseau : ")
    print(utilisateur)

    # ETAPE 2 - demander à l'ordinateur de saisir aléatoirement pierre, feuille ou ciseau
    robot = random.choice(liste)
    print(robot)

    # ETAPE 3 -  si l'utilisateur séléction pierre, feuille ou ciseau et l'ordinateur séléctionne pierre, feuille ou ciseau on affiche le résultat



    if utilisateur == "pierre" and robot == "ciseau":
        scoreUtilisateur += 1
        print("Vous"+" "+":"+str(scoreUtilisateur)+" "+"robot"+" "+str(scoreRobot))
        

    if utilisateur == "feuille" and robot == "pierre":
        scoreUtilisateur += 1
        print("Vous"+" "+":"+str(scoreUtilisateur)+" "+"robot"+" "+str(scoreRobot))
        

    if utilisateur == "ciseau" and robot == "feuille":
        scoreUtilisateur += 1
        print("Vous"+" "+":"+str(scoreUtilisateur)+" "+"robot"+" "+str(scoreRobot))
        

    if utilisateur == "pierre" and robot == "feuille":
        scoreRobot += 1
        print("Vous"+" "+":"+str(scoreUtilisateur)+" "+"robot"+" "+str(scoreRobot))
        

    if utilisateur == "feuille" and robot == "ciseau":
        scoreRobot += 1
        print("Vous"+" "+":"+str(scoreUtilisateur)+" "+"robot"+" "+str(scoreRobot))
        

    if utilisateur == "ciseau" and robot == "pierre":
        scoreRobot += 1
        print("Vous"+" "+":"+str(scoreUtilisateur)+" "+"robot"+" "+str(scoreRobot))
        

    if utilisateur == "pierre" and robot == "pierre":
        print("Vous"+" "+":"+str(scoreUtilisateur)+" "+"robot"+" "+str(scoreRobot))

    if utilisateur == "feuille" and robot == "feuille":
        print("Vous"+" "+":"+str(scoreUtilisateur)+" "+"robot"+" "+str(scoreRobot))

    if utilisateur == "ciseau" and robot == "ciseau":
        print("Vous"+" "+":"+str(scoreUtilisateur)+" "+"robot"+" "+str(scoreRobot))

    if scoreRobot == 3 :
        print("PERDU")
        break
    if scoreUtilisateur == 3 :
        print("GAGNER")
        break