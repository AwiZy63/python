# exercise-12-solution.py

# exo 12.1
# Créez une classe nommée `User` qui possède les attributs suivants :
# - firstname: valeur par défaut ''
# - lastname: valeur par défaut ''
# - email: valeur par défaut ''
# - newsletter: valeur par défaut False
# et la méthode suivante :
# - __init__() : le constructeur
# Ne créez pas de getters et de setters

# réponse 12.1
class User :
    def __init__(self, firstname, lastname, email, newsletter):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.newsletter = newsletter

# exo 12.2
# Créez 4 instances de la classe `User` et affectez les valeurs suivantes à ses attributs :
# - user1
#   - firstname: Joe
#   - lastname: Dalton
#   - email: joe.dalton@example.com
#   - newsletter: true
# - user2
#   - firstname: Jack
#   - lastname: Dalton
#   - email: jack.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: William
#   - lastname: Dalton
#   - email: william.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: Avrel
#   - lastname: Dalton
#   - email: avrel.dalton@example.com
#   - newsletter: true

# réponse 12.2

user1 = User("Joe", "Dalton", "joe.dalton@example.com", True)
print(user1.firstname)
print(user1.lastname)
print(user1.email)
print(user1.newsletter)

print()

user2 = User("Jack", "Dalton", "jack.dalton@example.com", False)
print(user2.firstname)
print(user2.lastname)
print(user2.email)
print(user2.newsletter)

print()

user3 = User("William", "Dalton", "william.dalton@example.com", False)
print(user3.firstname)
print(user3.lastname)
print(user3.email)
print(user3.newsletter)

print()

user4 = User("Avrel", "Dalton", "avrel.dalton@example.com", True)
print(user4.firstname)
print(user4.lastname)
print(user4.email)
print(user4.newsletter)

print()

# exo 12.3
# Ajoutez chacune des instances de la classe `User` à une liste nommée `users`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom complet et l'email de chaque utilisateur s'il est abonné à la newsletter

# réponse 12.3
users = [user1, user2, user3, user4]

for user in users:
    if user.newsletter:
        print(f"Nom : {user.firstname} {user.lastname}. Email : {user.email}.")
    else:
        break

print()
# exo 12.4
# Créez une classe nommée `ProductLorem` qui possède les attributs suivants :
# - _name: valeur par défaut ''
# - _price: valeur par défaut 0.0
# et les méthodes suivantes :
# - __init__() : le constructeur
# - getName() : renvoit le nom du produit
# - setName() : détermine le nom du produit
# - getPrice() : renvoit le prix du produit
# - setPrice() : détermine le prix du produit

# réponse 12.4

class ProductLorem:
    def __init__(self):
        self._name = ""
        self._price = 0.0

    def get_Name(self):
        return self._name

    def set_Name(self, name):
        self._name = name

    def get_Price(self):
        return self._price

    def set_Price(self, price):
        self._price = price


# exo 12.5
# Créez 3 instances de la classe `ProductLorem` et affectez les valeurs suivantes à ses attributs en utilisant les setters :
# - product1
#   - name: Foo
#   - price: 31,41
# - product2
#   - name: Bar
#   - price: 27,18
# - product3
#   - name: Baz
#   - price: 16,18

# réponse 12.5

product = ProductLorem()

product.set_Name("Foo")
product.set_Price(31.41)

print(product.get_Name())
print(product.get_Price())

print()

product2 = ProductLorem()

product2.set_Name("Bar")
product2.set_Price(27.18)

print(product2.get_Name())
print(product2.get_Price())

print()

product3 = ProductLorem()

product3.set_Name("Baz")
product3.set_Price(16.18)

print(product3.get_Name())
print(product3.get_Price())

print()

# exo 12.6
# Ajoutez chacune des instances de la classe `ProductLorem` à une liste nommée `product_lorems`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom et le prix de chaque produit
# Calculez la somme du prix des produits et affichez-la après la boucle `for`

# réponse 12.6

# exo 12.7
# Créez une classe nommée `ProductIpsum` qui possède les attributs suivants :
# - _name: valeur par défaut ''
# - _price: valeur par défaut 0.0
# - _tax: valeur par défaut 0.0
# et les méthodes suivantes :
# - __init__(name, price, tax) : le constructeur
# - getName() : renvoit le nom du produit
# - setName() : détermine le nom du produit
# - getPrice() : renvoit le prix du produit
# - setPrice() : détermine le prix du produit
# - getTax() : renvoit la taxe en pourcentage
# - setTax() :  détermine la taxe en pourcentage (20.0 pour une taxe de 20 %)
# - getTaxIncludedPrice() : cette méthode renvoit le prix taxe incluse

# réponse 12.7

# exo 12.8
# Créez 3 instances de la classe `ProductIpsum` et affectez les valeurs suivantes à ses attributs en utilisant le constructeur :
# - product1
#   - name: Dolor
#   - price: 31,41
#   - tax: 20.0
# - product2
#   - name: Sit
#   - price: 27,18
#   - tax: 10.0
# - product3
#   - name: Amet
#   - price: 16,18
#   - tax: 5.5

# réponse 12.8

# exo 12.9
# Ajoutez chacune des instances de la classe `ProductIpsum` à une liste nommée `product_ipsums`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom, le prix (sans la taxe), la taxe et le produit taxe incluse de chaque produit
# Calculez :
# - la somme du prix des produits sans les taxes
# - la somme du montant des taxes
# - la somme du prix des produits taxes incluses
# Et affichez-les après la boucle `for`

# réponse 12.9