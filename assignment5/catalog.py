"""Assignment 5 - a catalog of 20+ devices."""
from devices import Laptop, Smartphone, Tablet


def build_catalog():
    return [
        Smartphone("iPhone 15", 999, 10, 12, 6.1, 20),
        Smartphone("iPhone 15 Pro", 1199, 7, 12, 6.1, 23),
        Smartphone("Samsung Galaxy S24", 899, 12, 24, 6.2, 22),
        Smartphone("Google Pixel 8", 699, 9, 12, 6.2, 24),
        Smartphone("Xiaomi 14", 799, 15, 18, 6.36, 22),
        Smartphone("OnePlus 12", 749, 8, 24, 6.82, 26),
        Smartphone("Nothing Phone 2", 599, 6, 12, 6.7, 20),

        Laptop("MacBook Air M3", 1299, 5, 12, 16, 3.5),
        Laptop("MacBook Pro 14", 1999, 4, 12, 18, 4.0),
        Laptop("Dell XPS 13", 1099, 8, 24, 16, 3.2),
        Laptop("Lenovo ThinkPad X1", 1499, 6, 36, 32, 3.4),
        Laptop("HP Spectre x360", 1249, 7, 24, 16, 3.3),
        Laptop("Asus ROG Zephyrus", 1799, 5, 24, 32, 4.5),
        Laptop("Acer Swift 3", 699, 11, 12, 8, 2.8),

        Tablet("iPad Air", 599, 10, 12, "2360x1640", 462),
        Tablet("iPad Pro 12.9", 1099, 6, 12, "2732x2048", 682),
        Tablet("Samsung Tab S9", 799, 9, 24, "2560x1600", 498),
        Tablet("Xiaomi Pad 6", 399, 14, 18, "2880x1800", 490),
        Tablet("Lenovo Tab P12", 349, 12, 12, "2944x1840", 615),
        Tablet("Huawei MatePad 11", 449, 8, 12, "2560x1600", 485),
        Tablet("Amazon Fire Max 11", 229, 20, 12, "2000x1200", 490),
    ]
