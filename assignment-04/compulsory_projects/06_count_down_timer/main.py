import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        print(f"\r⏳ Time Left: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        t -= 1

    print("\n🎉 Time's up! Timer completed! ⏰")


while True:
    try:
        original_time = int(input("⏰ Enter time in seconds: "))
        if original_time > 0:
            break
        print("⚠️ Please enter a positive number.")
    except ValueError:
        print("⚠️ Invalid input! Please enter a number.")

countdown(original_time)
