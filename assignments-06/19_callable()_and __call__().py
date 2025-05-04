# 19. callable() and __call__()

# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function



class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor


m = Multiplier(3)

# callable()
print(callable(m))     

# Call object
result = m(10)
print(result)         
