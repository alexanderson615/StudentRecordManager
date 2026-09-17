import sqlite3

connection = sqlite3.connect('student.db')
cursor = connection.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS student (
   id INTEGER PRIMARY KEY,
   name TEXT,
   grade TEXT,
   email TEXT
   ) 
""")

connection.commit()

def add_student():
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    email = input("Enter student email: ")

    cursor.execute(
        "INSERT INTO student (name, grade, email) VALUES (?, ?, ?)",
        (name, grade, email)
    )
    connection.commit()

    print("Student added successfully")



def view_students():
    cursor.execute("SELECT * FROM student")

    students = cursor.fetchall()

    for student in students:
        print(student)

view_students()