


class Student:
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

student_list = []

def main_dashboard():
    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Show All Students")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter Name: ")
            roll = input("Enter Roll No: ")
            grd = input("Enter Grade: ")
            new_student = Student(name, roll, grd)
            student_list.append(new_student)
            print("Student added successfully!")

        elif choice == '2':
            search_roll = input("Enter Roll No to search: ")
            found = False
            for s in student_list:
                if s.roll_no == search_roll:
                    print(f"Found! Name: {s.name}, Grade: {s.grade}")
                    found = True
                    break
            if not found:
                print("Student not found.")

        elif choice == '3':

            print("\nList of all students:")
            for s in student_list:
                print(f"Roll: {s.roll_no} | Name: {s.name} | Grade: {s.grade}")

        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")

main_dashboard()
