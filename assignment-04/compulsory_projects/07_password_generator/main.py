import random
import string

def generate_passwords():
    print("🔐 Welcome to the Password Generator!\n")


    while True:
        try:
            num_passwords = int(input("📌 How many passwords do you want to generate? "))
            length = int(input("🔢 Enter desired password length: "))
            if num_passwords > 0 and length > 0:
                break
            print("⚠️ Please enter a positive number.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")


    chars = string.ascii_letters + string.digits + string.punctuation

    print("\n🎉 Here are your secure passwords:\n")
    
    for _ in range(num_passwords):
        password = "".join(random.choice(chars) for _ in range(length))
        print(f"🔑 {password}")

    print("\n✅ Keep them safe! 🔐")

generate_passwords()
