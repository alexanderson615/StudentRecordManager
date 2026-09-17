import sqlite3

def setup_database():
    connection = sqlite3.connect('student.db')
    cursor = connection.cursor()

    cursor.execute("""
       CREATE TABLE IF NOT EXISTS students (
       id INTEGER PRIMARY KEY,
       name TEXT,
       grade TEXT,
       email TEXT
       ) 
    """)

    connection.commit()

    return connection, cursor

connection, cursor = setup_database()

def validate_email(email):
    return '@' in email

def add_student():
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    email = input("Enter student email: ")

    if not name or not grade or not email:
        print("Please enter all fields")
        return

    if not validate_email(email):
        print("Invalid email, must contain '@'.")
        return
    try:
        cursor.execute(
            "INSERT INTO students (name, grade, email) VALUES (?, ?, ?)",
            (name, grade, email)
        )
        connection.commit()

        print("Student added successfully")

    except sqlite3.Error as e:
        print("Database error:", e)

def view_students():
    try:
        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        if not students:
            print("No students found")
            return

        for student in students:
            print("ID:", student[0])
            print("Name:", student[1])
            print("Grade:", student[2])
            print("Email:", student[3])
            print("-----------------------------")

    except sqlite3.Error as e:
        print("Database error:", e)

def update_student():
    try:
        student_id = int(input("Enter the ID of student you want to update: "))

    except ValueError:
        print("Please enter a valid integer ID.")
        return

    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    email = input("Enter student email: ")

    if not name or not grade or not email:
        print("All fields are required.")
        return

    if "@" not in email:
        print("Invalid email, must contain '@'.")
        return

    try:
        cursor.execute(
            "UPDATE students SET name = ?, grade = ?, email = ? WHERE id = ?",
            (name, grade, email, student_id)
        )

        connection.commit()

        if cursor.rowcount == 0:
            print("Student not found.")
        else:
            print("Student updated successfully.")

    except sqlite3.Error as e:
        print("Database error:", e)

def delete_student():
    try:
        student_id = int(input("Enter the ID of the student you want to delete: "))
    except ValueError:
        print("Please enter a valid integer ID.")
        return

    confirmation = input("Are you sure you want to delete this student? (y/n): ")

    if confirmation.lower() != "y":
        print("Deletion cancelled.")
        return

    try:
        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        connection.commit()

        if cursor.rowcount == 0:
            print("Student not found.")
        else:
            print("Student deleted successfully.")

    except sqlite3.Error as e:
        print("Database error:", e)

def main():
    while True:
        print("Student Record Manager")
        print("Enter 1 to add a new student")
        print("Enter 2 to view students")
        print("Enter 3 to update a student")
        print("Enter 4 to delete a student")
        print("Enter 5 to exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Goodbye!")
            connection.close()
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
