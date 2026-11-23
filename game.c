#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void showChoice(int choice) {
    if (choice == 1)
        printf("Rock");
    else if (choice == 2)
        printf("Paper");
    else
        printf("Scissors");
}

int main() {
    int player, computer;
    int playerScore = 0, computerScore = 0;
    char playAgain;

    // Initialize random numbers
    srand(time(NULL));

    printf("=================================\n");
    printf("     ROCK PAPER SCISSORS GAME\n");
    printf("=================================\n");

    do {
        printf("\nChoose your move:\n");
        printf("1. Rock\n");
        printf("2. Paper\n");
        printf("3. Scissors\n");2
        printf("Enter your choice: ");
        scanf("%d", &player);

        // Validate input
        if (player < 1 || player > 3) {
            printf("Invalid choice! Please choose 1, 2, or 3.\n");
            continue;
        }

        // Computer chooses randomly
        computer = rand() % 3 + 1;

        printf("\nYou chose: ");
        showChoice(player);

        printf("\nComputer chose: ");
        showChoice(computer);

        printf("\n");

        // Determine winner
        if (player == computer) {
            printf("It's a DRAW!\n");
        }
        else if ((player == 1 && computer == 3) ||
                 (player == 2 && computer == 1) ||
                 (player == 3 && computer == 2)) {
            printf("YOU WIN! 🎉\n");
            playerScore++;
        }
        else {
            printf("COMPUTER WINS!\n");
            computerScore++;
        }

        printf("\nScore: You %d - %d Computer\n",
               playerScore, computerScore);

        printf("\nPlay again? (y/n): ");
        scanf(" %c", &playAgain);

    } while (playAgain == 'y' || playAgain == 'Y');

    printf("\n=================================\n");
    printf("          FINAL SCORE\n");
    printf("=================================\n");
    printf("You:      %d\n", playerScore);
    printf("Computer: %d\n", computerScore);

    if (playerScore > computerScore)
        printf("Congratulations! You are the champion! 🏆\n");
    else if (playerScore < computerScore)
        printf("Computer wins the game!\n");
    else
        printf("The game ended in a draw!\n");

    printf("\nThanks for playing!\n");

    return 0;
}