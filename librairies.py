#random est une librairie de generateur d'hasard
import random
print(random.randrange(0,10))

print("----------")

import datetime
print(datetime.datetime.now())
print("---")
print(datetime.datetime.now().year)

print("----------")

import requests
response = requests.get("https://www.vitakraft.fr/")
#print(response.text)

import slugify
print(slugify.slugify("Bonjour, je suis pauvre"))


print("-------------------------------EXERCICES------------------------------------------------")
#exercices
print(" ")
print(" ")

import random
amour       = random.randrange(0,15)
argents    = random.randrange(0,15)

if amour > argents:
    phrase ="bonheur"
else:
    phrase ="libertés"
print(str(amour)+"%"+" "+"d'amour")
print(str(argents)+"%"+" "+"d'argent")
print("  ")
print("="+" "+phrase)

print(" ")

print("----------")

import datetime
annee = datetime.datetime.now().year
jour = datetime.datetime.now().day
mois = datetime.datetime.now().month
heures = datetime.datetime.now().hour
minutes = datetime.datetime.now().minute

print(str(jour)+"/"+str(mois)+"/"+str(annee)+" "+str(heures)+":"+str(minutes))

print("----------")

