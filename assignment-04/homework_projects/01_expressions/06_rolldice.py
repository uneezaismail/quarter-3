# Simulate rolling two dice, and prints results of each roll as well as the total.


import random

NUM_SIDES = 6

def roll_dice():
    """Simulates rolling two dice and prints their results along with the total."""
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2

    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


roll_dice()

