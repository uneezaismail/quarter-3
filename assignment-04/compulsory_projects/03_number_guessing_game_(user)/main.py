import random

def guess():
    """Let the player guess the computer's random number with input validation and feedback."""
    print("\n🎮 Welcome to the Number Guessing Game!")

   
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

    random_number = random.randint(low, high)
    attempts = 0
    guess = None

    print(f"\n🎯 Try to guess a number between {low} and {high}.")

    while guess != random_number:
        try:
            guess = int(input("💡 Your guess: "))
            attempts += 1
            if guess < low or guess > high:
                print(f"⚠️ Your guess must be within {low}-{high}. Try again!")
            elif guess < random_number:
                print("📉 Too low! Try again.")
            elif guess > random_number:
                print("📈 Too high! Try again.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

    print(f"\n🎉 Yay! You guessed the number {random_number} correctly in {attempts} attempts!\n")

guess()
