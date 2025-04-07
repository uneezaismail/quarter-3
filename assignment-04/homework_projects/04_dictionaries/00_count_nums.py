# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.



def collect_numbers():
    """
    Collects numbers from user input and stores them in a list.
    The input stops when the user enters a blank line.
    """
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        
        if user_input == "": 
            break
        
        try:
            number = int(user_input)  
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    return numbers


def count_occurrences(numbers_list):
    """
    Counts the occurrences of each number in the provided list and 
    returns a dictionary mapping numbers to their counts.
    """
    occurrences = {}
    for num in numbers_list:
        occurrences[num] = occurrences.get(num, 0) + 1 
        if num not in occurrences:
            occurrences[num] = 1
        else:
            occurrences[num] += 1
    
    return occurrences


def display_counts(occurrences):
    """
    Displays the count of each number from the occurrences dictionary.
    """
    for num, count in occurrences.items():
        print(f"{num} appears {count} times.")


def main():
    """
    Collects numbers from the user, counts their occurrences, and prints the results.
    """
    numbers = collect_numbers()
    occurrences = count_occurrences(numbers)
    display_counts(occurrences)


if __name__ == '__main__':
    main()
