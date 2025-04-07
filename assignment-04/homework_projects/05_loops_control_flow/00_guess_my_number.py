# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48



import random


MIN_VALUE = 0
MAX_VALUE = 99

def guess_my_number():
    """A simple number guessing game."""
    
    secret_number = random.randint(MIN_VALUE, MAX_VALUE)

    print(f"I am thinking of a number between {MIN_VALUE} and {MAX_VALUE}...")

    guess = int(input("Enter a guess: "))
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        
        guess = int(input("\nEnter a new guess: "))
        
    print(f"Congrats! The number was: {secret_number}")


guess_my_number()
