# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!


CORRECT_AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def affirmation_prompt():
    print(f"Please type the following affirmation: {CORRECT_AFFIRMATION}")

    user_input = input() 
    while user_input != CORRECT_AFFIRMATION: 
       
        print("That was not the affirmation.")

       
        print(f"Please type the following affirmation: {CORRECT_AFFIRMATION}")
        user_input = input()

    print("That's right! :)")

affirmation_prompt()
