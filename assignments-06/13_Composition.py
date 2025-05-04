# 13. Composition

# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
    def ignite(self):
        print("The engine is roaring to life!")

class Car:
    def __init__(self, engine_object):
        self.engine = engine_object  # composition

    def start_engine(self):
        print("Starting the car...")
        self.engine.ignite()    # Accessing Engine's method

engine = Engine()
car = Car(engine)
car.start_engine()
