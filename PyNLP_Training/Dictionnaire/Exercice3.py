#Le Nombre Mystère

import random

nom = input("Donne moi ton prénom : ")

def nbr_mystere():
    print("Hello, Welcome dans mon petit jeu")
    print("Je pense à un nombre entre 1 et 100 et tu dois le trouver")

    mystere = random.randint(1,100)
    essais = 0

    while True:
        try:
            choix = int(input("Entre un nombre : "))
        except ValueError:
            print("Non ce n'est pas un nombre")
            continue

        essais += 1

        if choix < mystere:
            print("Sorry, trop petit ! ")
        elif choix > mystere:
            print("Pas de chance, trop grand !")
        else : 
            print("Attend ! Quoi ! Tu as réussi",nom,"bien joué !")  
            print("Tu as trouvé en",essais,"essais")
            break

if __name__ == "__main__":
    nbr_mystere()              