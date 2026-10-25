"""Assignment 3 - Amount: a single transaction record."""
from datetime import datetime


class Amount:
    """One money movement on an account."""

    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"

    def __init__(self, amount, transaction_type, timestamp=None):
        self.amount = float(amount)
        self.transaction_type = transaction_type
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
        when = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{when}] {self.transaction_type:<10} {self.amount:>10.2f}"
