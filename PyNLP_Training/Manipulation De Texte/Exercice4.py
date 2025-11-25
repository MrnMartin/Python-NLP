#Remplacer un mot dans une phrase

phrase = input("Donne moi une phrase:")
ancien_m = input("Quel mot veux tu remplacer")
nouveau_m = input ("Quel est le nouveau mot")

nouvelle_phrase = phrase.replace(ancien_m,nouveau_m)

print("Nouvelle phrase:", nouvelle_phrase)