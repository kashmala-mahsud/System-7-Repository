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
chemistry = int(input("Enter your marks in Chemistry: "))
Total_marks = maths + physics + chemistry
print(f"Total marks: {Total_marks}")


# Q2. Grade Calculator

marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    grade = "A+"   
elif marks >= 80 and marks < 90:
    grade = "A"
elif marks >= 70 and marks < 80:
    grade = "B"
elif marks >= 60 and marks < 70:
    grade = "C"
elif marks < 50 and marks >= 0:
    grade = "F"
else:
    grade = "Invalid marks"

print(f"Grade: {grade}")

# Q3. Multiplication Table
number = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
