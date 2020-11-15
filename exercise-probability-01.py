# exercise-probability-01.py

import random

# code 1.1
# L'appel à la fonction random.randint(0, 1) renvoit un nombre entier aléatoire compris entre 0 et 1 inclus.
number = random.randint(0, 1)

# code 1.2
# Pour savoir si la variable "number" vaut 1, je peux utiliser un bloc conditionnel.
if number == 0:
    print("le nombre vaut 0")

# code 1.3
# Pour savoir quel nombre la variable "number" vaut, je peux utiliser une boucle.
for i in range(0, 2):
    if number == i:
        # affichage avec interpolation de la variable au moyen d'une "f-string"
        print(f"le nombre vaut {number}")

# exo 1.1
# Alice et Bob veulent jouer à pile ou face.
# - si la variable "head_or_tail" vaut 0, cela équivaut à pile
# - si elle vaut 1, cela équivaut à face
# Alice parie pile et Bob parie face.
# Qui gagne ? Alice ou Bob ?
# Rédigez le code qui indique le nom du gagnant.


# réponse 1.1
head_or_tail = random.randint(0, 1)

print()

print("Alice parie pile")
print()
print("Bob pari face")
print()

print(f"DEBUG : head_or_tail = {head_or_tail}")

print()

if head_or_tail == 0:
    print("la pièce est tombée sur pile")
    print()
    print("Alice a donc gagnée")
elif head_or_tail == 1:
    print("la pièce est tombée sur face")
    print()
    print("Bob a donc gagné")

print()
# exo 1.2
# Alice et Bob veulent jouer aux dés.
# Alice parie qu'elle va faire au moins 4. Bob parie qu'il va faire 3 au plus.
# Qui gagne ? Alice ou Bob ?
# Rédigez le code qui indique le nom du gagnant.

# réponse 1.2
des = random.randint(1, 6)

print()

print("Alice parie qu'elle fera au moins 4")
print()
print("Bob pari qu'il fera 3 au plus")
print()

print(f"DEBUG : des = {des}")

print()

if des >= 4:
    print(f"Le dès est tombé sur {des}")
    print()
    print("Alice a donc gagnée")
elif des <= 3:
    print(f"Le dès est tombé sur {des}")
    print()
    print("Bob a donc gagné")

print()
# exo 1.3
# Alice et Bob jouent à pierre papier ciseaux.
# - 1 équivaut à pierre
# - 2 équivaut à papier
# - 3 équivaut à ciseaux
# Rédigez le code qui indique qui gagne.

# réponse 1.3

while True:
    Alice = random.randint(1, 3)
    Bob = random.randint(1, 3)
    
    if Alice == Bob:
        print("Alice et Bob ont fait égalité.. \n Reessayons")
        print()
# Pierre -- Ciseaux
    elif Alice == 1 and Bob == 3:
        print(f"Alice a gagnée (Alice : ({Alice}) Pierre, Bob : ({Bob}) Ciseaux)")
        break
# Pierre -- Ciseaux
    elif Alice == 3 and Bob == 1:
        print(f"Bob a gagné (Bob : ({Bob}) Pierre, Alice : ({Alice}) Ciseaux)")
        break
# Papier -- Pierre
    elif Alice == 2 and Bob == 1:
        print(f"Alice a gagnée (Alice : ({Alice}) Papier, Bob : ({Bob}) Pierre)")
        break
# Papier -- Pierre
    elif Alice == 1 and Bob == 2:
        print(f"Bob a gagné (Bob : ({Bob}) Papier, Alice : ({Alice}) Pierre)")
        break
# Pierre -- Ciseaux
    elif Alice == 3 and Bob == 2:
        print(f"Alice a gagnée (Alice : ({Alice}) Pierre, Bob : ({Bob}) Ciseaux)")
        break
# Pierre -- Ciseaux
    elif Alice == 2 and Bob == 3:
        print(f"Bob a gagné (Bob : ({Bob}) Pierre, Alice : ({Alice}) Ciseaux)")
        break
    else:
        print("ERR!")
        break