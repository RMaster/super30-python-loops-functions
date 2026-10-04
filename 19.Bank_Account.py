# Q19: Bank Account Mini Application
# Why functions? Each banking action (deposit, withdraw, balance, history) is a
# separate job with its own rules, so each gets its own function.
# Why a while loop? We don't know how many actions the user will perform;
# the program runs until the user chooses Exit.
# Why a for loop? transaction_history() visits every record in the history list.


def deposit(account, amount):
    """Add money to the account. Returns (success, message)."""
    if amount <= 0:
        return False, "Deposit amount must be greater than zero."

    account["balance"] += amount
    account["history"].append(
        f"Deposit:    +₹{amount:,.2f} | Balance: ₹{account['balance']:,.2f}"
    )
    return True, f"₹{amount:,.2f} deposited successfully."


def withdraw(account, amount):
    """Take money out of the account. Blocks the withdrawal if the balance is too low.
    Returns (success, message)."""
    if amount <= 0:
        return False, "Withdrawal amount must be greater than zero."
    if amount > account["balance"]:
        return False, (
            f"Insufficient balance. You tried to withdraw ₹{amount:,.2f} "
            f"but have only ₹{account['balance']:,.2f}."
        )

    account["balance"] -= amount
    account["history"].append(
        f"Withdrawal: -₹{amount:,.2f} | Balance: ₹{account['balance']:,.2f}"
    )
    return True, f"₹{amount:,.2f} withdrawn successfully."


def check_balance(account):
    """Return the current balance."""
    return account["balance"]


def transaction_history(account):
    """Print every recorded transaction in order."""
    if len(account["history"]) == 0:
        print("No transactions yet.")
        return

    print("\n----- Transaction History -----")
    number = 1
    for record in account["history"]:
        print(f"{number}. {record}")
        number += 1


def main():
    account = {"balance": 0.0, "history": []}
    print("Welcome to the Bank Account Application")

    while True:
        print("\n----- Bank Menu -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1" or choice == "2":
            try:
                amount = float(input("Enter amount: ₹"))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            if choice == "1":
                success, message = deposit(account, amount)
            else:
                success, message = withdraw(account, amount)

            print(message if success else f"Error: {message}")
            if success:
                print(f"Current balance: ₹{check_balance(account):,.2f}")

        elif choice == "3":
            print(f"Current balance: ₹{check_balance(account):,.2f}")

        elif choice == "4":
            transaction_history(account)

        elif choice == "5":
            print("Thank you for banking with us. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()