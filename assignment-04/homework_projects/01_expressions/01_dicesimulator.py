
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.



# Import random module
import random

# Number of sides on each die
NUM_SIDES = 6

def roll_two_dice():
    """
    Rolls two dice and prints their values.
    """
    first_roll = random.randint(1, NUM_SIDES)  # Local variable
    second_roll = random.randint(1, NUM_SIDES)  # Local variable
    total: int = first_roll + second_roll
    print(f"First Die: {first_roll}, Second Die: {second_roll}, Total: {total}")

def run_simulation():
    """
    Calls roll_dice() three times and shows that variables inside
    roll_dice() do not affect those in run_simulation().
    """
    die1 = 10  # Local to main()
    print(f"die1 in run_simulation() starts as: {die1}")
    
    # Roll dice three times
    for _ in range(3):
        roll_two_dice()
    
    print(f"Initial value in run_simulation(): {die1}")


run_simulation()

