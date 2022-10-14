class Clothing:

    def __init__(self, color, size, style, price):
        self._color = color
        self._size = size
        self._style = style
        self._price = price

    def change_price(self, price):
        self._price = price

    def calculate_discount(self, discount):
        return self._price * (1 - discount)

    def calculate_shipping(self, weight, rate):
      self._weight = weight
      self._rate = rate

      return self._rate * self._weight



class Shirt(Clothing):

    def __init__(self, color, size, style, price, long_or_short):

        Clothing.__init__(self, color, size, style, price)
        self._long_or_short = long_or_short

    def double_price(self):
        self._price = 2 * self._price


class Pants(Clothing):

    def __init__(self, color, size, style, price, waist):

        Clothing.__init__(self, color, size, style, price)
        self._waist = waist

    def calculate_discount(self, discount):
        return self.price * (1 - discount / 2)

class Blouse(Clothing):

  def __init__(self, color, size, style, price, country_of_origin):
    Clothing.__init__(self, color, size, style, price)
    self._country_of_origin = country_of_origin

  def triple_price(self):
    return self._price * 3