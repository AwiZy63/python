# exercise-09.py

# exo 9.1
# Créez un dictionnaire nommé `my_dict` associant :
# - une clé alphanumérique et un nombre entier
# - une clé alphanumérique et un nombre à virgule flottante
# - une clé alphanumérique et une chaîne de caractères
# - une clé alphanumérique et un booléen
# Puis affichez le résultat avec un simple `print()`

# réponse 9.1
my_dict = {
    'lorem': 10,
    'ipsum': 1.5,
    'foo': "Lorem Ipsum",
    'bar': True
}

print(my_dict)

# exo 9.2
# Créez un dictionnaire nommé `my_dict` associant :
# - une clé booléenne et un nombre entier
# - une clé booléenne et un nombre à virgule flottante
# - une clé nuémrique et une chaîne de caractères
# - une clé alphanumérique et un booléen
# Puis affichez le résultat avec un simple `print()`

# réponse 9.2
my_dict = {
    True: 10,
    False: 1.5,
    20: "dix plus dix", 
    'lorem': True
}

print(my_dict)

# exo 9.3
# Ajoutez au dictionnaire un élément qui associe la clé alphanumérique `ipsum` à la valeur `2.71`
# Puis affichez le résultat avec un simple `print()`
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.3
my_dict['ipsum'] = 2.71

print(my_dict)
# exo 9.4
# Supprimez du dictionnaire la clé `foo`
# Puis affichez le résultat avec un simple `print()`
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.4
my_dict.pop('foo')

print(my_dict)
# exo 9.5
# Remplacez la valeur du dictionnaire associée à la clé `foo` par `123`
# Puis affichez le résultat avec un simple `print()`
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.5
my_dict['foo'] = 123

print(my_dict)
# exo 9.6
# En utilisant une boucle `for`, affichez les clés (et pas les valeurs) qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.6
for k in my_dict:
    print(f"Keys : {k}")

# exo 9.7
# En utilisant une boucle `for`, affichez les valeurs (et pas les clés) qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.7

for v in my_dict.values():
    print(f"Values : {v}")

# exo 9.8
# En utilisant une boucle `for` et sans utiliser la méthode `items()`, affichez les clés et les valeurs qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}
# Exemple de résultat attendu :
# key: foo, value: 42
# key: bar, value: 3.14
# key: baz, value: lorem ipsum
# etc...

# réponse 9.8
for i in my_dict:
    print(f"key: {my_dict.keys()}, value: {my_dict.values()}")

    # J'ai du refaire l'exercice, j'ai malheureusement oublié cette syntaxe

# exo 9.9
# En utilisant une boucle `for` et la méthode `items()`, affichez les clés et les valeurs qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}
# Exemple de résultat attendu :
# key: foo, value: 42
# key: bar, value: 3.14
# key: baz, value: lorem ipsum
# etc...

# réponse 9.9

for k, v in my_dict.items():
    print(f"key: {k}, value: {v}")