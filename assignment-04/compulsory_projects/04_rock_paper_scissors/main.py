import random
import time


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def play():
    """Enhanced Rock, Paper, Scissors Game"""
    print(f"\n🎮 {BOLD}Welcome to Rock, Paper, Scissors!{RESET}")

    user_score = 0
    computer_score = 0
    rounds_to_win = 3 

    while user_score < rounds_to_win and computer_score < rounds_to_win:
        print(f"\n{CYAN}🔹 Score: You {user_score} - {computer_score} Computer 🔹{RESET}")
        user = get_user_choice()
        
        if user == 'q':
            print(f"\n{YELLOW}👋 Exiting the game... See you next time!{RESET}")
            return
        
        computer = random.choice(['r', 'p', 's'])

        print(f"\n🧑‍💻 {BOLD}You chose:{RESET} {convert_choice(user)}")
        time.sleep(0.5) 
        print(f"🤖 {BOLD}Computer chose:{RESET} {convert_choice(computer)}")
        time.sleep(0.5)

        result = determine_winner(user, computer)

        if result == "win":
            print(f"{GREEN}🎉 You won this round!{RESET}")
            user_score += 1
        elif result == "lose":
            print(f"{RED}😢 You lost this round!{RESET}")
            computer_score += 1
        else:
            print(f"{YELLOW}🤝 It's a tie!{RESET}")

        time.sleep(1)

   
    print(f"\n🏆 {BOLD}FINAL SCORE:{RESET} You {user_score} - {computer_score} Computer")
    if user_score > computer_score:
        print(f"{GREEN}🎊 Congratulations! You won the game!{RESET}")
    else:
        print(f"{RED}💀 The computer won this time. Better luck next time!{RESET}")


    if play_again():
        play()
    else:
        print(f"\n{YELLOW}👋 Thanks for playing! Goodbye!{RESET}")

def get_user_choice():
    """Get a valid user input for Rock, Paper, Scissors."""
    while True:
        user = input(f"\nChoose: {BOLD}'r'{RESET} for Rock, {BOLD}'p'{RESET} for Paper, {BOLD}'s'{RESET} for Scissors (or {BOLD}'q'{RESET} to Quit): ").strip().lower()
        if user in ['r', 'p', 's', 'q']:
            return user
        print(f"{RED}⚠️ Invalid choice! Please enter 'r', 'p', 's', or 'q'.{RESET}")

def determine_winner(player, opponent):
    """Determine the winner of the round."""
    if player == opponent:
        return "tie"
    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):
        return "win"
    return "lose"

def convert_choice(choice):
    """Convert single-letter choices to full words with emojis."""
    choices = {
        "r": "Rock 🪨",
        "p": "Paper 📄",
        "s": "Scissors ✂️"
    }
    return choices.get(choice, "Invalid Choice")

def play_again():
    """Ask the user if they want to play again."""
    while True:
        again = input(f"\n🔄 {BOLD}Do you want to play again?{RESET} ({GREEN}y{RESET}/{RED}n{RESET}): ").strip().lower()
        if again in ['y', 'n']:
            return again == 'y'
        print(f"{RED}⚠️ Invalid input! Please enter 'y' or 'n'.{RESET}")

play()
