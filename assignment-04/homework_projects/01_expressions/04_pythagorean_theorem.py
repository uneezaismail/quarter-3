# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.


import math

def calculate_hypotenuse():
    """Calculates the hypotenuse of a right triangle using the Pythagorean theorem."""
    
 
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse
    bc = math.sqrt(ab**2 + ac**2)

    
    print(f"The length of BC (the hypotenuse) is: {bc}")


calculate_hypotenuse()
