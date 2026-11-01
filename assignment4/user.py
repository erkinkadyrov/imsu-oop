"""Assignment 4 - User (instance fields and methods)."""
from datetime import date, datetime


class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = None
        self.password = None
        self.birthday = birthday  # a datetime or date

    def get_details(self):
        """Return a human-readable description of the user."""
        return (f"#{self.user_id} {self.name} {self.surname} "
                f"<{self.email}> born {self._birth_str()} (age {self.get_age()})")

    def get_age(self):
        """Age in whole years from the birthday to today."""
        b = self.birthday
        if isinstance(b, datetime):
            b = b.date()
        today = date.today()
        years = today.year - b.year
        if (today.month, today.day) < (b.month, b.day):
            years -= 1
        return years

    def _birth_str(self):
        b = self.birthday
        if isinstance(b, datetime):
            b = b.date()
        return b.isoformat()

    def __str__(self):
        return self.get_details()
