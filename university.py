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
        cls.students.append(Student("Alice", 20, "alice@university.com", "001"))
        cls.students.append(Student("Bob", 22, "bob@university.com", "002"))

        # Add Sample Professors
        cls.professors.append(Professor("Dr. John Doe", 40, "john.doe@university.com", "P001"))
        cls.professors.append(Professor("Dr. Jane Smith", 35, "jane.smith@university.com", "P002"))

        # Add Sample Departments
        cls.departments.append(Department("Science", "Dr. Einstein"))
        cls.departments.append(Department("Engineering", "Dr. Tesla"))

        # Add Sample Buildings
        building1 = Building("Main Campus", "123 University Street")
        building2 = Building("Engineering Block", "456 Tech Avenue")
        cls.buildings.extend([building1, building2])

        # Add Sample Rooms
        building1.rooms.append(Room("101", 50))
        building1.rooms.append(Room("102", 30))
        building2.rooms.append(Room("201", 40))

        # Add Sample Courses
        course1 = Course("Rekayasa Perangkat Lunak", "rpl24", cls.departments[0])
        course2 = Course("Pemrograman Basis Data", "pb24", cls.departments[0])
        cls.courses.extend([course1, course2])

        # Enroll Students in Courses
        course1.students.append(cls.students[0])  # Alice in Mathematics
        course2.students.append(cls.students[1])  # Bob in Physics

        # Add Sample Schedules
        cls.schedules.append({
            "course": course1,
            "professor": cls.professors[0],
            "room": building1.rooms[0],
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

        # Add Sample Examinations
        cls.examinations.append(Examination(course1, "Quiz", "2025-01-10", "09:00-10:00"))
        cls.examinations.append(Examination(course1, "Final Exam", "2025-01-25", "10:00-12:00"))
        cls.examinations.append(Examination(course2, "Midterm", "2025-02-15", "14:00-16:00"))
        cls.examinations.append(Examination(course2, "Final Exam", "2025-03-20", "08:00-10:00"))

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

    @classmethod
    def view_courses(cls):
        if not cls.courses:
            print("No courses available.\n")
            return
        print("List of Courses:")
        for course in cls.courses:
            print(course)
            print("  Enrolled Students:")
            for student in course.students:
                print(f"    - {student.name} (ID: {student.student_id})")
        print()

    @classmethod
    def view_schedules(cls):
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
            9. View Schedules
            10. View Students
            11. View Professors
            12. View Departments
            13. View Buildings
            14. View Courses
            15. Schedule Examination
            16. Add Questions to Examination
            17. Bulk Add Questions to Examination
            18. Take Exam
            19. View Examinations by Student
            20. View Examinations by Course
            21. View Scores for an Examination
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
                cls.view_schedules()
            elif choice == 10:
                cls.view_students()
            elif choice == 11:
                cls.view_professors()
            elif choice == 12:
                cls.view_departments()
            elif choice == 13:
                cls.view_buildings()
            elif choice == 14:
                cls.view_courses()
            elif choice == 15:
                from examination import Examination
                Examination.schedule_exam()
            elif choice == 16:
                from examination import Examination
                Examination.add_questions_to_exam()
            if choice == 17:
                from examination import Examination
                Examination.bulk_add_questions()
            elif choice == 18:
                from examination import Examination
                Examination.take_exam()
            elif choice == 21:
                from examination import Examination
                Examination.view_scores()
            elif choice == 22:
                from examination import Examination
                Examination.view_all_scores()
            elif choice == 23:
                print("Exiting the system. Goodbye!\n")
                break
            else:
                print("Invalid choice. Try again.\n")


        