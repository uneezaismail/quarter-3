# 8. The super() Function

# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.



# parent class 
class Person:
    def __init__(self, name):
        self.name = name


# child class 
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # calling the Parent
        self.subject = subject




teacher1 = Teacher("Elsa", "Programmer")


print(f"Teacher Name: {teacher1.name}")
print(f"Subject: {teacher1.subject}")
