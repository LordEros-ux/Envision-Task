# Online Python com
import random
import time
from termcolor import colored

# ASCII Art for choices
ascii_art = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
}

choices = ["rock", "paper", "scissors"]

# Scoreboard
player_score = 0
computer_score = 0

def print_slow(text, color="white"):
    for char in text:
        print(colored(char, color), end="", flush=True)
        time.sleep(0.02)
    print()

print(colored("Welcome to Fancy Rock–Paper–Scissors! ✊📄✂️", "cyan"))

while True:
    print("\nChoose: rock, paper, or scissors")
    player_choice = input(colored("👉 Your choice: ", "yellow")).lower()

    if player_choice not in choices:
        print(colored("Invalid choice! Try again...", "red"))
        continue

    computer_choice = random.choice(choices)

    print_slow("\nYou chose:", "green")
    print(colored(ascii_art[player_choice], "green"))

    print_slow("Computer chose:", "magenta")
    print(colored(ascii_art[computer_choice], "magenta"))

    if player_choice == computer_choice:
        print(colored("😲 It's a draw!", "cyan"))
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print(colored("🎉 You win this round!", "green"))
        player_score += 1
    else:
        print(colored("💻 Computer wins this round!", "red"))
        computer_score += 1

    print(colored(f"Score → You: {player_score} | Computer: {computer_score}", "yellow"))

    play_again = input(colored("\nPlay again? (y/n): ", "cyan")).lower()
    if play_again != "y":
        print(colored("Thanks for playing! Goodbye 👋", "blue"))
        break
