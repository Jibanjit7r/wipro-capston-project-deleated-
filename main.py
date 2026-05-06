
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
''')

conn.commit()

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                   (name, age, course))
    conn.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    print("\nStudent Records")
    print("-" * 40)

    for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Course: {student[3]}")
        print("-" * 40)

def search_student():
    student_id = input("Enter student ID: ")

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Course: {student[3]}")
    else:
        print("Student not found.")

def delete_student():
    student_id = input("Enter student ID to delete: ")

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    print("Student deleted successfully!")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")

conn.close()
