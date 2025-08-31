import random

def number_guessing_game():
    while True:
        secret_number = random.randint(1, 100)
        attempts = 0

        print("\n🎯 Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100...")

        # Game loop
        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("❌ Please enter a valid number!")
                continue

            attempts += 1

            if guess < secret_number:
                print("📉 Too Low! Try again.")
            elif guess > secret_number:
                print("📈 Too High! Try again.")
            else:
                print(f"✅ Congratulations! You guessed the number {secret_number} in {attempts} attempts 🎉")
                break

        # Ask if the player wants to play again
        choice = input("\nDo you want to play again? (y/n): ").strip().lower()
        if choice != 'y':
            print("\n👋 Thanks for playing! Goodbye!")
            break

# Run the game
number_guessing_game()

