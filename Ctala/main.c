#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <stdlib.h>
void bankManagementSystem() {
    printf("\n==BANK MANAGEMENT SYSTEM==\n");
    int choice;
    printf("1. Check Balance\n");
    printf("2. Deposit Money\n");
    printf("3. Withdraw Money\n");
    printf("4. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Your balance is $1000\n");
            int 
            break;
        case 2:
            printf("Enter amount to deposit: ");
            int deposit;
            scanf("%d", &deposit);
            printf("$%d deposited successfully!\n", deposit);
            break;
        case 3:
            printf("Enter amount to withdraw: ");
            int withdraw;
            scanf("%d", &withdraw);
            if (withdraw > 1000) {
                printf("Insufficient funds!\n");
            } else {
                printf("$%d withdrawn successfully!\n", withdraw);
            }
            break;
        case 4:
            printf("Exiting the system. Goodbye!\n");
            exit(0);
        default:
            printf("Invalid choice! Please try again.\n");
    }
}
void mainMenu() {
    int choice;
    do {
        printf("\n==MAIN MENU==\n");
        printf("1. Bank Management System\n");
        printf("2. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                bankManagementSystem();
                break;
            case 2:
                printf("Exiting the program. Goodbye!\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    } while (choice != 2);
}

    int main() {
    mainMenu();
    return 0;

}
