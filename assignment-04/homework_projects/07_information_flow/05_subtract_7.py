# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.


def subtract_seven(num):
    """Subtracts 7 from num and returns the result."""
    num = num - 7
    return num

def main():
    number = int(input("Enter a number: ")) 
    result = subtract_seven(number)  
    print(f"Result after subtracting 7 from {number}: {result}")  


if __name__ == "__main__":
    main()
