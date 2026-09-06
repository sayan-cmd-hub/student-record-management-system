from student import Student
import file_handler


class StudentManager:
    """Manages multiple Student objects."""

    def __init__(self):
        self.students = []

    def add_student(self, student):
        """Add a Student object to the manager."""
        self.students.append(student)

    def remove_student(self, student_id):
        """Remove a student using Student ID."""
        for student in self.students:
            if student.student_id == int(student_id):
                self.students.remove(student)
                return True

        return False

    def search_student(self, student_id):
        """Search for a student using Student ID."""
        for student in self.students:
            if student.student_id == int(student_id):
                return student

        return None

    def search_by_name(self, name):
        """Search for students using their name."""
        results = []

        for student in self.students:
            if student.name.lower() == name.lower():
                results.append(student)

        return results

    def search_by_department(self, department):
        """Search for students using their department."""
        results = []

        for student in self.students:
            if student.department.lower() == department.lower():
                results.append(student)

        return results

    def search_by_average(self, minimum_average):
        """Find students whose average is above the given value."""
        results = []

        for student in self.students:
            if student.calculate_average() > float(minimum_average):
                results.append(student)

        return results

    def display_all_students(self):
        """Display information of all students."""
        for student in self.students:
            print(student.display_student())
            print("-" * 40)

    def save_to_file(self, filename, file_format):
        """Save all students to the selected file format."""

        if file_format == "txt":
            file_handler.write_txt(filename, self.students)

        elif file_format == "csv":
            file_handler.write_csv(filename, self.students)

        elif file_format == "json":
            file_handler.write_json(filename, self.students)

        else:
            print("Unsupported file format.")

    def load_from_file(self, filename, file_format):
        """Load students from the selected file format."""

        if file_format == "txt":
            self.students = file_handler.read_txt(filename)

        elif file_format == "csv":
            self.students = file_handler.read_csv(filename)

        elif file_format == "json":
            self.students = file_handler.read_json(filename)

        else:
            print("Unsupported file format.")
