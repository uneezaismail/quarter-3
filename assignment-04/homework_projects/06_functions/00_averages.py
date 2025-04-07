# Write a function that takes two numbers and finds the average between the two.



def midpoint(x: float, y: float) -> float:
    """
    Calculates the midpoint between two numbers x and y.
    """
    total_sum = x + y 
    return total_sum / 2 

def main():
    mid_1 = midpoint(0, 10)
    mid_2 = midpoint(8, 10)
    
    final_mid = midpoint(mid_1, mid_2)

    print(f"mid_1: {mid_1}")
    print(f"mid_2: {mid_2}")
    print(f"final_mid: {final_mid}")


if __name__ == '__main__':
    main()
