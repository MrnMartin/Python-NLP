#Trouver le mot le plus long dans une liste de mots

mots =["fruits", "légumes", "tomate", "carotte", "oignon"]

mot_pl = mots[0]
for mot in mots: 
    if len(mot) > len(mot_pl):
        mot_pl = mot

print("Le mot le plus long est:", mot_pl)