"""Assignment 5 - unit tests for the device hierarchy and the cart."""
import unittest

from cart import Cart
from catalog import build_catalog
from device import Device
from devices import Laptop, Smartphone, Tablet


class TestDevice(unittest.TestCase):
    def test_discount(self):
        d = Device("X", 100, 5, 12)
        d.apply_discount(10)
        self.assertAlmostEqual(d.price, 90.0)

    def test_availability_and_reduce(self):
        d = Device("X", 100, 5, 12)
        self.assertTrue(d.is_available(3))
        self.assertTrue(d.reduce_stock(3))
        self.assertEqual(d.stock, 2)
        self.assertFalse(d.reduce_stock(10))

    def test_inheritance(self):
        self.assertIsInstance(Smartphone("P", 1, 1, 1, 6.1, 20), Device)
        self.assertIsInstance(Laptop("L", 1, 1, 1, 16, 3.2), Device)
        self.assertIsInstance(Tablet("T", 1, 1, 1, "1x1", 400), Device)

    def test_subclass_methods(self):
        self.assertIn("calling", Smartphone("P", 1, 1, 1, 6.1, 20).make_call())
        self.assertIn("running", Laptop("L", 1, 1, 1, 16, 3.2).run_program())
        self.assertIn("browsing", Tablet("T", 1, 1, 1, "1x1", 400).browse_internet())


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.phone = Smartphone("P", 500, 5, 12, 6.1, 20)
        self.laptop = Laptop("L", 1000, 2, 24, 16, 3.2)

    def test_add_and_total(self):
        self.cart.add_device(self.phone, 2)
        self.cart.add_device(self.laptop, 1)
        self.assertEqual(self.cart.get_total_price(), 2000.0)

    def test_add_same_device_merges(self):
        self.cart.add_device(self.phone, 1)
        self.cart.add_device(self.phone, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.get_total_price(), 1500.0)

    def test_remove(self):
        self.cart.add_device(self.phone, 3)
        self.cart.remove_device(self.phone, 1)
        self.assertEqual(self.cart.get_total_price(), 1000.0)

    def test_checkout_reduces_stock(self):
        self.cart.add_device(self.phone, 2)
        self.assertTrue(self.cart.checkout())
        self.assertEqual(self.phone.stock, 3)
        self.assertEqual(self.cart.items, [])

    def test_checkout_blocked_when_insufficient_stock(self):
        self.cart.add_device(self.laptop, 5)  # only 2 in stock
        self.assertFalse(self.cart.checkout())


class TestCatalog(unittest.TestCase):
    def test_at_least_20_devices(self):
        self.assertGreaterEqual(len(build_catalog()), 20)


if __name__ == "__main__":
    unittest.main(verbosity=2)
