"""Assignment 5 - shopping application with a menu."""
from cart import Cart
from catalog import build_catalog


def show_devices(devices, cart):
    print("\n===== Devices =====")
    for i, device in enumerate(devices, start=1):
        print(f"\n#{i}")
        device.display_info()

    choice = input("\nEnter a device number to add to cart (or Enter to go back): ").strip()
    if not choice:
        return
    index = int(choice) - 1
    if 0 <= index < len(devices):
        amount = int(input("Quantity: "))
        cart.add_device(devices[index], amount)
        print(f"Added {amount} x {devices[index].name} to the cart.")
    else:
        print("No such device.")


def show_cart(cart):
    print("\n===== Cart =====")
    cart.print_items()
    if cart.items and input("Checkout now? (y/n): ").strip().lower() == "y":
        cart.checkout()


def main():
    devices = build_catalog()
    cart = Cart()

    while True:
        print("\n========== MENU ==========")
        print("#1 Show Devices")
        print("#2 Show Cart")
        print("#3 Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            show_devices(devices, cart)
        elif choice == "2":
            show_cart(cart)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
