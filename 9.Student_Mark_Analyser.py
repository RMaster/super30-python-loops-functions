# Q9: Student Marks Analyzer
# Why a for loop? We must visit every student's mark once, and one loop
# can update the total, highest, lowest, and pass/fail counts together.

PASS_MARK = 40

raw = input("Enter students' marks separated by spaces: ")

marks = []
for item in raw.split():
    try:
        mark = float(item)
    except ValueError:
        print(f"'{item}' is not a valid mark.")
        exit()
    if mark < 0 or mark > 100:
        print(f"{mark} is out of range. Marks must be between 0 and 100.")
        exit()
    marks.append(mark)

if len(marks) == 0:
    print("No marks entered, so there is nothing to analyze.")
    exit()

# Start with the first mark, NOT with 0 (same idea as Q4)
highest = marks[0]
lowest = marks[0]
total = 0
passed = 0
failed = 0

for mark in marks:
    total += mark

    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

    if mark >= PASS_MARK:
        passed += 1
    else:
        failed += 1

average = total / len(marks)

print(f"\nMarks: {marks}")
print(f"Number of students: {len(marks)}")
print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")
print(f"Average marks: {average:.2f}")
print(f"Passed (>= {PASS_MARK}): {passed}")
print(f"Failed (< {PASS_MARK}): {failed}")