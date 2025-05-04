# 14. Aggregation

# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.



class Employee:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"Employee Name: {self.name}")



class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation

    def show_department(self):
        print(f"Department: {self.dept_name}")
        self.employee.show_details()  # Accessing Employee method



# independently employee created
emp1 = Employee("Mr.Beast")
emp1.show_details()  # working


# create Department with existing Employee
dept1 = Department("HR", emp1)


# Show both classes
dept1.show_department()


# delete dept1
del dept1


# emp1 still exists
emp1.show_details()  # still working
