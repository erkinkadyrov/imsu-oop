"""Assignment 3 - unit tests."""
import unittest

from amount import Amount
from personal_account import PersonalAccount


class TestAmount(unittest.TestCase):
    def test_fields(self):
        a = Amount(100, Amount.DEPOSIT)
        self.assertEqual(a.amount, 100.0)
        self.assertEqual(a.transaction_type, "DEPOSIT")

    def test_str_contains_type(self):
        self.assertIn("DEPOSIT", str(Amount(10, Amount.DEPOSIT)))


class TestPersonalAccount(unittest.TestCase):
    def setUp(self):
        self.account = PersonalAccount(1, "Tester")

    def test_starts_at_zero(self):
        self.assertEqual(self.account.get_balance(), 0.0)

    def test_deposit(self):
        self.account.deposit(200)
        self.assertEqual(self.account.get_balance(), 200.0)
        self.assertEqual(len(self.account.transactions), 1)

    def test_withdraw(self):
        self.account.deposit(200)
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 150.0)

    def test_overdraw_is_refused(self):
        self.account.deposit(100)
        result = self.account.withdraw(500)
        self.assertIsNone(result)
        self.assertEqual(self.account.get_balance(), 100.0)

    def test_add_operator_deposits(self):
        self.account + 300
        self.assertEqual(self.account.get_balance(), 300.0)

    def test_sub_operator_withdraws(self):
        self.account.deposit(300)
        self.account - 100
        self.assertEqual(self.account.get_balance(), 200.0)

    def test_setters(self):
        self.account.set_account_holder("New Holder")
        self.account.set_account_number(999)
        self.assertEqual(self.account.get_account_holder(), "New Holder")
        self.assertEqual(self.account.get_account_number(), 999)


if __name__ == "__main__":
    unittest.main(verbosity=2)
