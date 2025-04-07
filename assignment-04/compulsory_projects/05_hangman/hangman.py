import random
from words import words
import string

HANGMAN_PICS = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
          ===
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
          ===
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
          ===
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
          ===
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
          ===
    """,
    """
       -----
       |   |
       O   |
           |
           |
          ===
    """,
    """
       -----
       |   |
           |
           |
           |
          ===
    """
]

def get_valid_word(words):
    """Select a random valid word from the list."""
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    """Fun and interactive Hangman game."""
    print("\n🎮 Welcome to Hangman! Try to guess the word before you run out of lives! 🎭\n")

    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = len(HANGMAN_PICS) - 1  

    while len(word_letters) > 0 and lives >= 0:
        print(HANGMAN_PICS[lives])  
        print(f"\n💀 Lives left: {lives}")
        print(f"📜 Used letters: {' '.join(sorted(used_letters)) if used_letters else 'None'}")

       
        word_display = ' '.join([letter if letter in used_letters else '-' for letter in word])
        print(f"\n📝 Word: {word_display}")

        user_letter = input("\n🔠 Guess a letter: ").strip().upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("\n✅ Good job! That letter is in the word!")
            else:
                lives -= 1  
                print(f"\n❌ Oops! '{user_letter}' is not in the word.")

        elif user_letter in used_letters:
            print("\n⚠️ You've already guessed that letter. Try a different one!")

        else:
            print("\n🚫 Invalid input! Please enter a valid letter.")

   
    if lives < 0:
        print(HANGMAN_PICS[0])
        print(f"\n💀 You lost! The word was: **{word}**. Better luck next time!")
    else:
        print(f"\n🎉 YAY! You guessed the word **{word}** correctly! You're a Hangman master! 🏆")

if __name__ == '__main__':
    hangman()
