from university import University

class Examination:
    def __init__(self, course, exam_type, date, time):
        self.course = course
        self.exam_type = exam_type  # e.g., "Quiz", "Midterm", "Final Exam"
        self.date = date
        self.time = time

    def __str__(self):
        return (f"Examination: {self.exam_type}, Course: {self.course.course_name} "
                f"({self.course.course_code}), Date: {self.date}, Time: {self.time}")

    @classmethod
    def schedule_exam(cls):
        course_code = input("Enter course code: ")
        exam_type = input("Enter exam type (Quiz, Midterm, Final Exam): ")
        date = input("Enter exam date (e.g., 2024-12-01): ")
        time = input("Enter exam time (e.g., 10:00-12:00): ")

        # Find the course
        course = next((c for c in University.courses if c.course_code == course_code), None)

        if course:
            exam = cls(course, exam_type, date, time)
            University.examinations.append(exam)
            print(f"{exam_type} for {course.course_name} scheduled successfully!")
        else:
            print("Course not found. Examination not scheduled.")

    @classmethod
    def view_exams_by_student(cls):
        student_id = input("Enter student ID: ")
        student = next((s for s in University.students if s.student_id == student_id), None)

        if not student:
            print("Student not found.")
            return

        print(f"Examinations for {student.name} (ID: {student_id}):")
        exams = [exam for exam in University.examinations if student in exam.course.students]

        if not exams:
            print("No examinations found for this student.")
            return

        for exam in exams:
            print(exam)

    @classmethod
    def view_exams_by_course(cls):
        course_code = input("Enter course code: ")
        course = next((c for c in University.courses if c.course_code == course_code), None)

        if not course:
            print("Course not found.")
            return

        print(f"Examinations for {course.course_name} (Code: {course_code}):")
        exams = [exam for exam in University.examinations if exam.course == course]

        if not exams:
            print("No examinations found for this course.")
            return

        for exam in exams:
            print(exam)
