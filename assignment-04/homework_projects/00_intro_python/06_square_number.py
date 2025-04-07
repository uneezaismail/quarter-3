# Ask the user for a number and print its square (the product of the number times itself).

def square():
    user_number = float(input("Type a number to see its square : "))

    square_of_number = user_number ** 2

    print(f"\nThe square of {user_number} is {square_of_number}")

square()    