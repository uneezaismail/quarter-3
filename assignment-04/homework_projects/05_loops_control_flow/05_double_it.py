# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.



def double_until_limit():
    curr_value = int(input("Enter a number: ")) 

    while curr_value < 100:
        curr_value *= 2  
        print(curr_value, end=" ")  


double_until_limit()
