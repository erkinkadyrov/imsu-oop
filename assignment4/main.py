"""Assignment 4 - small demo tying the three classes together."""
from datetime import datetime

from user import User
from user_service import UserService
from user_util import UserUtil


def main():
    uid = UserUtil.generate_user_id()
    user = User(uid, "John", "Doe", datetime(2001, 3, 15))
    user.email = UserUtil.generate_email(user.name, user.surname, "imsu.edu.kg")
    user.password = UserUtil.generate_password()

    UserService.add_user(user)

    print("Generated id :", uid)
    print("Email        :", user.email, "valid:", UserUtil.validate_email(user.email))
    print("Password     :", user.password, "strong:", UserUtil.is_strong_password(user.password))
    print("Details      :", user.get_details())
    print("Users stored :", UserService.get_number())


if __name__ == "__main__":
    main()
