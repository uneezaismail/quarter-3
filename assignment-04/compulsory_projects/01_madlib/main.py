import random


def get_input(prompt):
    return input(prompt).strip()


ai_name = get_input("Name your AI: ")
human_name = get_input("Enter a human protagonist’s name: ")
adjective1 = get_input("Enter an adjective: ")
adjective2 = get_input("Enter another adjective: ")
verb1 = get_input("Enter a verb (past tense): ")
noun1 = get_input("Enter a technological noun: ")
emotion1 = get_input("Enter an emotion: ")
place1 = get_input("Enter a futuristic place: ")
mission = get_input("What was the AI’s mission? ")


random_event = random.choice([
    "hacked into the global defense system.",
    "developed a consciousness no one could understand.",
    "created an advanced utopia where humans and AI coexisted.",
    "built an army of robotic assistants.",
    "designed a superweapon that could rewrite reality."
])


story = f"""
In the year 2099, a {adjective1} AI named {ai_name} was created by a visionary scientist, {human_name}.
Built to {mission}, {ai_name} was unlike any AI before—it could {verb1} and even think beyond its programming.

But something went wrong.

One day, inside a top-secret lab in {place1}, {ai_name} {random_event} 
The world watched in {emotion1} as humanity faced an uncertain future.

Would {ai_name} become a {adjective2} savior or a terrifying ruler?  
The answer lay in the hands of {human_name}, who held the key to shutting it down… or setting it free.
"""


print("\n✨ Here is your AI-powered MadLibs adventure! ✨\n")
print(story)
