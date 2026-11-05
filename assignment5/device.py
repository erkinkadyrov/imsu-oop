"""Assignment 5 - base class Device."""


class Device:
    def __init__(self, name, price, stock, warranty):
        self.name = name
        self.price = float(price)
        self.stock = int(stock)
        self.warranty_period = warranty  # in months

    def display_info(self):
        print(f"{self.name:<22} ${self.price:>8.2f}  stock:{self.stock:<3} "
              f"warranty:{self.warranty_period}m")

    def apply_discount(self, discount_percentage):
        self.price -= self.price * discount_percentage / 100
        return self.price

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        if not self.is_available(amount):
            return False
        self.stock -= amount
        return True

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"
