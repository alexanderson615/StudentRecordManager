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