# Q1. Student Marks Using a List

student_marks = [85, 92, 78, 96, 88]
total_marks = sum(student_marks)
average_marks = total_marks / len(student_marks)
highest_marks = max(student_marks)
lowest_marks = min(student_marks)
marks_in_descending_order = sorted(student_marks, reverse=True)

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")
print(f"Marks in Descending Order: {marks_in_descending_order}")

# Q2. Remove Duplicates

numbers = [10, 20, 10, 30, 40, 20, 50, 30]

# without using set
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(f"Original List: {numbers}")
print(f"List without Duplicates: {unique_numbers}")

# with using set
unique_numbers_set = list(set(numbers))
print(f"List without Duplicates (using set): {unique_numbers_set}")

# Q3. Tuple Operations
tuple1 = ("Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar")
print(f"Original Tuple: {tuple1}")
print(f"First Element: {tuple1[0]}")
print(f"Last Element: {tuple1[-1]}")
print(f"Length of Tuple: {len(tuple1)}")

# Q4. Student Record Using a Dictionary

student_record = {
    "name": "Ali",
    "age": 20,
    "marks": {
        "Math": 85,
        "Science": 92,
        "English": 78
    }
}
print(student_record)
print(f"Student Name: {student_record['name']}")

student_record["marks"]["History"] = 88
print(f"Updated Student Record: {student_record}")

student_record.update({"grade": 'A'})
print(f"Final Student Record: {student_record}")

print(f"Student Record Values: {list(student_record.values())}")
dict_keys = list(student_record.keys())
print(f"Student Record Keys: {dict_keys}")