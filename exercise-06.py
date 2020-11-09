# exercise-06.py

import random

# exo 6.1
# Créez une liste nommée `my_list` contenant un nombre entier, un nombre à virgule flottante, une chaîne de caractères et un booléen

# réponse 6.1
my_list = [1, 1.5, "string"]
# exo 6.2
# Affichez l'élément qui se trouve à la troisième position de la liste
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.2
print(my_list[2])
# exo 6.3
# Ajoutez une chaîne de caractères à la liste `my_list` (sans modfier le code d'initialisation) et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.3
my_list.append('addedString')

print(my_list)

# exo 6.4
# Supprimez l'élément qui se trouve en deuxièm position de la liste et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.4
del(my_list[1])

print(my_list)

# exo 6.5
# Remplacez l'élément qui se trouve en deuxièm position de la liste par un nombre entier et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.5
my_list[1] = 10

print(my_list)

# exo 6.6
# Affichez la taille de la liste
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.6
print(len(my_list))
# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7

my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# Remarque : les exercices suivants nécessitent l'utilisation d'une boucle `for`

# exo 6.8
# Calculez la somme des nombres de la liste et affichez le résultat
my_list = [2.71, 42]

# réponse 6.8
for i in my_list:
    print(my_list[0] + my_list[1])
    break

# exo 6.9
# Calculez la somme des nombres de la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.9
for i in my_list:
    print(my_list[0] + my_list[1] + my_list[2] + my_list[3] + my_list[4] + my_list[5])
    break

# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10
for i in my_list:
    print((my_list[0] + my_list[1] + my_list[2] + my_list[3] + my_list[4] + my_list[5]) / 6)
    break

# exo 6.11
# Trouvez l'index de la valeur `3.14` dans la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.11
print(my_list.index(3.14))

# exo 6.12
# Comptez les nombres plus petits ou égaux à 10 dans la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.12
#my_list.count(float>10)

#Après plusieurs essais, et plusieurs recherches, je n'ai toujours pas trouvé

# exo 6.13
# Multipliez chacun des nombres dans la liste par 100 et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.13
print((my_list[0] * 100) + (my_list[1] * 100) + (my_list[2] * 100) + (my_list[3] * 100) + (my_list[4] * 100) + (my_list[5] * 100))
# exo 6.14
# Créez une deuxième liste ne contenant que les nombre entiers de la liste
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.14
my_list2 = [42, 123, 2]

# exo 6.15
# Ici le but est d'intervertir les éléments de la liste deux à deux
# Liste initiale :
#
#   my_list = [2.71, 42, 123, 2, 3.14, 1.61]
#
# Résultat attendu :
#
#   my_list = [42, 2.71, 2, 123, 1.61, 3.14]
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.15
my_list[0], my_list[1], my_list[2], my_list[3], my_list[4], my_list[5] = my_list[1], my_list[0], my_list[3], my_list[2], my_list[5], my_list[4]

print(my_list)
# exo 6.16
# Triez la liste en utilisant l'algorithme du tri bulle puis affichez la liste
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.16
my_list.sort()
print(my_list)
# code 6.1
# Lire la valeur de la ligne `m` et de la colonne `n` d'un tableau en 2 dimension
# print(matrix[m][n])
#
# Exemple avec la ligne 2 (index 1) et la colonne 3 (index 2)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# Cette ligne affiche `6`
print(matrix[1][2])

# exo 6.17
# Affichez la valeur qui se trouve à la colonne 4, ligne 3
# Attention : il faut faire `- 1` pour obtenir les index correspondant
size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

print(matrix)

# réponse 6.17
print(matrix[2][3])
# exo 6.18
# Avec le même tableau en 2 dimension, affichez toutes les valeurs plus petites ou égales à 50 ainsi que leur cordoonnées (ligne et colonne)

# réponse 6.18

# Je n'ai pas su trouver la réponse.