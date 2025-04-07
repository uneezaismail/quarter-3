# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd



def main():
    """
    Iterates through numbers from 10 to 19 and prints whether each number is odd or even.
    """
    for i in range(10, 20):  
        if is_odd(i):
            print(f"{i} odd") 
        else:
            print(f"{i} even")

def is_odd(value: int):
    """
    Determines whether a given number is odd.
    
    Args:
        value (int): The number to check.
    
    Returns:
        bool: True if the number is odd, False if even.
    """
    return value % 2 == 1  


if __name__ == '__main__':
    main()
