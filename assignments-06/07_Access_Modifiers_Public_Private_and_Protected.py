# 7 Access Modifiers: Public, Private, and Protected

# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee:

    def __init__(self):
        self.employee_name = "Ronaldo"      # Public variable
        self._employee_salary = 1000         # Protected variable
        self.__employee_ssn = "123-45-6789"   # Private variable


emp = Employee()


print(emp.employee_name)    # public: accessible

print(emp._employee_salary) # protected: accessible but use carefully

# print(emp.__employee_ssn) # ❌ Private: gives error


# (name mangling)
print(emp._Employee__employee_ssn)  # Now accessible


