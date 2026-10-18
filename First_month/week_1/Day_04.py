# Q1. File Handling
import os
f = open("test.txt", "w")
f.write("Hello, kashmala!")
f.close()

f = open("test.txt", "r")
content = f.read()
print(f"File Content: {content}")
f.close()

os.remove("test.txt")

# Q2. Exception Handling

No1 = int(input("Enter a number: "))
No2 = int(input("Enter another number: "))

try:
    result = No1 / No2
    print(f"Result: {result}")

except ZeroDivisionError:

    print("Error: Division by zero is not allowed.")

# Q3. Python Modules

f = open('D:\\System-7-Repository\\First_month\\week_1\\calculator.py', 'r') 
content = f.read()
print(f"Calculator Content: {content}")
f.close()

# Q4. Student Class

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

student1 = Student("Ali", 20, 85)
student2 = Student("Sara", 21, 92)
student3 = Student("Ahmed", 19, 78)

student1.display_info()
student2.display_info()
student3.display_info()