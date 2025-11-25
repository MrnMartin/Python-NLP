#Compter les lettres “a” dans un texte.

#Solution 1
phrase = input("Donne moi ta phrase")
lettre = "a"

nombre = phrase.count(lettre)
print("Le nombre de fois que la lettre",lettre,"apparaît est:",nombre)

#Solution 2 
phrase = input("Donne moi ta phrase")
lettre = "a"

if lettre in phrase:
    nombre = phrase.count(lettre)
    print("Le nombre de fois que la lettre",lettre,"apparaît est:",nombre)
else:
    print("La lettre", lettre, "n'apparait pas dans la phrase.")