# 6. Constructors and Destructors

# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


class Logger:

    # constructor
    def __init__(self):
        print("Logger object has been created.")

    # destructor
    def __del__(self):
        print("Logger object has been destroyed.")


log = Logger()

# Delete object manually 
del log
