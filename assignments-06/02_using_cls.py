# 2. Using cls

# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.



class Counter:
    # Class variable
    count = 0 

    def __init__(self):
        # Increase count on each object
        Counter.count += 1

    @classmethod
    def display_count(cls):
        
        print(f"Total objects created: {cls.count}")


object1 = Counter()
object2 = Counter()
object3 = Counter()


Counter.display_count()
