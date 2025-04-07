# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.


def divide_numbers():
    
    numerator = int(input("Please enter an integer to be divided: "))
    denominator = int(input("Please enter an integer to divide by: "))

    # throw error when dividing by zero
    if denominator == 0:
        print("Error: Division by zero is not allowed.")
        return

    
    quotient_result = numerator // denominator
    remainder_result = numerator % denominator


    print(f"The result of this division is {quotient_result} with a remainder of {remainder_result}")

divide_numbers()
