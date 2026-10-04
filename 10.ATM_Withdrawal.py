# Q10: ATM Withdrawal Simulator
# Why a while loop? We don't know how many transactions the user will make.
# The program must keep running until the user explicitly chooses Exit,
# so "while True" with a break on Exit is the right choice.

balance = 10000

print("Welcome to the ATM")

while True:
    print("\n----- ATM Menu -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is ₹{balance:,.2f}")

    elif choice == "2":
        try:
            amount = float(input("Enter amount to deposit: ₹"))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            balance += amount
            print(f"₹{amount:,.2f} deposited successfully.")
            print(f"New balance: ₹{balance:,.2f}")

    elif choice == "3":
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance. Withdrawal declined.")
        else:
            balance -= amount
            print(f"₹{amount:,.2f} withdrawn successfully.")
            print(f"New balance: ₹{balance:,.2f}")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")