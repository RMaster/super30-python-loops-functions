# Q4: Find Maximum and Minimum Without max() / min()
# Why a for loop? We must look at every item in the list once and compare
# it with the best values found so far, so "for number in numbers" fits.

raw = input("Enter numbers separated by spaces: ")

numbers = []
for item in raw.split():
    try:
        numbers.append(float(item))
    except ValueError:
        print(f"'{item}' is not a valid number.")
        exit()

if len(numbers) == 0:
    print("The list is empty, so there is no maximum or minimum.")
    exit()

# Start with the first element, NOT with 0
largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print(f"\nNumbers: {numbers}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")