# Q7: Prime Number Finder
# Why nested for loops? The outer loop goes through every number in the range
# (known count), and the inner loop checks divisors of that number (also a
# known range), so for + range() fits both.

try:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
except ValueError:
    print("Please enter valid whole numbers.")
    exit()

if start > end:
    print("The starting number must not be greater than the ending number.")
    exit()

print(f"\nPrime numbers between {start} and {end}:")
found_any = False

for num in range(start, end + 1):
    if num < 2:
        continue  # 0, 1 and negatives are not prime

    is_prime = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break  # one divisor is enough to rule it out

    if is_prime:
        print(num, end=" ")
        found_any = True

if not found_any:
    print("No prime numbers found in this range.")
else:
    print()  # newline after the row of primes