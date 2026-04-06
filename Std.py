class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    @staticmethod
    def create_student():
        id = int(input("Enter student id: "))
        name = input("Enter the name of student: ")   # FIXED
        age = int(input("Enter the age of student: "))

        stdobj = Student(id, name, age)
        return stdobj

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}")


# List to store students
students = []

# Add student
std_info = Student.create_student()
students.append(std_info)

# Display all students
print("\nAll Students:")
for std in students:
    std.display()

# Search by ID
search_id = int(input("\nEnter ID to search: "))

found = False
for std in students:
    if std.id == search_id:
        print("\nStudent Found:")
        std.display()
        found = True
        break

if not found:
    print("Student not found.")