# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.



# Sample inventory
INVENTORY = {
    "apple": 50,
    "banana": 30,
    "orange": 20,
    "pear": 1000,
    "grape": 75
}


def num_in_stock(fruit):

    """Returns the number of the given fruit in stock, or 0 if not found."""

    if fruit in INVENTORY:
        return INVENTORY[fruit]
    else:
        return 0

def main():
    
    fruit = input("Enter a fruit: ").strip().lower()
    stock = num_in_stock(fruit)

    if stock > 0:
        print("\nThis fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("\nThis fruit is not in stock.")


if __name__ == "__main__":
    main()
