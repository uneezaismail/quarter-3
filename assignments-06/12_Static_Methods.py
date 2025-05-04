# 12. Static Methods

# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.


class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    

f = TemperatureConverter.celsius_to_fahrenheit(25)
print(f)    


# NOTE for me
# Static methods don’t need access to self or cls — they just do a job and work like regular functions inside a class.