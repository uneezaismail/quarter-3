# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, you should call done() and check if it returns True or not. If done() returns True, we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), which will print "done counting". We've written main() for you -- check it out! Notice that we'll only print "done counting" from main() once chaotic_counting() is done with its execution.



import random

DONE_LIKELIHOOD = 0.3

def done():

    """Randomly determines whether counting should stop based on DONE_LIKELIHOOD."""

    return random.random() < DONE_LIKELIHOOD  



def chaotic_counting():

    """Counts from 1 to 10 but may stop early depending on the done() function."""

    for num in range(1, 11): 
        if done():  
            return 
        print(num, end=" ")  



def main():

    """Runs the chaotic counting sequence and signals when it's done."""

    print("Counting from 1 to 10... but I might stop early!")
    chaotic_counting()
    print("\nDone counting.")


if __name__ == '__main__':
    main()
