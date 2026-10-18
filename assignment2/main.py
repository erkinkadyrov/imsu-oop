"""Assignment 2 - main program.

Asks the user for N students, creates them using both constructors,
stores them in a list and calls display_info() on each one.
"""
from student import Student


def main():
    students = []
    n = int(input("How many students? "))

    for i in range(n):
        print(f"\nStudent #{i + 1}")
        name = input("  Name: ")
        student_id = input("  Student ID: ")
        major = input("  Major: ")
        gpa_raw = input("  GPA (leave empty for a blank record): ").strip()

        if gpa_raw == "":
            # default constructor, then fill nothing - blank student
            student = Student.default()
            student.name = name or None
        else:
            # parameterized constructor
            student = Student(name, student_id, major, float(gpa_raw))

        students.append(student)

    print("\n===== All students =====")
    for student in students:
        student.display_info()


if __name__ == "__main__":
    main()
