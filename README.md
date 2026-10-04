# Student Record Management and Search System

A Python-based Student Record Management and Search System developed using Object-Oriented Programming (OOP), basic searching techniques, command-line arguments, and file handling for TXT, CSV, and JSON files.

## A. Objective

The objective of this assignment is to develop a Student Record Management and Search System using Python.

The project focuses on understanding and implementing practical Python programming concepts such as:

- Object-Oriented Programming (OOP)
- Classes and objects
- Constructors and attributes
- Instance methods
- Student record management
- Basic searching using loops and conditions
- Condition-based filtering
- Text file handling
- CSV file handling
- JSON file handling
- Command-line arguments using argparse
- Reading and writing student records
- Modular programming using multiple Python files

The system represents an individual student using the `Student` class and manages multiple student objects using the `StudentManager` class.

## B. Features

The program provides the following features:

- Add a new student
- Display student information
- Display all students
- Calculate total marks
- Calculate average marks
- Determine pass/fail status
- Update student marks
- Remove a student
- Search for a student using Student ID
- Search students using Name
- Search students using Department
- Search students based on average marks
- Read student records from TXT files
- Write student records to TXT files
- Read student records from CSV files
- Write student records to CSV files
- Read student records from JSON files
- Write student records to JSON files
- Use command-line arguments to specify file path and file format
- Test the program using at least five student records

## C. Project Structure

````text
student-record-system/
│
├── data/
│   ├── students.txt
│   ├── students.csv
│   └── students.json
│
├── screenshots/
│   ├── 01_csv_execution.png
│   ├── 02_txt_execution.png
│   ├── 03_json_execution.png
│   ├── 04_search.png
│   └── 05_update_and_save.png
│
├── main.py
├── student.py
├── manager.py
├── file_handler.py
├── README.md
└── .gitignore

File Description

main.py
main.py is the main entry point of the application.

It is responsible for:

Processing command-line arguments using argparse
Accepting the input file path
Accepting the file format
Creating the StudentManager object
Loading student records
Providing the interactive menu
Accepting user input
Calling the required student management and searching methods
Saving updated student records

student.py
student.py contains the Student class.

The Student class represents one student and stores:

Student ID
Name
Department
Semester
Marks in three subjects

The class provides methods for:

Calculating total marks
Calculating average marks
Determining pass/fail status
Displaying student information
Updating student marks

manager.py
manager.py contains the StudentManager class.

The StudentManager class is responsible for managing multiple Student objects.

It provides methods for:

Adding students
Removing students
Searching by Student ID
Searching by Name
Searching by Department
Searching by average marks
Displaying all students
Loading student records from files
Saving student records to files

file_handler.py
file_handler.py is responsible for file handling operations.

It provides functionality for:

Reading TXT files
Writing TXT files
Appending to TXT files
Reading CSV files
Writing CSV files
Reading JSON files
Writing JSON files

The Python standard library modules csv and json are used for CSV and JSON processing.
````
## D. Requirements
Software Requirements

The following software is required to run the project:

Python 3.x
PyCharm or any Python-compatible IDE
Command-line/Terminal access
Python Modules Used

The project uses Python's standard library modules:

argparse
csv
json

No external Python packages are required.

Pandas and NumPy are not used in this project.

## E. How to Run

The program is executed from the command line.

The program accepts two main command-line arguments:

--file - specifies the path of the student data file
--format - specifies the file format

The supported formats are:

txt
csv
json

Run Using TXT File

python main.py --file data/students.txt --format txt

Run Using CSV File

python main.py --file data/students.csv --format csv

Run Using JSON File

python main.py --file data/students.json --format json

After successfully loading the selected file, the program displays the main menu.

Main Menu
==================================================
       STUDENT RECORD MANAGEMENT SYSTEM
==================================================
1. Display all students
2. Add a new student
3. Search student by ID
4. Search students by Name
5. Search students by Department
6. Search students by Average
7. Update student marks
8. Remove student
9. Save students to file
10. Exit

Enter your choice:

## F. Input and Output
Input

The program accepts the following inputs:

Student ID

Student Name

Department

Semester

Marks in three subjects

Student ID for searching

Name for searching

Department for searching

Minimum average marks for condition-based searching

File path through command-line arguments

File format through command-line arguments

The program can also read previously saved student information from TXT, CSV, and JSON files.

Sample Data

The data folder contains sample student records.

The project is tested using at least five student records.

Example student records:

101, Rahul, Computer Science, 1, 78, 82, 69

102, Priya, Computer Science, 1, 91, 87, 94

103, Amit, Mathematics, 1, 65, 71, 68

104, Sneha, Electronics, 2, 88, 76, 81

105, Arjun, Information Technology, 2, 55, 62, 59

### Output

The program can produce the following outputs:

Student information

Total marks

Average marks

Pass/fail status

Search results

Student addition confirmation

Student removal confirmation

Marks update confirmation

File saving confirmation

### Example Student Output

ID: 101

Name: Rahul

Department: Computer Science

Semester: 1

Marks: 78, 82, 69

Total: 229

Average: 76.33

Result: PASS

Example Search Output

For example, when searching for Student ID 101:

--- Search by Student ID ---

Enter Student ID: 101

Student found:

ID: 101

Name: Rahul

Department: Computer Science

Semester: 1

Marks: 78, 82, 69

Total: 229

Average: 76.33

Result: PASS

Output Files

When updated records are saved, the program writes the records to the selected file.

Examples:

data/students.txt

data/students.csv

data/students.json

## G. OOP Concepts Used

Object-Oriented Programming is an important part of this project.

1. Classes

Two main classes are implemented:

Student

StudentManager
2. Objects

Each student record is represented as an object of the Student class.

For example:

student = Student(
    101,
    "Rahul",
    "Computer Science",
    1,
    78,
    82,
    69
)

A StudentManager object is used to manage multiple Student objects.

3. Constructors

The Student class uses a constructor to initialize the information of a student.

The constructor initializes attributes such as:

Student ID\
Name\
Department\
Semester\
Subject marks
4. Attributes

The Student object contains attributes such as:

student_id\
name\
department\
semester\
marks
5. Instance Methods

The Student class contains methods such as:

calculate_total()\
calculate_average()\
get_result()\
display_student()\
update_marks()

The StudentManager class contains methods such as:

add_student()\
remove_student()\
search_student()\
search_by_name()\
search_by_department()\
search_by_average()\
display_all_students()\
load_from_file()\
save_to_file()
6. Separation of Responsibilities

The project separates different responsibilities into different modules.

Student represents one student.\
StudentManager manages multiple students.\
file_handler.py handles file operations.\
main.py handles command-line arguments and user interaction.

## H. File Handling Concepts Used

The project demonstrates file handling using three different file formats:

TXT\
CSV\
JSON
1. TXT File Handling

The program reads and writes student records using normal text files.

Python file handling concepts used include:

open()\
read()\
readline()\
readlines()\
write()\
with open(...)

Different file modes such as:

r\
w\
a

are used where appropriate.

The TXT file stores student records in a simple comma-separated format.

Example:

101, Rahul, Computer Science, 1, 78, 82, 69

The program converts the records read from the TXT file into Student objects.

2. CSV File Handling

The CSV part uses Python's built-in csv module.

The following are used:

csv.reader\
csv.writer

The CSV file contains a header:

Student_ID,Name,Department,Semester,Subject1,Subject2,Subject3

Example:

101,Rahul,Computer Science,1,78,82,69\
102,Priya,Computer Science,1,91,87,94

The program:

Reads the CSV file\
Handles the header row\
Reads individual rows\
Converts each row into a Student object\
Displays student information\
Allows new students to be added\
Searches student records\
Saves updated records

No external library is used for CSV processing.

3. JSON File Handling

The project uses Python's built-in json module.

The following functions are used:

json.load()\
json.dump()

Student information is stored using dictionaries and lists.

Example JSON structure:

{\
    "student_id": 101,\
    "name": "Rahul",\
    "department": "Computer Science",\
    "semester": 1,\
    "marks": {\
        "subject1": 78,\
        "subject2": 82,\
        "subject3": 69\
    }\
}

The program:

Reads student information from JSON\
Converts JSON records into Student objects\
Displays student information\
Searches for students\
Modifies student marks\
Saves updated information to a JSON file

## I. Searching Concepts Used

The project implements student searching using basic Python programming logic.

The searching operations are performed using:

for loops\
if conditions\
Comparisons\
Lists\
Basic Python logic

No Pandas, NumPy, or external search libraries are used.

1. Search by Student ID

The program checks each Student object and compares its Student ID with the ID entered by the user.

Conceptually:

for student in students:\
    if student.student_id == student_id:\
        ...
2. Search by Name

The program loops through the student records and compares the entered name with the name stored in each Student object.

3. Search by Department

The program checks each student's department and returns the students whose department matches the entered department.

4. Condition-Based Search

The program supports searching for students whose average marks are greater than a specified value.

For example:

Enter minimum average marks: 80

The program checks each student's average marks and returns the students satisfying the condition.

Conceptually:

for student in students:\
    if student.calculate_average() > minimum_average:\
        ...

The search operations are implemented using basic loops, conditions, and comparisons.

## J. Learning Outcome / Conclusion

This assignment provided practical experience in Python programming, Object-Oriented Programming, file handling, searching, and modular program development.

Through this project, the following concepts were learned:

Creating classes and objects\
Using constructors and attributes\
Implementing instance methods\
Managing multiple objects using a manager class\
Reading and writing text files\
Working with CSV files\
Working with JSON files\
Converting file data into Python objects\
Updating student information\
Searching records using loops and conditions\
Implementing condition-based searching\
Using command-line arguments with argparse\
Dividing a Python program into multiple modules\
Testing a program using multiple input records

One of the main challenges was maintaining a consistent student data structure while working with different file formats. Separating the program into student.py, manager.py, file_handler.py, and main.py helped make the program more organized and easier to understand.

Overall, this assignment improved practical understanding of Python Object-Oriented Programming, file handling, basic searching, modular programming, and command-line execution.