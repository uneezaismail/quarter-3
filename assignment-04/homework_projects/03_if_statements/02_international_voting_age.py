# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# Here's a sample run of the program (user input is in blue):

# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.



PETURKSBOUIPO_VOTING_AGE : int = 16
STANLAU_VOTING_AGE : int = 25
MAYENGUA_VOTING_AGE : int = 48

def can_vote():
    
    user_age = int(input("How old are you? "))

    # check whether user can vote in the respective country
    if user_age >= PETURKSBOUIPO_VOTING_AGE:
        print(f"You are eligible for voting in Peturksbouipo where the voting age is {PETURKSBOUIPO_VOTING_AGE}")
    else:
        print(f"You are not eligible for voting in Peturksbouipo where the voting age is {PETURKSBOUIPO_VOTING_AGE}")

    if user_age >= STANLAU_VOTING_AGE:
        print(f"You are eligible for voting in stanlau where the voting age is {STANLAU_VOTING_AGE}")
    else:
        print(f"You are not eligible for voting in stanlau where the voting age is {STANLAU_VOTING_AGE}")

    if user_age >= MAYENGUA_VOTING_AGE:
        print(f"You are eligible for voting in mayengua where the voting age is {MAYENGUA_VOTING_AGE}")
    else:
        print(f"You are not eligible for voting in mayengua where the voting age is {MAYENGUA_VOTING_AGE}")


can_vote()