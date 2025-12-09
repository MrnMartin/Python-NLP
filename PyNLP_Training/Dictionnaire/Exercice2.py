#Compter les occurrences de chaque mot dans une liste.

mots = ["chien", "chat", "lapin", "serpent", "chien", "hiboux", "alpaga"]

compteur = {}

for mot in mots:
    if mot in compteur:
        compteur[mot] +=1
    else:
        compteur[mot] = 1
        
print (compteur)