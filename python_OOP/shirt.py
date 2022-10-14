class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)


Shirt("Red", "M", "Short sleeve", "499")

new_shirt = Shirt("Red", "M", "Short sleeve", "499")

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)


new_shirt.change_price(389)
print(new_shirt.price)

new_shirt.discount(.2)
print(new_shirt.discount)

tshirt_collection = []

shirt_one = Shirt("Orange", "M", "Short sleeve", "299")
shirt_two = Shirt("Pink", "L", "Long shorts", "799")
shirt_three = Shirt("Yellow", "XL", "long shorts", "899")

tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three)

for i in range(len(tshirt_collection)):
    print(tshirt_collection[i].color)
