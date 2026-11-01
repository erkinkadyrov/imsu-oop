"""Assignment 4 - UserUtil (static helper methods)."""
import random
import re
import string
from datetime import date

SPECIALS = "!@#$%^&*()-_=+"


class UserUtil:
    @staticmethod
    def generate_user_id():
        """9-digit id: first 2 digits = current year (e.g. '26'), rest random."""
        year_prefix = f"{date.today().year % 100:02d}"
        rest = "".join(random.choice(string.digits) for _ in range(7))
        return int(year_prefix + rest)

    @staticmethod
    def generate_password(length=12):
        """At least 8 chars with >=1 upper, lower, digit and special."""
        length = max(length, 8)
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(SPECIALS),
        ]
        pool = string.ascii_letters + string.digits + SPECIALS
        password += [random.choice(pool) for _ in range(length - 4)]
        random.shuffle(password)
        return "".join(password)

    @staticmethod
    def is_strong_password(password):
        return (
            len(password) >= 8
            and any(c.isupper() for c in password)
            and any(c.islower() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in SPECIALS for c in password)
        )

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain.lower()}"

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-z0-9]+\.[a-z0-9]+@[a-z0-9.-]+\.[a-z]{2,}$"
        return re.match(pattern, email) is not None
