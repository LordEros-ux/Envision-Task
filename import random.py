#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int secretNumber, guess, attempts;
    char choice;

    srand(time(0)); // Seed the random number generator

    do {
        // Reset attempts for each new game
        attempts = 0;
        secretNumber = rand() % 100 + 1; // Random number between 1 and 100

        printf("\n🎯 Welcome to the Number Guessing Game!\n");
        printf("I'm thinking of a number between 1 and 100...\n");

        // Game loop
        do {
            printf("Enter your guess: ");
            scanf("%d", &guess);
            attempts++;

            if (guess < secretNumber) {
                printf("Too Low! 📉 Try again.\n");
            } else if (guess > secretNumber) {
                printf("Too High! 📈 Try again.\n");
            } else {
                printf("✅ Congratulations! You guessed the number %d in %d attempts 🎉\n", secretNumber, attempts);
            }
        } while (guess != secretNumber);

        // Ask if the user wants to play again
        printf("\nDo you want to play again? (y/n): ");
        scanf(" %c", &choice); // Notice the space before %c to ignore newline char

    } while (choice == 'y' || choice == 'Y');

    printf("\n👋 Thanks for playing! Goodbye!\n");
    return 0;
}
