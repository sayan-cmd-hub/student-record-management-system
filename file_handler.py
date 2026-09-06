import csv
import json

from student import Student


# ============================================================
# TEXT FILE HANDLING
# ============================================================

def read_txt(filename):
    """Read student records from a TXT file."""
    students = []

    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        if line:
            values = line.split(",")

            student = Student(
                values[0].strip(),
                values[1].strip(),
                values[2].strip(),
                values[3].strip(),
                values[4].strip(),
                values[5].strip(),
                values[6].strip()
            )

            students.append(student)

    return students


def write_txt(filename, students):
    """Write all student records to a TXT file."""
    with open(filename, "w") as file:
        for student in students:
            values = student.to_list()

            line = (
                f"{values[0]}, {values[1]}, {values[2]}, "
                f"{values[3]}, {values[4]:.0f}, "
                f"{values[5]:.0f}, {values[6]:.0f}\n"
            )

            file.write(line)


def append_txt(filename, student):
    """Append one student record to a TXT file."""
    with open(filename, "a") as file:
        values = student.to_list()

        line = (
            f"{values[0]}, {values[1]}, {values[2]}, "
            f"{values[3]}, {values[4]:.0f}, "
            f"{values[5]:.0f}, {values[6]:.0f}\n"
        )

        file.write(line)


# ============================================================
# CSV FILE HANDLING
# ============================================================

def read_csv(filename):
    """Read student records from a CSV file."""
    students = []

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)

        # Skip the CSV header row
        header = next(reader)

        for row in reader:
            if row:
                student = Student(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6]
                )

                students.append(student)

    return students


def write_csv(filename, students):
    """Write student records to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Student_ID",
            "Name",
            "Department",
            "Semester",
            "Subject1",
            "Subject2",
            "Subject3"
        ])

        for student in students:
            writer.writerow(student.to_list())


# ============================================================
# JSON FILE HANDLING
# ============================================================

def read_json(filename):
    """Read student records from a JSON file."""
    students = []

    with open(filename, "r") as file:
        data = json.load(file)

    for record in data:
        student = Student(
            record["student_id"],
            record["name"],
            record["department"],
            record["semester"],
            record["marks"]["subject1"],
            record["marks"]["subject2"],
            record["marks"]["subject3"]
        )

        students.append(student)

    return students


def write_json(filename, students):
    """Write student records to a JSON file."""
    data = []

    for student in students:
        data.append(student.to_dict())

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
