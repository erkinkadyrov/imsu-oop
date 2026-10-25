"""Assignment 3 - demo program."""
from personal_account import PersonalAccount


def main():
    account = PersonalAccount(account_number=1001, account_holder="Erkin Kadyrov")
    print(account)

    print("\nDeposit 500, deposit 250.50")
    account.deposit(500)
    account.deposit(250.50)
    print("Balance:", account.get_balance())

    print("\nWithdraw 300")
    account.withdraw(300)
    print("Balance:", account.get_balance())

    print("\nTry to withdraw 1000 (more than balance)")
    account.withdraw(1000)
    print("Balance:", account.get_balance())

    print("\nUsing operators:  account + 100,  account - 50")
    account + 100
    account - 50
    print("Balance:", account.get_balance())

    print()
    account.print_transaction_history()
    print()
    print(account)


if __name__ == "__main__":
    main()
