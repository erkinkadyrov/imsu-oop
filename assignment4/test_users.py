"""Assignment 4 - unit tests for User, UserService, UserUtil."""
import unittest
from datetime import datetime

from user import User
from user_service import UserService
from user_util import UserUtil


class TestUser(unittest.TestCase):
    def test_get_age(self):
        user = User(1, "Ivan", "Petrov", datetime(2000, 1, 1))
        self.assertGreaterEqual(user.get_age(), 25)

    def test_get_details_contains_name(self):
        user = User(1, "Ivan", "Petrov", datetime(2000, 1, 1))
        self.assertIn("Ivan", user.get_details())


class TestUserService(unittest.TestCase):
    def setUp(self):
        UserService.users = {}

    def test_add_and_find(self):
        user = User(10, "A", "B", datetime(1990, 5, 5))
        UserService.add_user(user)
        self.assertIs(UserService.find_user(10), user)

    def test_get_number(self):
        UserService.add_user(User(1, "A", "B", datetime(1990, 5, 5)))
        UserService.add_user(User(2, "C", "D", datetime(1991, 5, 5)))
        self.assertEqual(UserService.get_number(), 2)

    def test_delete(self):
        UserService.add_user(User(3, "A", "B", datetime(1990, 5, 5)))
        UserService.delete_user(3)
        self.assertIsNone(UserService.find_user(3))

    def test_update(self):
        UserService.add_user(User(4, "Old", "Name", datetime(1990, 5, 5)))
        UserService.update_user(4, User(4, "New", "Name", datetime(1990, 5, 5)))
        self.assertEqual(UserService.find_user(4).name, "New")


class TestUserUtil(unittest.TestCase):
    def test_user_id_is_9_digits_with_year(self):
        uid = str(UserUtil.generate_user_id())
        self.assertEqual(len(uid), 9)
        self.assertTrue(uid.startswith(str(datetime.now().year % 100).zfill(2)))

    def test_generated_password_is_strong(self):
        for _ in range(20):
            self.assertTrue(UserUtil.is_strong_password(UserUtil.generate_password()))

    def test_weak_password_rejected(self):
        self.assertFalse(UserUtil.is_strong_password("abc"))
        self.assertFalse(UserUtil.is_strong_password("alllowercase1!"))

    def test_generate_email(self):
        self.assertEqual(
            UserUtil.generate_email("John", "Doe", "Example.com"),
            "john.doe@example.com",
        )

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("john.doe@example.com"))
        self.assertFalse(UserUtil.validate_email("johndoe@example.com"))
        self.assertFalse(UserUtil.validate_email("john.doe@com"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
