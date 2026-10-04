# Q20: Final Challenge - Student Registration System
# Why functions? Each feature (add, view, search, update, delete, average, top)
#   is a separate job, so each gets its own small, reusable function.
# Why for loops? view_students, class_average and top_student must visit
#   every student record.
# Why a while loop? We don't know how many actions the user will perform;
#   the menu runs until the user chooses Exit.
# Data structure: a dictionary {id: {"name":..., "age":..., "marks":...}}
#   so searching, updating and deleting by ID need no loop.


def read_marks(prompt):
    """Keep asking until the user enters a number from 0 to 100. Returns a float."""
    while True:
        try:
            marks = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            continue
        return marks


def read_age(prompt):
    """Keep asking until the user enters a whole number from 1 to 120. Returns an int."""
    while True:
        try:
            age = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if age < 1 or age > 120:
            print("Age must be between 1 and 120.")
            continue
        return age


def add_student(students, student_id, name, age, marks):
    """Add a new student. Returns False if the ID already exists."""
    if student_id in students:
        return False
    students[student_id] = {"name": name, "age": age, "marks": marks}
    return True


def view_students(students):
    """Print all students in a table."""
    if len(students) == 0:
        print("No students registered yet.")
        return

    print(f"\n{'ID':<8}{'Name':<15}{'Age':>5}{'Marks':>9}")
    print("-" * 37)
    for student_id in students:
        s = students[student_id]
        print(f"{student_id:<8}{s['name']:<15}{s['age']:>5}{s['marks']:>9.2f}")
    print("-" * 37)
    print(f"Total students: {len(students)}")


def search_student(students, student_id):
    """Return the student's record, or None if the ID is not found."""
    return students.get(student_id)


def update_student(students, student_id, name, age, marks):
    """Update a student's details. A value of None means 'keep the old one'.
    Returns False if the ID is not found."""
    if student_id not in students:
        return False
    if name is not None:
        students[student_id]["name"] = name
    if age is not None:
        students[student_id]["age"] = age
    if marks is not None:
        students[student_id]["marks"] = marks
    return True


def delete_student(students, student_id):
    """Delete a student. Returns True if deleted, False if the ID is not found."""
    if student_id in students:
        del students[student_id]
        return True
    return False


def class_average(students):
    """Return the average marks of all students, or None if there are none."""
    if len(students) == 0:
        return None
    total = 0
    for student_id in students:
        total += students[student_id]["marks"]
    return total / len(students)


def top_student(students):
    """Return (id, record) of the student with the highest marks, or None if empty."""
    if len(students) == 0:
        return None

    best_id = None
    for student_id in students:
        if best_id is None or students[student_id]["marks"] > students[best_id]["marks"]:
            best_id = student_id
    return best_id, students[best_id]


def main():
    students = {}
    print("Welcome to the Student Registration System")

    while True:
        print("\n----- Menu -----")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by ID")
        print("4. Update student")
        print("5. Delete student")
        print("6. Class average marks")
        print("7. Highest-performing student")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            student_id = input("Student ID: ").strip()
            if student_id == "":
                print("ID cannot be empty.")
                continue
            if student_id in students:
                print(f"A student with ID '{student_id}' already exists.")
                continue
            name = input("Name: ").strip()
            if name == "":
                print("Name cannot be empty.")
                continue
            age = read_age("Age: ")
            marks = read_marks("Marks (0-100): ")
            add_student(students, student_id, name, age, marks)
            print(f"Student '{name}' added successfully.")

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            student_id = input("Enter student ID to search: ").strip()
            record = search_student(students, student_id)
            if record is None:
                print(f"No student found with ID '{student_id}'.")
            else:
                print(f"\nID: {student_id}")
                print(f"Name: {record['name']}")
                print(f"Age: {record['age']}")
                print(f"Marks: {record['marks']:.2f}")

        elif choice == "4":
            student_id = input("Enter student ID to update: ").strip()
            if search_student(students, student_id) is None:
                print(f"No student found with ID '{student_id}'.")
                continue

            print("Press Enter to keep the current value.")
            new_name = input("New name: ").strip()
            new_name = new_name if new_name != "" else None

            new_age = None
            age_text = input("New age: ").strip()
            if age_text != "":
                new_age = read_age("Confirm new age: ") if not age_text.isdigit() else int(age_text)
                if new_age < 1 or new_age > 120:
                    print("Age must be between 1 and 120. Age not changed.")
                    new_age = None

            new_marks = None
            marks_text = input("New marks (0-100): ").strip()
            if marks_text != "":
                try:
                    value = float(marks_text)
                    if 0 <= value <= 100:
                        new_marks = value
                    else:
                        print("Marks must be between 0 and 100. Marks not changed.")
                except ValueError:
                    print("Invalid marks. Marks not changed.")

            update_student(students, student_id, new_name, new_age, new_marks)
            print("Student details updated.")

        elif choice == "5":
            student_id = input("Enter student ID to delete: ").strip()
            if delete_student(students, student_id):
                print(f"Student with ID '{student_id}' deleted.")
            else:
                print(f"No student found with ID '{student_id}'.")

        elif choice == "6":
            average = class_average(students)
            if average is None:
                print("No students registered yet, so there is no average.")
            else:
                print(f"Class average marks: {average:.2f}")

        elif choice == "7":
            result = top_student(students)
            if result is None:
                print("No students registered yet.")
            else:
                student_id, record = result
                print(f"Top student: {record['name']} (ID {student_id}) with {record['marks']:.2f} marks")

        elif choice == "8":
            print("Thank you for using the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()