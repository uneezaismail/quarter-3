# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------\n")

    your_score = 0  # Milestone 5

    # Milestone 4
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Milestone 1
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print(f"Your number is {your_num}")

        # Milestone 2
        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Extension 1
        while choice not in ["higher", "lower"]:
            choice = input("Please enter either 'higher' or 'lower': ").lower()

        # Milestone 3
        is_correct = (
            (choice == "higher" and your_num > computer_num) or
            (choice == "lower" and your_num < computer_num)
        )

        if is_correct:
            print(f"You were right! The computer's number was {computer_num}.")
            your_score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}.")

       
        print(f"Your score is now {your_score}\n")

  
    print(f"Your final score is {your_score} out of {NUM_ROUNDS}.")

    # Extension 2
    if your_score == NUM_ROUNDS:
        print("🎯 Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("👏 Good job, you played really well!")
    else:
        print("💡 Better luck next time!")


if __name__ == "__main__":
    main()
