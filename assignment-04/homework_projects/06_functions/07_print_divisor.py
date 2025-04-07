# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

# Here's a sample run (user input is in blue):

# Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12





def print_divisors(num: int):
    """
    Prints all divisors of the given number.
    
    Args:
        num (int): The number whose divisors are to be printed.
    """
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()


def main():
    """
    Asks the user for a number and prints all its divisors.
    """
    try:
        num = int(input("Enter a number: "))
        print(f"Here are the divisors of {num}:")
        print_divisors(num)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == '__main__':
    main()
