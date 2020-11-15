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

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
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

product1 = ProductLorem()

product1.set_name("Foo")
product1.set_price(31.41)

print(product1.get_name())
print(product1.get_price())

print()

product2 = ProductLorem()

product2.set_name("Bar")
product2.set_price(27.18)

print(product2.get_name())
print(product2.get_price())

print()

product3 = ProductLorem()

product3.set_name("Baz")
product3.set_price(16.18)

print(product3.get_name())
print(product3.get_price())

print()

# exo 12.6
# Ajoutez chacune des instances de la classe `ProductLorem` à une liste nommée `products`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom et le prix de chaque produit
# Calculez la somme du prix des produits et affichez-en un arrondi à 2 chiffres après la virgule, après la boucle `for`


# réponse 12.6

products = [product1, product2, product3]

total_Product_Price = 0

for product in products:
    total_Product_Price += product.get_price()
 
    print(f"Nom du produit : {product.get_name()} | Prix du produit : {product.get_price()}")

    print()
    print(f"La somme total des produits est de {round(total_Product_Price, 2)}")
    print()

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
class ProductIpsum:
    def __init__(self, name:str='', price:int=0.0, tax:int=0.0):
        self._name = name
        self._price = price
        self._tax = tax

    def get_name(self) -> str:
        return self._name

    def set_name(self, name:str) -> None:
        self._name = name

    def get_price(self) -> int:
        return self._price

    def set_price(self, price:int) -> None:
        self._price = price
        
    def get_tax(self) -> int:
        return self._tax

    def set_tax(self, tax:int) -> None:
        self._tax = tax

    def get_tax_included_price(self) -> int:
        return self._price + ((self._tax * self._price) / 100)



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
product1 = ProductIpsum()

product1.set_name("Dolor")
product1.set_price(31.41)
product1.set_tax(20.0)
print(product1.get_name())
print(product1.get_price())
print(product1.get_tax())
print(product1.get_tax_included_price())
print()

product2 = ProductIpsum()
product2.set_name("Sit")
product2.set_price(27.18)
product2.set_tax(10.0)
print(product2.get_name())
print(product2.get_price())
print(product2.get_tax())
print(product2.get_tax_included_price())
print()

product3 = ProductIpsum()
product3.set_name("Amet")
product3.set_price(16.18)
product3.set_tax(5.5)
print(product3.get_name())
print(product3.get_price())
print(product3.get_tax())
print(product3.get_tax_included_price())
print()
print()
# exo 12.9
# Ajoutez chacune des instances de la classe `ProductIpsum` à une liste nommée `product_ipsums`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom, le prix (sans la taxe), la taxe et le produit taxe incluse de chaque produit
# Calculez :
# - la somme du prix des produits sans les taxes
# - la somme du montant des taxes
# - la somme du prix des produits taxes incluses
# Et affichez-les après la boucle `for`

# réponse 12.9

product_ipsums = [product1, product2, product3]

total_product_price_without_tax = 0
total_tax_price = 0
total_product_price_with_tax = 0

for product in product_ipsums:
    total_product_price_without_tax += product.get_price()
    total_tax_price = ((product.get_tax() * product.get_price()) / 100)
    total_product_price_with_tax = total_product_price_without_tax + total_tax_price

    print(f"""Nom du produit : {product.get_name()} | 
    Prix du produit : {product.get_price()}€ HT + {product.get_tax()}% de taxe 
    soit : {product.get_tax_included_price()}€ TTC""")

    print()
    print(f"La somme total des produits sans les taxes est de {round(total_product_price_without_tax, 2)}")
    print()
    print(f"La somme du montant des taxes est de {round(total_tax_price, 2)}")
    print()
    print(f"La somme total des produits avec les taxes est de {round(total_product_price_with_tax, 2)}")
    print()