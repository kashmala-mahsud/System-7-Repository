#   Q1 Create variables to store your name, age, CGPA, and student status.

name = "Kashmala Mahsud"
age = 23
CGPA = 3.96
Is_a_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {CGPA}")
print(f"Is a student: {type(Is_a_student).__name__}")

# Q2. Arithmetic Operators

maths = int(input("Enter your marks in Maths: "))
physics = int(input("Enter your marks in Physics: "))
Total_marks = maths + physics
print(f"Total marks: {Total_marks}")