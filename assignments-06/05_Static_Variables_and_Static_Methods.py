# 5. Static Variables and Static Methods

# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.


class MathUtils:

    # static method
    @staticmethod
    def add(a, b):
        return a + b

# static method do not need to create object
result = MathUtils.add(5, 3)
print(result) 
