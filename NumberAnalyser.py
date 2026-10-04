# Q1: Number Analyzer
# Why a for loop? We know in advance how many numbers to process (1 to N),
# so a for loop with range() is the natural choice.

try:
    n = int(input("Enter a number N: "))
except ValueError:
    print("Please enter a valid whole number.")
    exit()

if n < 1:
    print("Please enter a number greater than 0.")
    exit()

even_count = 0
odd_count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"{i} is Even")
        even_count += 1
    else:
        print(f"{i} is Odd")
        odd_count += 1

print("\n--- Summary ---")
print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")