"""Assignment 5 - shopping Cart."""


class Cart:
    def __init__(self):
        self.items = []  # list of (device, amount)
        self.total_price = 0.0

    def add_device(self, device, amount):
        for i, (dev, qty) in enumerate(self.items):
            if dev is device:
                self.items[i] = (dev, qty + amount)
                break
        else:
            self.items.append((device, amount))
        self._recalculate()

    def remove_device(self, device, amount):
        for i, (dev, qty) in enumerate(self.items):
            if dev is device:
                new_qty = qty - amount
                if new_qty > 0:
                    self.items[i] = (dev, new_qty)
                else:
                    self.items.pop(i)
                break
        self._recalculate()

    def get_total_price(self):
        return self.total_price

    def _recalculate(self):
        self.total_price = sum(dev.price * qty for dev, qty in self.items)

    def print_items(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("Cart contents:")
        for dev, qty in self.items:
            print(f"  {dev.name:<22} x{qty:<3} = ${dev.price * qty:.2f}")
        print(f"  {'TOTAL':<22}       = ${self.get_total_price():.2f}")

    def checkout(self):
        """Verify availability, reduce stock, print a receipt."""
        for dev, qty in self.items:
            if not dev.is_available(qty):
                print(f"Cannot checkout: not enough stock of {dev.name} "
                      f"(need {qty}, have {dev.stock}).")
                return False

        print("\n===== RECEIPT =====")
        for dev, qty in self.items:
            dev.reduce_stock(qty)
            print(f"  {dev.name:<22} x{qty:<3} = ${dev.price * qty:.2f}")
        print(f"  {'TOTAL':<22}       = ${self.get_total_price():.2f}")
        print("===================\n")

        self.items = []
        self.total_price = 0.0
        return True
