# Write a program to print terms in the Fibonacci sequence up to a maximum value.

# Write a program that displays the terms in the Fibonacci sequence, starting with Fib(0) and continuing as long as the terms are less than 10,000 (you should store this value as a constant!). Thus, your program should produce the following sample run:

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765


MAX_LIMIT = 10000

def generate_fibonacci():
    """Prints Fibonacci sequence up to MAX_LIMIT."""
    prev_num = 0  
    curr_num = 1  

    while prev_num <= MAX_LIMIT:
        
        print(prev_num, end=" ")
        next_num = prev_num + curr_num  
        prev_num = curr_num  
        curr_num = next_num  

generate_fibonacci()
