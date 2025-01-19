from university import University
import json


class Examination:
    def __init__(self, course, exam_type, date, time):
        self.course = course
        self.exam_type = exam_type  # e.g., "Quiz", "Midterm", "Final Exam"
        self.date = date
        self.time = time
        self.questions = []  # Initialize an empty list for questions
        self.scores = {}  # Dictionary to store student scores {student_id: score}

    def __str__(self):
        return (f"Examination: {self.exam_type}, Course: {self.course.course_name} "
                f"({self.course.course_code}), Date: {self.date}, Time: {self.time}")
    
    def add_question(self, question, choices, answer):
        """Add a new question to the exam."""
        self.questions.append({"question": question, "choices": choices, "answer": answer})
        print("Question added successfully!\n")

    def save_score(self, student_id, score):
        """Save the score for a student."""
        self.scores[student_id] = score
        print(f"Score for Student {student_id} saved successfully!\n")

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

    @classmethod
    def add_questions_to_exam(cls):
        course_code = input("Enter course code: ")
        exam_type = input("Enter exam type (Quiz, Midterm, Final Exam): ")

        # Find the exam
        exam = next(
            (e for e in University.examinations if e.course.course_code == course_code and e.exam_type == exam_type), 
            None
        )

        if not exam:
            print("Examination not found.")
            return

        print(f"Adding questions to {exam_type} for {exam.course.course_name}:\n")
        while True:
            question = input("Enter the question: ")
            choices = [input(f"Choice {ch}: ") for ch in ['A', 'B', 'C', 'D']]
            answer = input("Enter the correct answer (A/B/C/D): ").upper()

            exam.add_question(question, choices, answer)

            another = input("Do you want to add another question? (yes/no): ").lower()
            if another != 'yes':
                break

    @classmethod
    def take_exam(cls):
        student_id = input("Enter your student ID: ")
        student = next((s for s in University.students if s.student_id == student_id), None)

        if not student:
            print("Student not found.")
            return

        course_code = input("Enter course code: ")
        exam_type = input("Enter exam type (Quiz, Midterm, Final Exam): ")

        # Find the exam
        exam = next(
            (e for e in University.examinations if e.course.course_code == course_code and e.exam_type == exam_type), 
            None
        )

        if not exam:
            print("Examination not found.")
            return

        if not exam.questions:
            print(f"No questions are available for {exam_type} in {exam.course.course_name}.")
            return

        print(f"Starting {exam_type} for {exam.course.course_name}...\n")
        score = 0
        for i, question in enumerate(exam.questions, start=1):
            print(f"Question {i}: {question['question']}")
            for idx, choice in enumerate(question['choices'], start=1):
                print(f"{chr(64 + idx)}. {choice}")

            answer = input("Enter your answer (A/B/C/D): ").upper()
            if answer == question['answer']:
                score += 1

        total_questions = len(exam.questions)
        percentage = (score / total_questions) * 100
        print(f"\nExam Completed! You scored {score}/{total_questions} ({percentage:.2f}%)\n")

        exam.save_score(student_id, percentage)

    @classmethod
    def view_scores(cls):
        course_code = input("Enter course code: ")
        exam_type = input("Enter exam type (Quiz, Midterm, Final Exam): ")

        # Find the exam
        exam = next(
            (e for e in University.examinations if e.course.course_code == course_code and e.exam_type == exam_type), 
            None
        )

        if not exam:
            print("Examination not found.")
            return

        if not exam.scores:
            print(f"No scores available for {exam_type} in {exam.course.course_name}.")
            return

        print(f"Scores for {exam_type} in {exam.course.course_name}:\n")
        for student_id, score in exam.scores.items():
            student = next((s for s in University.students if s.student_id == student_id), None)
            student_name = student.name if student else "Unknown Student"
            print(f"{student_name} (ID: {student_id}): {score:.2f}%")
        print()

    @classmethod
    def view_scores_by_student(cls):
        student_id = input("Enter student ID: ")
        student = next((s for s in University.students if s.student_id == student_id), None)

        if not student:
            print("Student not found.")
            return

        print(f"Scores for {student.name} (ID: {student_id}):\n")
        has_scores = False

        for exam in University.examinations:
            if student_id in exam.scores:
                has_scores = True
                print(f"{exam.exam_type} - {exam.course.course_name} ({exam.course.course_code}): "
                    f"{exam.scores[student_id]:.2f}%")

        if not has_scores:
            print(f"No scores available for {student.name}.")
        print()


    @classmethod
    def view_all_scores(cls):
        if not University.examinations:
            print("No examinations scheduled.")
            return

        print("Scores for All Examinations:\n")
        for exam in University.examinations:
            print(f"{exam.exam_type} - {exam.course.course_name} ({exam.course.course_code}):")
            if not exam.scores:
                print("  No scores available.")
            else:
                for student_id, score in exam.scores.items():
                    student = next((s for s in University.students if s.student_id == student_id), None)
                    student_name = student.name if student else "Unknown Student"
                    print(f"  {student_name} (ID: {student_id}): {score:.2f}%")
            print()


    @classmethod
    def bulk_add_questions(cls):
        course_code = input("Enter course code: ")
        exam_type = input("Enter exam type (Quiz, Midterm, Final Exam): ")

        # Find the exam
        exam = next(
            (e for e in University.examinations if e.course.course_code == course_code and e.exam_type == exam_type), 
            None
        )

        if not exam:
            print("Examination not found.")
            return

        print(f"Bulk adding questions to {exam_type} for {exam.course.course_name}:\n")

        # Prompt for JSON file path
        file_path = input("Enter the path to the JSON file with questions: ")

        # Load questions from the specified JSON file
        try:
            with open(file_path, "r") as file:
                questions = json.load(file)
        except FileNotFoundError:
            print(f"File not found: {file_path}. Please ensure the file exists.")
            return
        except json.JSONDecodeError:
            print(f"Invalid JSON format in file: {file_path}. Please check the file.")
            return

        # Add each question to the exam
        for q in questions:
            exam.add_question(q["question"], q["choices"], q["answer"])

        print(f"{len(questions)} questions added successfully to {exam_type} for {exam.course.course_name}!\n")
