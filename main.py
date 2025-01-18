from university import University
from student import Student
from professor import Professor
from course import Course
from building import Building
from room import Room
from examination import Examination

if __name__ == "__main__":
    University.load_sample_data()  # Load sample data on startup
    University.menu()
