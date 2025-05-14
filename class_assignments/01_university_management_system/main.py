# Base class for Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name, self.age


# Student class inherits from Person
class Student(Person):
    def __init__(self, name, age, rollNumber):
        super().__init__(name, age)
        self.rollNumber = rollNumber
        self.courses = []

    def registerForCourses(self, course):
        self.courses.append(course)
        course.addStudent(self)


# Instructor class inherits from Person
class Instructor(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = []

    def assignCourse(self, course):
        self.courses.append(course)
        course.setInstructor(self)


# Course class
class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name
        self.students = []
        self.instructor = None

    def addStudent(self, student):
        self.students.append(student)

    def setInstructor(self, instructor):
        self.instructor = instructor

# Department class
class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def addCourse(self, course):
        self.courses.append(course)



# Create Department
cs_department = Department("Computer Science")

# Create Courses
course1 = Course("CS101", "Intro to Python")
course2 = Course("CS102", "Data Structures")


# Add Courses to Department
cs_department.addCourse(course1)
cs_department.addCourse(course2)


# Create Instructor
instructor1 = Instructor("Sir Hamzah", 45, 90000)
instructor1.assignCourse(course1)


# Create Student
student1 = Student("Uneeza Ismail", 20, "S123")
student1.registerForCourses(course1)


# Output
instructor_name, instructor_age = course1.instructor.getName()
instructor_salary = course1.instructor.salary

print("📘 Course Details")
print("----------------------------")
print(f"📚 Course Name     : {course1.name}")
print(f"👨‍🏫 Instructor     : {instructor_name}")
print(f"🎂 Instructor Age  : {instructor_age}")
print(f"💰 Salary          : ${instructor_salary}")
print()

student_name, student_age = student1.getName()
print("🧑‍🎓 Student Details")
print("----------------------------")
print(f"👤 Name            : {student_name}")
print(f"🎂 Age             : {student_age}")
print(f"📝 Enrolled Course : {[c.name for c in student1.courses][0]}")

