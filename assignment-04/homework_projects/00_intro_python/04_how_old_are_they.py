# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! 

def age():
    anton_age = 21
    beth_age = anton_age + 6
    chen_age = beth_age + 20
    drew_age = chen_age + anton_age
    Ethan_age = chen_age

    print(f"Anton age is {anton_age}")
    print(f"Beth age is {beth_age}")
    print(f"Chen age is {chen_age}")
    print(f"Drew age is {drew_age}")
    print(f"Ethan age is {Ethan_age}")

age()    
                            