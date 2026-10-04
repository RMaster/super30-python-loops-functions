# Q14: Create Your Own sum() Function
# Why a function? The summing logic is reusable. Once written, we can call
# my_sum() with any list instead of rewriting the loop each time.
# Why a for loop inside it? We visit every item in the list exactly once.

def my_sum(numbers):
    """Return the sum of a list of numbers without using the built-in sum()."""
    total = 0                 # accumulator, starts at 0
    for number in numbers:
        total += number
    return total              # return the value, do not print it here


# ---------- Main program ----------
raw = input("Enter numbers separated by spaces: ")

numbers = []
for item in raw.split():
    try:
        numbers.append(float(item))
    except ValueError:
        print(f"'{item}' is not a valid number.")
        exit()

result = my_sum(numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {result}")

# ---------- Quick self-tests with hardcoded lists ----------
print("\nSelf-tests:")
print(my_sum([1, 2, 3, 4, 5]))     # 15
print(my_sum([10, -4, 6]))         # 12
print(my_sum([2.5, 3.5]))          # 6.0
print(my_sum([]))                  # 0
print(my_sum([7]))                 # 7