# Write a function that takes a list of numbers and returns the sum of those numbers.


def sum_numbers(numbers):
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    numbers_sum = 0

    for number in numbers:
        numbers_sum += number

    return numbers_sum   


result = sum_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(result)
