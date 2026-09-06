class Student:
    """Represents one student and provides student-level operations."""

    PASS_MARK = 40

    def __init__(self, student_id, name, department, semester,
                 subject1, subject2, subject3):

        self.student_id = int(student_id)
        self.name = name
        self.department = department
        self.semester = int(semester)

        self.marks = {
            "subject1": float(subject1),
            "subject2": float(subject2),
            "subject3": float(subject3)
        }

    def calculate_total(self):
        """Calculate and return total marks."""
        return (
            self.marks["subject1"]
            + self.marks["subject2"]
            + self.marks["subject3"]
        )

    def calculate_average(self):
        """Calculate and return average marks."""
        return self.calculate_total() / 3

    def get_result(self):
        """Return PASS if all subjects have at least 40 marks."""
        if (
            self.marks["subject1"] >= self.PASS_MARK
            and self.marks["subject2"] >= self.PASS_MARK
            and self.marks["subject3"] >= self.PASS_MARK
        ):
            return "PASS"

        return "FAIL"

    def update_marks(self, subject1, subject2, subject3):
        """Update the marks of all three subjects."""
        self.marks["subject1"] = float(subject1)
        self.marks["subject2"] = float(subject2)
        self.marks["subject3"] = float(subject3)

    def display_student(self):
        """Return formatted student information."""
        return (
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Department: {self.department}\n"
            f"Semester: {self.semester}\n"
            f"Marks: {self.marks['subject1']:.0f}, "
            f"{self.marks['subject2']:.0f}, "
            f"{self.marks['subject3']:.0f}\n"
            f"Total: {self.calculate_total():.0f}\n"
            f"Average: {self.calculate_average():.2f}\n"
            f"Result: {self.get_result()}"
        )

    def to_list(self):
        """Convert student data into a list for TXT/CSV files."""
        return [
            self.student_id,
            self.name,
            self.department,
            self.semester,
            self.marks["subject1"],
            self.marks["subject2"],
            self.marks["subject3"]
        ]

    def to_dict(self):
        """Convert student data into a dictionary for JSON files."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "department": self.department,
            "semester": self.semester,
            "marks": {
                "subject1": self.marks["subject1"],
                "subject2": self.marks["subject2"],
                "subject3": self.marks["subject3"]
            }
        }
