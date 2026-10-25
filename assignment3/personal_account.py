"""Assignment 3 - PersonalAccount."""
from amount import Amount


class PersonalAccount:
    """A personal bank account that tracks a balance and a transaction log."""

    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        """Add money: records a DEPOSIT and increases the balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        tx = Amount(amount, Amount.DEPOSIT)
        self.transactions.append(tx)
        self.balance += amount
        return tx

    def withdraw(self, amount):
        """Take money: records a WITHDRAWAL and decreases the balance.

        Refuses to withdraw more than the current balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            print(f"Declined: cannot withdraw {amount:.2f}, balance is {self.balance:.2f}")
            return None
        tx = Amount(amount, Amount.WITHDRAWAL)
        self.transactions.append(tx)
        self.balance -= amount
        return tx

    def print_transaction_history(self):
        print(f"Transaction history for account {self.account_number}:")
        if not self.transactions:
            print("  (no transactions)")
        for tx in self.transactions:
            print(f"  {tx}")

    # getters / setters
    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, value):
        self.account_number = value

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, value):
        self.account_holder = value

    # operator overloading
    def __add__(self, amount):
        """account + amount  ==  deposit(amount)."""
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        """account - amount  ==  withdraw(amount)."""
        self.withdraw(amount)
        return self

    def __str__(self):
        return (f"Account #{self.account_number} ({self.account_holder}), "
                f"balance = {self.balance:.2f}, "
                f"{len(self.transactions)} transaction(s)")
