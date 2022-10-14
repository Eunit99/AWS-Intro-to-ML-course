from shirt import Shirt

shirt_one = Shirt("Blue", "M", "long sleeves", 299)
shirt_two = Shirt("Orange", "S", "Long sleeves", 299)

print(shirt_one.color)
print(shirt_one.color)

shirt_two.change_price(300)
print(shirt_two.price)
