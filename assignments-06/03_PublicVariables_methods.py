# 3. Public Variables and Methods

# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:

    def __init__(self,brand):
        self.brand = brand     # public variable  

# Public method start()
    def start(self):
        print(f'Starting the engine of the {self.brand}')
        print(f'**vroom vroom.....**')    


car1 = Car("Ferrari LaFerrari")
car1.start()