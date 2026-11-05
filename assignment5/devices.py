"""Assignment 5 - Device subclasses: Smartphone, Laptop, Tablet."""
from device import Device


class Smartphone(Device):
    def __init__(self, name, price, stock, warranty, screen_size, battery_life):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def display_info(self):
        super().display_info()
        print(f"    screen:{self.screen_size}\"  battery:{self.battery_life}h")

    def make_call(self):
        return f"{self.name} is calling..."

    def install_app(self, app="an app"):
        return f"{self.name} installed {app}."

    def __str__(self):
        return f"Smartphone {self.name} ({self.screen_size}\", ${self.price:.2f})"


class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def display_info(self):
        super().display_info()
        print(f"    ram:{self.ram_size}GB  cpu:{self.processor_speed}GHz")

    def run_program(self, program="a program"):
        return f"{self.name} is running {program}."

    def use_keyboard(self):
        return f"Typing on {self.name}."

    def __str__(self):
        return f"Laptop {self.name} ({self.ram_size}GB RAM, ${self.price:.2f})"


class Tablet(Device):
    def __init__(self, name, price, stock, warranty, screen_resolution, weight):
        super().__init__(name, price, stock, warranty)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def display_info(self):
        super().display_info()
        print(f"    resolution:{self.screen_resolution}  weight:{self.weight}g")

    def browse_internet(self):
        return f"{self.name} is browsing the internet."

    def use_touchscreen(self):
        return f"Tapping on {self.name}'s screen."

    def __str__(self):
        return f"Tablet {self.name} ({self.screen_resolution}, ${self.price:.2f})"
