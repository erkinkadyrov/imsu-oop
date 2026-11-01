# Assignment 4 - User class methods

Three classes, each showing a different kind of method:

- `User` (user.py) - normal instance fields and methods (`get_details`,
  `get_age`).
- `UserService` (user_service.py) - a class attribute `users` (a dict) and class
  methods to add, find, delete, update users and count them.
- `UserUtil` (user_util.py) - only static methods.

What UserUtil does:

- `generate_user_id()` - 9 digits, first two are the current year (like 26...).
- `generate_password()` - at least 8 chars with an upper, a lower, a digit and a
  special character.
- `is_strong_password()` - checks the same rules.
- `generate_email(name, surname, domain)` - gives `name.surname@domain` in lower
  case.
- `validate_email()` - checks the `name.surname@domain.tld` format.

Tests are in test_users.py (TestUser, TestUserService, TestUserUtil).

UML:

```mermaid
classDiagram
    class User {
        + user_id : int
        + name : str
        + surname : str
        + email : str
        + password : str
        + birthday : datetime
        + get_details() str
        + get_age() int
    }
    class UserService {
        + users : dict$
        + add_user(user)$
        + find_user(user_id)$
        + delete_user(user_id)$
        + update_user(user_id, user_update)$
        + get_number() int$
    }
    class UserUtil {
        + generate_user_id() int$
        + generate_password() str$
        + is_strong_password(password) bool$
        + generate_email(name, surname, domain) str$
        + validate_email(email) bool$
    }
    UserService ..> User
    UserUtil ..> User
```

Run:

```bash
python3 main.py
python3 -m unittest -v
```
