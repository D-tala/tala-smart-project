from timeit import main


print("=======MODERN LIBRARY MANAGEMENT SYSTEM=======")
print("Welcome to the Modern Library Management System!")

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the publication year: ")
    isbn = input("Enter the ISBN number: ")
    book_number = input("Enter the book number: ")
    
    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "ISBN": isbn,
        "Number": book_number
    }
    
    # Here you would typically save the book to a database or a file
    print(f"Book '{title}' (Number: {book_number}) added successfully!")
def view_books():
    # Here you would typically retrieve the books from a database or a file
    print("Viewing all books in the library..."))
    # For demonstration, we'll just print a placeholder message
    print("No books available at the moment.")

def search_book():
    search_title = input("Enter the title of the book to search: ")
    search_number = input("Enter the book number: ")
    # Here you would typically search for the book in a database or a file
    print(f"Searching for book with title '{search_title}' (Number: {search_number})...")
    # For demonstration, we'll just print a placeholder message
    print("Book not found.")

def update_book():
    update_title = input("Enter the title of the book to update: ")
    update_number = input("Enter the book number: ")
    # Here you would typically search for the book and update its details in a database or a file
    print(f"Updating book with title '{update_title}'...")
    # For demonstration, we'll just print a placeholder message
    print("Book updated successfully.")

def delete_book():
    delete_title = input("Enter the title of the book to delete: ")
    # Here you would typically search for the book and delete it from a database or a file
    print(f"Deleting book with title '{delete_title}'...")
    # For demonstration, we'll just print a placeholder message
    print("Book deleted successfully.")
    
def check_availability():
    check_title = input("Enter the title of the book to check availability: ")
    # Here you would typically search for the book in a database or a file
    print(f"Checking availability of book with title '{check_title}'...")
    # For demonstration, we'll just print a placeholder message
    print("Book is available.")

def filter_books():
    filter_author = input("Enter the author's name to filter books: ")
    # Here you would typically filter the books by author in a database or a file
    print(f"Filtering books by author '{filter_author}'...")
    # For demonstration, we'll just print a placeholder message
    print("No books found for the specified author.")

def sort_books():
    sort_option = input("Enter 'title' to sort by title or 'year' to sort by publication year: ")
    # Here you would typically sort the books in a database or a file
    print(f"Sorting books by '{sort_option}'...")
    # For demonstration, we'll just print a placeholder message
    print("Books sorted successfully.")

def main():
    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Check Availability")
        print("7. Filter Books by Author")
        print("8. Sort Books")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            update_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            check_availability()
        elif choice == '7':
            filter_books()
        elif choice == '8':
            sort_books()
        elif choice == '9':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")
