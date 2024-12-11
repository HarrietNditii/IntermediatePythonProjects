import sqlite3
from tabulate import tabulate

conn = sqlite3.connect("student_management.db")
cursor = conn.cursor()

#create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
               
""")

#commit changes and close connection
conn.commit()
conn.close()

def add_student(name, age, grade):
    conn = sqlite3.connect("student_management.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students(name, age, grade) VALUES(?,?,?)", (name, age, grade))
    conn.commit()
    conn.close()
    print(f"Student '{name}' added succesfully!")

def view_students():
    conn = sqlite3.connect("student_management.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Age", "Grade"], tablefmt="grid"))
    else:
        print("No students found.")

def update_student(student_id, name=None, age=None, grade=None):
    conn = sqlite3.connect("student_management.db")
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE students SET name = ? WHERE id = ?", (name, student_id))
    if age:
        cursor.execute("UPDATE STUDENTS SET age = ? WHERE id = ?", (age, students_id))
    if grade:
        cursor.execute("UPDATE STUDENTS SET grade = ? WHERE id = ?",(grade, students_id))
    conn.commit()
    conn.close()
    print(f"Student with ID {student_id} updated successfully!")

def delete_student(student_id):
    conn = sqlite3.connect("student_management.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print(f"Student with ID {student_id} deleted successfully!")

def main():
    while True:
        print("\n---Student Management System ---")
        print("1. Add Student.")
        print("2. View Student.")
        print("3. Update Student.") 
        print("4. Delete Student.")
        print("5. Exit.")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = input("Enter student's grade: ")
            add_student(name, age, grade) 
        elif choice == '2':
            view_students()
        elif choice == '3':
            student_id = int(input("Enter student's ID to update: "))
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age(leave blank to skip): ")
            grade = input("Enter new grade(leave blank to skip): ")
            update_student(
                student_id,
                name if name else None,
                int(age) if age else None,
                grade if grade else None
            )

        elif choice == '4':
            student_id = int(input("Enter student's ID to delete: "))
            delete_student(student_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
                          
                                                                            
