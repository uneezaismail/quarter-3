# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

INCHES_PER_FOOT = 12  # Use uppercase for constants

def feet_to_inches():
    """Converts feet to inches and prints the result."""
    
    feet = float(input("Enter the number of feet: "))

    inches = feet * INCHES_PER_FOOT

    
    foot_label = "foot" if feet == 1 else "feet"
    inch_label = "inch" if inches == 1 else "inches"

    print(f"\n{feet} {foot_label} is equal to {inches} {inch_label}.")

feet_to_inches()  