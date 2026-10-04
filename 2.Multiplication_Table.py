# Q2: Multiplication Table Generator
# Why a for loop? The number of rows is known before the loop starts
# (10 in Part 1, the user's end value in Part 2), so for + range() fits.

# ---------- Part 1: fixed range (1 to 10) ----------
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid whole number.")
    exit()

print(f"\nMultiplication table of {n} (1 to 10):")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# ---------- Part 2: user-defined range ----------
try:
    end = int(input("\nEnter the ending value for the table: "))
except ValueError:
    print("Please enter a valid whole number.")
    exit()

if end < 1:
    print("The ending value must be at least 1.")
    exit()

print(f"\nMultiplication table of {n} (1 to {end}):")
for i in range(1, end + 1):
    print(f"{n} x {i} = {n * i}")