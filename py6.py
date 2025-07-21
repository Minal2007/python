
students = {
    "Minal": 88,
    "Janhavi": 85,
    "Pranita": 93,
    "Pragati": 76
}

# 2. Add new students
# (You can use input() here if you want user interaction)
students["pratiksha"] = 91
students["ridhi"] = 79

# 3. Find the average grade
total = sum(students.values())
count = len(students)
average = total / count
print(f"Average Grade: {average:.2f}")

# 4. Identify the top performer
top_student = max(students, key=students.get)
top_grade = students[top_student]
print(f"Top Performer: {top_student} with a grade of {top_grade}")
