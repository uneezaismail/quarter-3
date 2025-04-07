# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]


def double_numbers():
    """
    Doubles each element in the global 'numbers' list.
    """

    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(len(numbers)):
        numbers[i] *= 2   
        
    print(numbers)

double_numbers() 
