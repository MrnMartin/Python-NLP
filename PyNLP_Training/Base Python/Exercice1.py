#Exercice 1 : Afficher ton prénom et ton âge

#Première Solution
Nom = input("Veuillez mettre votre prénom")
Age = input("Indiquez votre âge")

print(f"Vous êtes {Nom} et vous avez {Age} ans.")

#Deuxième Solution
Information = input("Veuillez sélectionner votre prénom et votre âge") 

nom , age = Information.split() #Accepte que l'espace comme séparateur.

print(f"Vous êtes {nom} et vous avez {age} ans.")

#Troisième Solution
import re #REGEX

Information = input("Veuillez sélectionner votre prénom et votre âge") 

nom, age = re.split("r[ ,]+", Information.strip()) #Strip enlève les espaces au début et en fin de chaîne 
 
print(f"Vous êtes {nom} et vous avez {age} ans.")