# 1. Using self

# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name  
        self.marks = marks

    def display(self):  
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

student1 = Student("Babar", 56)
student1.display()
