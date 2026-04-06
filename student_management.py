class student:
    def __init__(self,s_id,s_name,s_course):
        self.s_id=s_id
        self.s_name=s_name
        self.s_course=s_course

def input_data():
    std_name=input("Enter student name: ")
    std_id = 1
    std_course = "Math"
    adding_value1 = student(s_id=std_id,s_name=std_name,s_course=std_course)
    return adding_value1

# new_data_student = input_data()
new_students = input_data()
print(f"{new_students.s_id}")


if new_students.s_id != new_students.s_id:
    print(" not student")

else:
    print(f"{new_students.s_name}")
