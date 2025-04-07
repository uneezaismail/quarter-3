import random

def computer_guess():
    """Let the computer guess the player's secret number using binary search strategy."""
    print("\n🤖 Welcome to the Computer Guessing Game!")
    
  
    while True:
        try:
            low = int(input("🔢 Enter the minimum number: "))
            high = int(input("🔢 Enter the maximum number: "))
            if low >= high:
                print("⚠️ Minimum should be less than maximum. Try again!")
            else:
                break
        except ValueError:
            print("⚠️ Invalid input! Please enter valid numbers.")

    print(f"\n📌 Think of a number between {low} and {high}. The computer will try to guess it!")
    input("✅ Press Enter when you're ready...")

    attempts = 0
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 

        attempts += 1

    
        while True:
            print("\n🔎 Enter 'H' if the guess is too high, 'L' if it's too low, or 'C' if it's correct.")
            feedback = input(f"💡 Is {guess} (H)igh, (L)ow, or (C)orrect? ").strip().lower()
            if feedback in ['h', 'l', 'c']:
                break 
            print("⚠️ Invalid input! You must enter only 'H', 'L', or 'C'.")

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"\n🎉 The computer guessed your number {guess} correctly in {attempts} attempts!\n")


computer_guess()
