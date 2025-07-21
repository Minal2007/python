class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}        # Format: {course_name: grade}
        self.credits = {}        # Format: {course_name: credit_hours}

    def enroll(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = None
            print(f"{self.name} enrolled in {course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course_name}.")

    def update_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
            print(f"Updated grade for {course_name}: {grade}")
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    def add_credits(self, course_name, credits):
        if course_name in self.courses:
            self.credits[course_name] = credits
            print(f"Credits added for {course_name}: {credits}")
        else:
            print(f"{self.name} must enroll in {course_name} first.")

    def calculate_gpa(self):
        valid_grades = [grade for grade in self.courses.values() if grade is not None]
        if valid_grades:
            return round(sum(valid_grades) / len(valid_grades), 2)
        return 0.0

    def calculate_weighted_gpa(self):
        total_weighted = 0
        total_credits = 0
        for course, grade in self.courses.items():
            if grade is not None and course in self.credits:
                total_weighted += grade * self.credits[course]
                total_credits += self.credits[course]

        if total_credits > 0:
            return round(total_weighted / total_credits, 2)
        return 0.0

    def get_highest_grade(self):
        graded_courses = {course: grade for course, grade in self.courses.items() if grade is not None}
        if graded_courses:
            highest_course = max(graded_courses, key=graded_courses.get)
            return highest_course, graded_courses[highest_course]
        return None, None

    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Courses & Grades:")
        for course in self.courses:
            grade = self.courses[course] if self.courses[course] is not None else "Not graded yet"
            credit = self.credits.get(course, "No credits assigned")
            print(f"  {course}: Grade={grade}, Credits={credit}")
        print(f"Simple GPA: {self.calculate_gpa()}")
        print(f"Weighted GPA: {self.calculate_weighted_gpa()}\n")

    def __str__(self):
        return f"Student({self.name}, ID: {self.student_id}, GPA: {self.calculate_gpa()})"
