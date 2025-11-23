from book import Book
from library import Library

def main():
    library = Library()

    # Adicionando alguns livros iniciais
    library.add_book(Book("The Witcher", "Andrzej Sapkowski", 1993))
    library.add_book(Book("1984", "George Orwell", 1949))
    library.add_book(Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997))

    while True:
        print("\n--- Library Menu ---")
        print("1. List all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Add a new book")
        print("5. Check available books by year")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            library.list_books()

        elif choice == "2":
            title = input("Enter the title of the book to borrow: ").strip()
            message = library.borrow_book(title)
            print(message)

        elif choice == "3":
            title = input("Enter the title of the book to return: ").strip()
            message = library.return_book(title)
            print(message)

        elif choice == "4":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            try:
                year = int(input("Enter publication year: ").strip())
                new_book = Book(title, author, year)
                print(library.add_book(new_book))
            except ValueError as ve:
                print(f"Invalid input: {ve}")

        elif choice == "5":
            try:
                year = int(input("Enter publication year to check availability: ").strip())
                available_books = library.check_availability(year)
                if available_books:
                    print(f"\nBooks available from {year}:")
                    for book in available_books:
                        print(f"- {book.title} by {book.author}")
                else:
                    print(f"No available books found from the year {year}.")
            except ValueError:
                print("Please enter a valid number for the year.")

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")

if __name__ == "__main__":
    main()
