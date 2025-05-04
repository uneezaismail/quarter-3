# 10. Instance Methods

# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.



class Dog:
    def __init__(self, name, breed):
        self.name = name    # Instance variable
        self.breed = breed  

    def bark(self):          # Instance method
        print(f"{self.name} is barking! Woof woof!")



dog1 = Dog("Bella", "Samoyed")


dog1.bark()
