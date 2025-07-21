class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}  # Dictionary: {course_name: grade}

    def enroll(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = None
            print(f"{self.name} enrolled in {course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course_name}.")

    def update_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
            print(f"Grade updated for {self.name} in {course_name}: {grade}")
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    def calculate_gpa(self):
        valid_grades = [grade for grade in self.courses.values() if grade is not None]
        if valid_grades:
            gpa = sum(valid_grades) / len(valid_grades)
            return round(gpa, 2)
        else:
            return 0.0

    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Courses & Grades:")
        for course, grade in self.courses.items():
            grade_display = grade if grade is not None else "Not graded yet"
            print(f"  {course}: {grade_display}")
        print(f"GPA: {self.calculate_gpa()}\n")
