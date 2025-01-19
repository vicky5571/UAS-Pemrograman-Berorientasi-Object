class University:
    students = []
    professors = []
    courses = []
    departments = []
    buildings = []
    schedules = []
    examinations = []  # New list for storing examinations

    @classmethod
    def load_sample_data(cls):
        from student import Student
        from professor import Professor
        from course import Course
        from building import Building
        from room import Room
        from examination import Examination
        from department import Department

        # Add Sample Students
        cls.students.append(Student("Vicky", 19, "vicky@university.com", "001"))
        cls.students.append(Student("Galih", 21, "galih@university.com", "002"))
        cls.students.append(Student("Alice", 20, "alice@university.com", "003"))
        cls.students.append(Student("Bob", 22, "bob@university.com", "004"))

        # Add Sample Professors
        cls.professors.append(Professor("Joni Maulindar", 40, "joni@university.com", "P001"))
        cls.professors.append(Professor("Ridwan", 30, "ridwan@university.com", "P002"))
        cls.professors.append(Professor("Dr. Jane Smith", 35, "jane.smith@university.com", "P002"))
        cls.professors.append(Professor("Eko", 41, "eko@university.com", "P002"))

        # Add Sample Departments
        cls.departments.append(Department("Engineering", "Dr. Einstein"))
        cls.departments.append(Department("Fikom", "Dr. Tesla"))

        # Add Sample Buildings
        building1 = Building("Main Campus", "Jl. Nusukan")
        building2 = Building("Fikom", "Jl. Bhayangkara")
        cls.buildings.extend([building1, building2])

        # Add Sample Rooms
        building1.rooms.append(Room("101", 50))
        building1.rooms.append(Room("102", 30))
        building2.rooms.append(Room("201", 40))
        building2.rooms.append(Room("202", 30))

        # Add Sample Courses
        course1 = Course("Rekayasa Perangkat Lunak", "rpl24", cls.departments[0])
        course2 = Course("Pemrograman Basis Data", "pb24", cls.departments[0])
        course3 = Course("Statistika", "st24", cls.departments[0])
        course4 = Course("Matematika Diskrit", "md24", cls.departments[0])
        cls.courses.extend([course1, course2, course3, course4])

        # Enroll Students in Courses
        course1.students.append(cls.students[0])
        course1.students.append(cls.students[1])
        course2.students.append(cls.students[0])
        course2.students.append(cls.students[1])
        course3.students.append(cls.students[2])
        course3.students.append(cls.students[3])
        course4.students.append(cls.students[2])
        course4.students.append(cls.students[3])

        # Add Sample Schedules
        cls.schedules.append({
            "course": course1,
            "professor": cls.professors[0],
            "room": building2.rooms[0],
            "time": "Mon 10:00-12:00",
            "students": course1.students,
        })

        cls.schedules.append({
            "course": course2,
            "professor": cls.professors[1],
            "room": building2.rooms[0],
            "time": "Wed 14:00-16:00",
            "students": course2.students,
        })

        cls.schedules.append({
            "course": course3,
            "professor": cls.professors[2],
            "room": building1.rooms[1],
            "time": "Tue 14:00-16:00",
            "students": course3.students,
        })

        cls.schedules.append({
            "course": course4,
            "professor": cls.professors[3],
            "room": building1.rooms[0],
            "time": "Mon 14:00-16:00",
            "students": course4.students,
        })

        # Add Sample Examinations
        cls.examinations.append(Examination(course1, "Quiz", "2025-01-10", "09:00-10:00"))
        cls.examinations.append(Examination(course1, "Midterm", "2025-02-01", "10:00-12:00"))
        # cls.examinations.append(Examination(course1, "Final Exam", "2025-01-25", "10:00-12:00"))

        cls.examinations.append(Examination(course2, "Quiz", "2025-02-10", "09:00-10:00"))
        cls.examinations.append(Examination(course2, "Midterm", "2025-02-15", "14:00-16:00"))
        cls.examinations.append(Examination(course2, "Final Exam", "2025-03-20", "08:00-10:00"))

        cls.examinations.append(Examination(course3, "Quiz", "2025-03-10", "09:00-10:00"))
        cls.examinations.append(Examination(course3, "Midterm", "2025-03-15", "14:00-16:00"))
        cls.examinations.append(Examination(course3, "Final Exam", "2025-04-20", "08:00-10:00"))

        cls.examinations.append(Examination(course4, "Quiz", "2025-04-10", "09:00-10:00"))
        cls.examinations.append(Examination(course4, "Midterm", "2025-04-15", "14:00-16:00"))
        cls.examinations.append(Examination(course4, "Final Exam", "2025-05-20", "08:00-10:00"))

        # Add Questions
        course_questions = {
        "rpl24": {
            "Quiz": [
                {"question": "What is OOP?", "choices": ["Object-Oriented Programming", "Office-Oriented Programming", "Output-Oriented Programming", "None"], "answer": "A"},
                {"question": "What is Python?", "choices": ["Language", "Snake", "Game", "IDE"], "answer": "A"},
                {"question": "What does IDE stand for?", "choices": ["Integrated Development Environment", "Internet Development Environment", "Internal Data Editor", "None"], "answer": "A"},
                {"question": "What is Git?", "choices": ["Version Control System", "Game", "IDE", "Programming Language"], "answer": "A"}
            ],
            "Midterm": [
                {"question": "What is Inheritance in OOP?", "choices": ["A feature", "Class reuse", "Method reuse", "All"], "answer": "D"},
                {"question": "Which is not a datatype?", "choices": ["Integer", "String", "HTML", "Float"], "answer": "C"},
                {"question": "What is Encapsulation?", "choices": ["Hiding details", "Inheritance", "None", "Polymorphism"], "answer": "A"},
                {"question": "What is PEP?", "choices": ["Python Enhancement Proposal", "Python Enrichment Proposal", "None", "Python Example Proposal"], "answer": "A"}
            ],
            "Final Exam": [
                # {"question": "What is Polymorphism?", "choices": ["Method Overriding", "Object reuse", "Both", "None"], "answer": "A"},
                # {"question": "What is Module in Python?", "choices": ["Library", "Game", "IDE", "Framework"], "answer": "A"},
                # {"question": "What is Framework?", "choices": ["Collection of Modules", "IDE", "Game", "None"], "answer": "A"},
                # {"question": "What is Django?", "choices": ["Web Framework", "IDE", "Programming Language", "None"], "answer": "A"}
            ]
        },
        "pb24": {
            "Quiz": [
                {"question": "What is SQL?", "choices": ["Structured Query Language", "Simple Query Language", "Sequential Query Language", "None"], "answer": "A"},
                {"question": "What is PRIMARY KEY?", "choices": ["Unique Identifier", "Foreign Key", "Duplicate Key", "None"], "answer": "A"},
                {"question": "What does CRUD stand for?", "choices": ["Create, Read, Update, Delete", "Copy, Read, Update, Delete", "Create, Run, Update, Delete", "None"], "answer": "A"},
                {"question": "What is JOIN?", "choices": ["Combines Tables", "Splits Tables", "Deletes Tables", "None"], "answer": "A"}
            ],
            "Midterm": [
                {"question": "What is Normalization?", "choices": ["Reduce Redundancy", "Remove Nulls", "Both", "None"], "answer": "A"},
                {"question": "What is a View?", "choices": ["Virtual Table", "Physical Table", "None", "Query"], "answer": "A"},
                {"question": "What is a Stored Procedure?", "choices": ["Predefined Query", "Backup", "None", "Command"], "answer": "A"},
                {"question": "What is a Trigger?", "choices": ["Event-based Procedure", "Query", "Backup", "Command"], "answer": "A"}
            ],
            "Final Exam": [
                {"question": "What is ACID?", "choices": ["Transaction Properties", "Framework", "Library", "None"], "answer": "A"},
                {"question": "What is Foreign Key?", "choices": ["Reference Key", "Primary Key", "Both", "None"], "answer": "A"},
                {"question": "What is Indexing?", "choices": ["Speeds Queries", "Deletes Data", "Adds Data", "None"], "answer": "A"},
                {"question": "What is NoSQL?", "choices": ["Non-relational DB", "SQL Variant", "None", "None of the above"], "answer": "A"}
            ]
        },
                "st24": {
            "Quiz": [
                {"question": "What is the mean of [1,2,3,4,5]?", "choices": ["3", "4", "2.5", "None"], "answer": "A"},
                {"question": "What is the mode of [1,1,2,3]?", "choices": ["1", "2", "3", "None"], "answer": "A"},
                {"question": "What is the median of [3,2,1,4,5]?", "choices": ["1", "3", "5", "None"], "answer": "B"},
                {"question": "What is a histogram?", "choices": ["Bar Graph", "Pie Chart", "Line Graph", "None"], "answer": "A"}
            ],
            "Midterm": [
                {"question": "What is probability?", "choices": ["Likelihood of event", "Certainty", "None", "Both"], "answer": "A"},
                {"question": "What is variance?", "choices": ["Data Spread", "Mean", "Median", "None"], "answer": "A"},
                {"question": "What is standard deviation?", "choices": ["Square root of variance", "Variance", "Mean", "None"], "answer": "A"},
                {"question": "What is regression?", "choices": ["Statistical Modeling", "Graphing", "None", "Both"], "answer": "A"}
            ],
            "Final Exam": [
                {"question": "What is hypothesis testing?", "choices": ["Test assumptions", "Nullify Hypothesis", "None", "Both"], "answer": "A"},
                {"question": "What is correlation?", "choices": ["Relationship Strength", "Variance", "Both", "None"], "answer": "A"},
                {"question": "What is sampling?", "choices": ["Subset Selection", "Full Data", "Both", "None"], "answer": "A"},
                {"question": "What is ANOVA?", "choices": ["Variance Analysis", "Probability", "Mean Testing", "None"], "answer": "A"}
            ]
        },
        "md24": {
            "Quiz": [
                {"question": "What is a set?", "choices": ["Collection of elements", "Null", "None", "Both"], "answer": "A"},
                {"question": "What is a graph?", "choices": ["Nodes and Edges", "Bar Graph", "Line Graph", "None"], "answer": "A"},
                {"question": "What is a tree?", "choices": ["Graph with hierarchy", "Graph", "Both", "None"], "answer": "A"},
                {"question": "What is a relation?", "choices": ["Mapping", "Null", "Graph", "None"], "answer": "A"}
            ],
            "Midterm": [
                {"question": "What is logic?", "choices": ["Reasoning", "Truth Table", "Both", "None"], "answer": "A"},
                {"question": "What is a proposition?", "choices": ["Statement", "Graph", "Tree", "None"], "answer": "A"},
                {"question": "What is induction?", "choices": ["Proof", "Graph", "Tree", "None"], "answer": "A"},
                {"question": "What is recursion?", "choices": ["Self-reference", "Loop", "Both", "None"], "answer": "A"}
            ],
            "Final Exam": [
                {"question": "What is an automaton?", "choices": ["Machine Model", "Graph", "Tree", "None"], "answer": "A"},
                {"question": "What is DFA?", "choices": ["Deterministic Finite Automaton", "Data Frame", "Graph", "None"], "answer": "A"},
                {"question": "What is Turing Machine?", "choices": ["Computational Model", "Graph", "Tree", "None"], "answer": "A"},
                {"question": "What is complexity?", "choices": ["Algorithm Efficiency", "Graph", "Tree", "None"], "answer": "A"}
            ]
        }
    }
            # Add Exams and Questions for Each Course
        exam_types = ["Quiz", "Midterm", "Final Exam"]
        exam_dates = {
            "Quiz": "2025-01-10",
            "Midterm": "2025-02-15",
            "Final Exam": "2025-03-20"
        }
        exam_times = {
            "Quiz": "09:00-10:00",
            "Midterm": "14:00-16:00",
            "Final Exam": "08:00-10:00"
        }

        courses = [
            Course("Rekayasa Perangkat Lunak", "rpl24", cls.departments[0]),
            Course("Pemrograman Basis Data", "pb24", cls.departments[0]),
            Course("Statistika", "st24", cls.departments[0]),
            Course("Matematika Diskrit", "md24", cls.departments[0])
        ]

        cls.courses.extend(courses)

        for course in cls.courses:
            questions_for_course = course_questions[course.course_code]
            for exam_type in exam_types:
                exam = Examination(course, exam_type, exam_dates[exam_type], exam_times[exam_type])
                for q in questions_for_course[exam_type]:
                    exam.add_question(q["question"], q["choices"], q["answer"])
                cls.examinations.append(exam)


        print("Sample data loaded successfully!\n")


    @classmethod
    def view_students(cls):
        if not cls.students:
            print("No students available.\n")
            return
        print("List of Students:")
        for student in cls.students:
            print(student)
        print()

    @classmethod
    def view_professors(cls):
        if not cls.professors:
            print("No professors available.\n")
            return
        print("List of Professors:")
        for professor in cls.professors:
            print(professor)
        print()

    @classmethod
    def view_departments(cls):
        if not cls.departments:
            print("No departments available.\n")
            return
        print("List of Departments:")
        for department in cls.departments:
            print(department)
        print()

    @classmethod
    def view_buildings(cls):
        if not cls.buildings:
            print("No buildings available.\n")
            return
        print("List of Buildings:")
        for building in cls.buildings:
            print(building)
            for room in building.rooms:
                print(f"  - Room: {room.room_number}, Capacity: {room.capacity}")
        print()

    # @classmethod
    # def view_courses(cls):
    #     if not cls.courses:
    #         print("No courses available.\n")
    #         return
    #     print("List of Courses:")
    #     for course in cls.courses:
    #         print(course)
    #         print("  Enrolled Students:")
    #         for student in course.students:
    #             print(f"    - {student.name} (ID: {student.student_id})")
    #     print()

    @classmethod
    def view_courses_schedules(cls):
        if not cls.schedules:
            print("No schedules available.\n")
            return
        print("List of Schedules:")
        for schedule in cls.schedules:
            course = schedule['course']
            professor = schedule['professor']
            room = schedule['room']
            time = schedule['time']
            students = schedule['students']
            
            print(f"Course: {course.course_name} ({course.course_code}), "
                  f"Professor: {professor.name}, "
                  f"Room: {room.room_number}, "
                  f"Time: {time}")
            print("  Enrolled Students:")
            for student in students:
                print(f"    - {student.name} (ID: {student.student_id})")
        print()

    @classmethod
    def menu(cls):
        print("Welcome to the Scheduling System for Students")
        print('''
            1. Add Student
            2. Add Professor
            3. Add Department
            4. Add Building
            5. Add Room to Building
            6. Add Course
            7. Assign Student to Course
            8. Assign Course to Schedule
            9. View Students
            10. View Professors
            11. View Departments
            12. View Buildings
            13. View Courses Schedules
            14. Schedule Examination
            15. Add Questions to Examination
            16. Bulk Add Questions to Examination
            17. Take Exam
            18. View Examinations by Student
            19. View Examinations by Course
            20. View Scores for an Examination
            21. View Scores by Student
            22. View All Scores
            23. Exit
        ''')
        while True:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                from student import Student
                Student.register()
            elif choice == 2:
                from professor import Professor
                Professor.register()
            elif choice == 3:
                from department import Department
                Department.add_department()
            elif choice == 4:
                from building import Building
                Building.add_building()
            elif choice == 5:
                from room import Room
                Room.add_room()
            elif choice == 6:
                from course import Course
                Course.create_course()
            elif choice == 7:
                from course import Course
                Course.assign_student()
            elif choice == 8:
                from course import Course
                Course.assign_schedule()
            elif choice == 9:
                cls.view_students()
            elif choice == 10:
                cls.view_professors()
            elif choice == 11:
                cls.view_departments()
            elif choice == 12:
                cls.view_buildings()
            elif choice == 13:
                cls.view_courses_schedules()
            elif choice == 14:
                from examination import Examination
                Examination.schedule_exam()
            elif choice == 15:
                from examination import Examination
                Examination.add_questions_to_exam()
            elif choice == 16:
                from examination import Examination
                Examination.bulk_add_questions()
            elif choice == 17:
                from examination import Examination
                Examination.take_exam()
            elif choice == 18:
                from examination import Examination
                Examination.view_exams_by_student()
            elif choice == 19:
                from examination import Examination
                Examination.view_exams_by_course()
            elif choice == 20:
                from examination import Examination
                Examination.view_scores()
            elif choice == 21:
                from examination import Examination
                Examination.view_scores_by_student()
            elif choice == 22:
                from examination import Examination
                Examination.view_all_scores()
            elif choice == 23:
                print("Exiting the system. Goodbye!\n")
                break
            else:
                print("Invalid choice. Try again.\n")
                

        