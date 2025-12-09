#Créer un dictionnaire “nom → âge” et afficher une valeur.

ages = {
    "Ana" : 25,
    "Carla" : 26,
    "Sophie" : 38,
}

nom = input("Choisir un nom entre : Ana , Carla , Sophie : ")

if nom in ages:
    print(nom,"à",ages[nom],"ans")
else:
    print("Ce nom n'existe pas dans le dictionnaire")
