# Q13: Menu-Driven Calculator
# Why a while loop? We don't know how many calculations the user will do.
# The program must keep running until the user chooses Exit, so
# "while True" with a break on Exit is the right choice.

print("Welcome to the Calculator")

while True:
    print("\n----- Calculator Menu -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "6":
        print("Thank you for using the calculator. Goodbye!")
        break

    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid choice. Please enter a number from 1 to 6.")
        continue

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid number. Please try again.")
        continue

    if choice == "1":
        print(f"Result: {a} + {b} = {a + b}")

    elif choice == "2":
        print(f"Result: {a} - {b} = {a - b}")

    elif choice == "3":
        print(f"Result: {a} x {b} = {a * b}")

    elif choice == "4":
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {a} / {b} = {a / b}")

    elif choice == "5":
        if b == 0:
            print("Error: Modulus by zero is not allowed.")
        else:
            print(f"Result: {a} % {b} = {a % b}")