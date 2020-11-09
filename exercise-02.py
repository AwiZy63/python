# exo 2.1
# Affectez :
# - le nombre 42 à une variable
# - le nombre d'or 1,61 à une variable
# - votre nom et prénom à une variable
# - la valeur booléenne vrai si nous sommes le matin, sinon la valeur booléenne faux, à une variable
# - la valeur null `None` à une variable
# Affichez ces variables

# réponse 2.1
number = 42
number2 = 1.61
my_Name = "Flanquart Bastien"
is_Morning = True

if is_Morning:
    print("Nous sommes le matin")
else:
    print("Nous ne sommes pas le matin")

null = None

# code 2.1
# la fonction `round()` permet d'arrondir un float en un integer
# 0,1 est arrondi à la valeur inférieur
print(round(0.1))
# 0,9 est arrondi à la valeur supérieur
print(round(0.9))
# la fonction `round()` permet aussi d'arrondir en précisant le nombre de chiffres après la virgule
# arrondir à un nombre décimal à 4 chiffres après la virgule
print(round(1 / 3, 4))

# exo 2.2
# Stockez le valeurs suivantes dans une variable et transtypez-les :
# - integer 2 en un float
# - float 1,62 en un integer
# - float 1,62 en un float arrondi en un integer
# - float 1,62 en un float arrondi en un float à un chiffre après la virgule
# À chaque fois stockez le résultat dans une variable et affichez le résultat.

# réponse 2.2

int1 = 2
print(type(int1))
int2 = float(int1)
print(type(int2))

float1 = 1.62

# to integer :
float2 = int(float1)
print(type(float2))

# to float arrondi to integer
float2 = round(float1)
print(float2)
float3 = int(float2)
print(type(float2))

# to float arrondi 1 chiffre après la virgule

float2 = round(float1, 1)
print(float2)
