#commentaire
prenom="sam"
print(prenom)


a = 10 
b = 5
c = a*b
print(a*b)
print(a+a)
print(c-a)

#sujet suivant
print("---------------------------------------------------------------- ")

maVariable = "salut"
autreVariable = "toi"
print(maVariable+" "+autreVariable+"<3")

#ajouter un string pour afficher les chiffres (str)
print(maVariable+str(3))

#pour afficher le nombre de caractère avec "len()"
longueurPrenom = len(prenom)

if longueurPrenom > 5:
    print("votre prenom est trop balèze hihih")

elif longueurPrenom == 3:
    print("votre prenom à trois caractères :)")

else:
    print("votre prenom est mini dit donc")

#sujet suivant
print("----------------------------------------------------------------  ")
print(" ")

passaDasnBoucle = 0

# while = tant que 10 est inferieur ou egale à 0
while passaDasnBoucle <= 10:
    print("passage numéro"+" "+str(passaDasnBoucle))


#il va de 2 en 2 pour arriver à 10
    passaDasnBoucle += 2

#sujet suivant
print("----------------------------------------------------------------  ")
print(" ")

dataViz = ["chan katerin", "antho", "Gab","dani","jazon","moi"]

print(dataViz[0])
print(dataViz[1])
print(dataViz[2])
print(dataViz[3])
print(dataViz[4])
print(dataViz[5])
print(" ")
#pour eviter de repeter les "print()" on creer une boucle for in 

for classe in dataViz:
    print(classe)
    if classe == "moi":
        print("'sammy'")
    
#sujet suivant
print("----------------------------------------------------------------  ")
print(" ")

#Dictionnaire
campus = {
    "nom":          "fonderie de l'image",
    "ville":        "bagnolet",
    "formation":    "web dataviz",
    "annee":        "2022"
}

print(campus["nom"])

print(" ")

# afficher les clés du dictionnaire + les noms avec une boucle for
for key in campus:
    print(key + " : "+ campus[key])

#sujet suivant
print("----------------------------------------------------------------  ")
print(" ")

#def = function
def direBonjour(prenom, formation):
    phrase ="bonjour"+" "+prenom+" "+formation+"!"
    return phrase
print(direBonjour("chan katerine","web dataviz"))


#sujet suivant
print("----------------------------------------------------------------  ")
print(" ")

def siPrenomCool(prenom):
    longueur_prenom = len(prenom)

    if longueur_prenom < 5:
        phrase = "Ton prenom n'est pas so good :("
    else:
        phrase = "ton prenom est so good :)"
    return phrase

#on appelle la fonction
print(siPrenomCool("Chan Katrine"))

#sujet suivant
print("----------------------------------------------------------------  ")
print(" ")

