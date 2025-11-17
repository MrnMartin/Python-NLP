#Exercice 2 : Additionner 2 nombres entrés par l’utilisateur

#Première Solution
Number1 = float(input("Nombre décimal numéro 1 : ")) #Convertit cette chaîne en nombre décimal
Number2 = float(input("Nombre décimal numéro 2 : "))

Total = Number1 + Number2

print(f"L'addition des deux nombres = {Total}")

#Deuxième Solution
Total = int(input("Nombre entier 1 : ")) + int(input("Nombre entier 2 : ")) #Convertit cette chaîne en nombre entier

print(f"L'addition des deux nombres = {Total}")