class Cake:
    def prepare(self):
        print("Welcome to Cake Store")

class ChocolateCake(Cake):
    def prepare(self):
        super().prepare()
        print("Baking a sweet chocolate cake")
        print("Please wait a moment")

class StrawberryCake(Cake):
    def prepare(self):
        super().prepare()
        print("Baking a fresh strawberry cake")
        print("Please wait a moment")

class CheeseCake(Cake):
    def prepare(self):
        super().prepare()
        print("Baking a creamy cheese cake")
        print("Please wait a moment")

def order_cake(cake):
    cake.prepare()

print("Select a cake:")
print("1. Chocolate Cake")
print("2. Strawberry Cake")
print("3. Cheese Cake")

choice = input("Enter the number (1, 2, or 3): ")

if choice == "1":
    choco = ChocolateCake()
    order_cake(choco)
elif choice == "2":
    strawberry = StrawberryCake()
    order_cake(strawberry)
elif choice == "3":
    cheese = CheeseCake()
    order_cake(cheese)
else:
    print("Invalid choice.")
    print("I'm sorry, you can only choose from the 3 available options.")