# Q16: Student Grade Function
# Why a function? Grading logic is reusable for any student, and it RETURNS
# results so the caller decides how to display them.
# Why a for loop inside? We process exactly five marks (a known count).
#
# Grading rules:
#   Percentage >= 80  -> A
#   Percentage >= 65  -> B
#   Percentage >= 50  -> C
#   Percentage >= 40  -> D
#   Below 40          -> Fail
#   Extra rule: any single subject below 40 -> Fail

SUBJECT_COUNT = 5
MAX_MARK = 100
PASS_MARK = 40


def calculate_grade(marks):
    """Validate five marks and return a dictionary with total, percentage and grade.
    If the marks are invalid, return a dictionary with an 'error' key instead."""
    if len(marks) != SUBJECT_COUNT:
        return {"error": f"Exactly {SUBJECT_COUNT} marks are required."}

    total = 0
    failed_subject = False

    for mark in marks:
        if mark < 0 or mark > MAX_MARK:
            return {"error": f"Invalid mark {mark}. Marks must be between 0 and {MAX_MARK}."}
        total += mark
        if mark < PASS_MARK:
            failed_subject = True

    percentage = total / (SUBJECT_COUNT * MAX_MARK) * 100

    if failed_subject:
        grade = "Fail"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 65:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    return {"total": total, "percentage": percentage, "grade": grade}


# ---------- Main program ----------
marks = []
for i in range(1, SUBJECT_COUNT + 1):
    try:
        marks.append(float(input(f"Enter marks for subject {i}: ")))
    except ValueError:
        print("Please enter a valid number.")
        exit()

result = calculate_grade(marks)

if "error" in result:
    print(f"\nError: {result['error']}")
else:
    print(f"\nTotal: {result['total']} / {SUBJECT_COUNT * MAX_MARK}")
    print(f"Percentage: {result['percentage']:.2f}%")
    print(f"Grade: {result['grade']}")

# ---------- Quick self-tests ----------
print("\nSelf-tests:")
print(calculate_grade([90, 85, 88, 92, 80]))   # A
print(calculate_grade([70, 68, 72, 66, 69]))   # B
print(calculate_grade([55, 60, 52, 58, 50]))   # C
print(calculate_grade([45, 42, 48, 41, 44]))   # D
print(calculate_grade([90, 90, 90, 90, 30]))   # Fail (one subject below 40)
print(calculate_grade([90, 90, 90, 90, 101]))  # error
print(calculate_grade([50, 60, 70]))           # error