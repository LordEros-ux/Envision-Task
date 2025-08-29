import random

def number_guessing_game():
    # Computer randomly chooses a number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    while True:
        # Player makes a guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue
        
        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("Too Low! 📉 Try again.")
        elif guess > secret_number:
            print("Too High! 📈 Try again.")
        else:
            print(f"✅ Congratulations! You guessed the number {secret_number} in {attempts} attempts 🎉")
            break

# Run the game
number_guessing_game()