# Assignment 3 - Personal account

Two classes:

- `Amount` (amount.py) - one transaction: amount, timestamp and type
  (DEPOSIT or WITHDRAWAL).
- `PersonalAccount` (personal_account.py) - the account, keeps a balance and a
  list of Amount objects.

The balance starts at 0. `deposit()` adds an Amount of type DEPOSIT and raises
the balance, `withdraw()` adds a WITHDRAWAL and lowers it, but it does not let
you withdraw more than the balance. I also overloaded `+` and `-` so that
`account + 100` is the same as deposit and `account - 50` the same as withdraw.

`main.py` is a small demo (deposit, withdraw, check balance, print history).
Tests are in test_account.py.

UML:

```mermaid
classDiagram
    class Amount {
        + amount : float
        + timestamp : datetime
        + transaction_type : str
        + __init__(amount, transaction_type, timestamp)
        + __str__() str
    }
    class PersonalAccount {
        + account_number : int
        + account_holder : str
        + balance : float
        + transactions : list~Amount~
        + deposit(amount)
        + withdraw(amount)
        + print_transaction_history()
        + get_balance() float
        + __add__(amount)
        + __sub__(amount)
        + __str__() str
    }
    PersonalAccount "1" o-- "many" Amount : records
```

Run:

```bash
python3 main.py
python3 -m unittest -v
```
