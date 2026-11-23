#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
void add_Book() {
    char bookName[100];
    int bookNumber;
    char bookAuthor[100];
    int bookYear;
    printf("Enter the name of the book: ");
    scanf(" %[^\n]s", bookName);
    printf("Enter the book number: ");
    scanf("%d", &bookNumber);
    printf("Enter the author's name: ");
    scanf(" %[^\n]s", bookAuthor);
    printf("Enter the publication year: ");
    scanf("%d", &bookYear);
    printf("Adding book '%s' (Number: %d) to the library...\n", bookName, bookNumber);
    printf("Book '%s' (Number: %d) added successfully.\n", bookName, bookNumber);

}
void search_Book() {
    char bookName[100];
    int bookNumber;
    char bookAuthor[100];
    int bookYear;
    printf("Enter the name of the book to search: ");
    scanf(" %[^\n]s", bookName);
    printf("Enter the book number: ");
    scanf("%d", &bookNumber);
    printf("Enter the author's name: ");
    scanf(" %[^\n]s", bookAuthor);
    printf("Enter the publication year: ");
    scanf("%d", &bookYear);
    printf("Searching for book '%s' (Number: %d)...\n", bookName, bookNumber);
}
void delete_Book() {
    char bookName[100];
    int bookNumber;
    char bookAuthor[100];
    int bookYear;
    printf("Enter the name of the book to delete: ");
    scanf(" %[^\n]s", bookName);
    printf("Enter the book number: ");
    scanf("%d", &bookNumber);
    printf("Enter the author's name: ");
    scanf(" %[^\n]s", bookAuthor);
    printf("Enter the publication year: ");
    scanf("%d", &bookYear);
    printf("Deleting book '%s' (Number: %d)...\n", bookName, bookNumber);
}
void sort_Books() {
    // Sorting logic can be implemented here
    // For demonstration, we'll just print a placeholder message
    printf("Sorting books in the library...\n");
    char bookName[100];
    int bookNumber;
    char bookAuthor[100];
    int bookYear;       
    printf("Enter the name of the book to sort: ");
    scanf(" %[^\n]s", bookName);
    printf("Enter the book number: ");
    scanf("%d", &bookNumber);
    printf("Enter the author's name: ");
    scanf(" %[^\n]s", bookAuthor);
    printf("Enter the publication year: ");
    scanf("%d", &bookYear);
    printf("Books sorted successfully.\n");
}
void main() {
    char bookName[100];
    int bookNumber;
    char bookAuthor[100];
    int bookYear;
    while (true) {
        printf("\nLibrary Management System Menu:\n");
        printf("1. Add Book\n");
        printf("Enter the name of the book to add: ");
        scanf(" %[^\n]s", bookName);
        printf("Enter the book number: ");
        scanf("%d", &bookNumber);
        printf("Enter the author's name: ");
        scanf(" %[^\n]s", bookAuthor);
        printf("Enter the publication year: ");
        scanf("%d", &bookYear);
        printf("2. Search Book\n");
        printf("3. Delete Book\n");
        printf("4. Sort Books\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        
        int choice;
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                add_Book();
                break;
            case 2:
                search_Book();
                break;
            case 3:
                delete_Book();
                break;
            case 4:
                sort_Books();
                break;
            case 5:
                printf("Exiting the program.\n");
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }
}