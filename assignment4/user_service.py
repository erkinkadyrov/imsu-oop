"""Assignment 4 - UserService (class methods + class attribute)."""


class UserService:
    # class attribute: user_id -> User
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user
        return user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id)

    @classmethod
    def delete_user(cls, user_id):
        return cls.users.pop(user_id, None)

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id not in cls.users:
            return None
        user_update.user_id = user_id
        cls.users[user_id] = user_update
        return user_update

    @classmethod
    def get_number(cls):
        return len(cls.users)
