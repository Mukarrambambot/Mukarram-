class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

def create_student():
    name = input("Enter student name: ")
    roll_number = input("Enter student roll number: ")
    cgpa = float(input("Enter student CGPA: "))
    return Student(name, roll_number, cgpa)

# Input the list of students
num_students = int(input("Enter the number of students: "))
students = []

for _ in range(num_students):
    student = create_student()
    students.append(student)

sorted_students = sort_students(students)

print("Sorted Students:")
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
