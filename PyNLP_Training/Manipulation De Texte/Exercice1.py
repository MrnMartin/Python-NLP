#Compter les mots d’un texte.

phrase = input("Donne moi ta phrase")

def compte_mots(phrase):
    return len(phrase.split())

print("Le nombre de mots est :", compte_mots(phrase))