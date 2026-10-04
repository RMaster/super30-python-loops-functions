# Q8: Pattern Generator
# Why nested for loops? The outer loop handles the rows (N rows),
# and the inner loop handles the numbers in each row (i numbers in row i).
# Both counts are known in advance, so for + range() fits.

try:
    n = int(input("Enter the number of rows (N): "))
except ValueError:
    print("Please enter a valid whole number.")
    exit()

if n < 1:
    print("Please enter a number greater than 0.")
    exit()

print()
for i in range(1, n + 1):          # outer loop: rows
    for j in range(1, i + 1):      # inner loop: numbers in this row
        print(j, end=" ")
    print()                        # newline after each row