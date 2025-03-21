import random

def guess_the_number():
    computer = random.randint(1, 100)
    attempts = 0
    low, high = 1, 100

    print("🎯 Welcome to 'Guess the Number'!")
    print("I've chosen a number between 1 and 100. Can you guess it? 🤔")

    while True:
        try:
            num = int(input(f"Enter your guess ({low}-{high}): "))
            if num < 1 or num > 100:
                print("🚫 Out of range! Choose a number between 1 and 100.")
                continue
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")
            continue

        attempts += 1

        if num < computer:
            low = num + 1
            print("⬆️ Too low! Try a higher number.")
        elif num > computer:
            high = num - 1
            print("⬇️ Too high! Try a lower number.")
        else:
            print(f"🎉 Congratulations! You guessed the number {computer} in {attempts} attempts! 🏆")
            break

    # Ask if the user wants to play again
    play_again = input("🔄 Want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        guess_the_number()
    else:
        print("👋 Thanks for playing! See you next time.")

# Start the game
guess_the_number()
