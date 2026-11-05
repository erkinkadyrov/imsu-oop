# Assignment 5 - Device shopping cart

Inheritance example.

- `Device` (device.py) - base class with name, price, stock, warranty and
  methods like apply_discount, is_available, reduce_stock.
- `Smartphone`, `Laptop`, `Tablet` (devices.py) - subclasses, each adds its own
  fields and methods and overrides display_info.
- `Cart` (cart.py) - holds (device, amount) pairs, can add/remove items, give the
  total price and checkout (it checks stock, lowers it and prints a receipt).
- `catalog.py` - 21 ready devices.
- `main.py` - the menu app: #1 show devices, #2 show cart, #3 exit.

Tests are in test_shop.py.

UML:

```mermaid
classDiagram
    class Device {
        + name : str
        + price : float
        + stock : int
        + warranty_period : int
        + display_info()
        + apply_discount(pct)
        + is_available(amount) bool
        + reduce_stock(amount) bool
    }
    class Smartphone {
        + screen_size
        + battery_life
        + make_call()
        + install_app()
    }
    class Laptop {
        + ram_size
        + processor_speed
        + run_program()
        + use_keyboard()
    }
    class Tablet {
        + screen_resolution
        + weight
        + browse_internet()
        + use_touchscreen()
    }
    class Cart {
        + items : list
        + total_price : float
        + add_device(device, amount)
        + remove_device(device, amount)
        + get_total_price() float
        + print_items()
        + checkout() bool
    }
    Device <|-- Smartphone
    Device <|-- Laptop
    Device <|-- Tablet
    Cart o-- Device
```

Run:

```bash
python3 main.py
python3 -m unittest -v
```
