class Pants:

    def __init__(self, pant_color, pant_waist_size, pant_length, pant_price):
        self._color = pant_color
        self._waist_size = pant_waist_size
        self._length = pant_length
        self._price = pant_price

    def change_price(self, new_price):
        self._price = new_price

    def discount(self, percentage):
        return self._price * (1 - percentage)


class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary):
      self._first_name = first_name
      self._last_name = last_name
      self._employee_id = employee_id
      self._salary = salary
      self._pants_sold = []
      self._total_sales = 0

    def sell_pant(self, pants_object):
      self._pants_sold.append(pants_object)

    def display_sales
