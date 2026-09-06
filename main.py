import argparse

from student import Student
from manager import StudentManager


def create_parser():
    parser = argparse.ArgumentParser(
        description="Student Record Management and Search System"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path of the student data file"
    )

    parser.add_argument(
        "--format",
        required=True,
        choices=["txt", "csv", "json"],
        help="Format of the student data file"
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    manager = StudentManager()

    manager.load_from_file(args.file, args.format)

    print("\nStudents loaded successfully.")
    print("Number of students:", len(manager.students))

    menu(manager, args.file, args.format)


def menu(manager, filename, file_format):

    while True:

        print("\n" + "=" * 50)
        print("       STUDENT RECORD MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Display all students")
        print("2. Add a new student")
        print("3. Search student by ID")
        print("4. Search students by Name")
        print("5. Search students by Department")
        print("6. Search students by Average")
        print("7. Update student marks")
        print("8. Remove student")
        print("9. Save students to file")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            manager.display_all_students()

        elif choice == "2":
            add_student(manager)

        elif choice == "3":
            search_by_id(manager)

        elif choice == "4":
            search_by_name(manager)

        elif choice == "5":
            search_by_department(manager)

        elif choice == "6":
            search_by_average(manager)

        elif choice == "7":
            update_student_marks(manager)

        elif choice == "8":
            remove_student(manager)

        elif choice == "9":
            save_students(manager, filename, file_format)

        elif choice == "10":
            print("\nProgram terminated.")
            break

        else:
            print("\nInvalid choice. Please try again.")


def add_student(manager):

    print("\n--- Add New Student ---")

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    semester = int(input("Enter Semester: "))

    subject1 = float(input("Enter Subject 1 marks: "))
    subject2 = float(input("Enter Subject 2 marks: "))
    subject3 = float(input("Enter Subject 3 marks: "))

    student = Student(
        student_id,
        name,
        department,
        semester,
        subject1,
        subject2,
        subject3
    )

    manager.add_student(student)

    print("\nStudent added successfully.")


def search_by_id(manager):

    print("\n--- Search by Student ID ---")

    student_id = int(input("Enter Student ID: "))

    student = manager.search_student(student_id)

    if student is not None:
        print("\nStudent found:")
        print(student.display_student())
    else:
        print("\nStudent not found.")


def search_by_name(manager):

    print("\n--- Search by Name ---")

    name = input("Enter student name: ")

    results = manager.search_by_name(name)

    if len(results) > 0:
        print("\nStudents found:")

        for student in results:
            print(student.display_student())
            print("-" * 40)

    else:
        print("\nNo students found.")


def search_by_department(manager):

    print("\n--- Search by Department ---")

    department = input("Enter department: ")

    results = manager.search_by_department(department)

    if len(results) > 0:
        print("\nStudents found:")

        for student in results:
            print(student.display_student())
            print("-" * 40)

    else:
        print("\nNo students found.")


def search_by_average(manager):

    print("\n--- Search by Average Marks ---")

    minimum_average = float(
        input("Enter minimum average marks: ")
    )

    results = manager.search_by_average(minimum_average)

    if len(results) > 0:
        print(
            f"\nStudents having average above "
            f"{minimum_average}:"
        )

        for student in results:
            print(student.display_student())
            print("-" * 40)

    else:
        print("\nNo students found.")


def update_student_marks(manager):

    print("\n--- Update Student Marks ---")

    student_id = int(input("Enter Student ID: "))

    student = manager.search_student(student_id)

    if student is None:
        print("\nStudent not found.")
        return

    print("\nCurrent student information:")
    print(student.display_student())

    subject1 = float(input("\nEnter new Subject 1 marks: "))
    subject2 = float(input("Enter new Subject 2 marks: "))
    subject3 = float(input("Enter new Subject 3 marks: "))

    student.update_marks(
        subject1,
        subject2,
        subject3
    )

    print("\nMarks updated successfully.")


def remove_student(manager):

    print("\n--- Remove Student ---")

    student_id = int(input("Enter Student ID: "))

    removed = manager.remove_student(student_id)

    if removed:
        print("\nStudent removed successfully.")
    else:
        print("\nStudent not found.")


def save_students(manager, filename, file_format):

    manager.save_to_file(filename, file_format)

    print("\nStudents saved successfully.")
    print("File:", filename)
    print("Format:", file_format)


if __name__ == "__main__":
    main()