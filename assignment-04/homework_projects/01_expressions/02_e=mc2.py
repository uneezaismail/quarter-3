# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2
# speed of light -- C = 299792458 m/s



SPEED_OF_LIGHT = 299792458  

def calculate_energy():
    """
    Asks the user for mass and calculates energy using E = m * c^2.
    """
    
    print("\n*****Let's calculate energy using the famous mass-energy equation!****\n")

    mass_kg = float(input("Enter mass in kilograms: "))

    # get energy using Einstein's equation ( E = m * c**2 )
    energy_joules = mass_kg * (SPEED_OF_LIGHT ** 2)

   
    print("\nUsing E = m * c^2...")
    print(f"Mass: {mass_kg} kg")
    print(f"Speed of light: {SPEED_OF_LIGHT} m/s")
    print(f"Energy: {energy_joules} joules!")


calculate_energy()
