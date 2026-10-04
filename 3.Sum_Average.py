# Q3: Sum and Average Without sum()
# Why a for loop? We need to visit every item in a list exactly once,
# so "for number in numbers" is the simplest and clearest choice.

raw = input("Enter numbers separated by spaces: ")

numbers = []
for item in raw.split():
    try:
        numbers.append(float(item))
    except ValueError:
        print(f"'{item}' is not a valid number.")
        exit()

if len(numbers) == 0:
    print("The list is empty, so there is no total or average.")
    exit()

total = 0
for number in numbers:
    total += number

average = total / len(numbers)

print(f"\nNumbers: {numbers}")
print(f"Total: {total}")
print(f"Average: {average}")