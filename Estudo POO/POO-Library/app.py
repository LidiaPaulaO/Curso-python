# main.py
from book import Book
from library import Library

def main():
    library = Library()
    
    # Adicionando alguns livros iniciais
    library.add_book(Book("The Witcher","Andrzej Sapkowski", 1993))
    library.add_book(Book("1984","George Orwell", 1949))
    library.add_book(Book("Harry Potter and the Philosopher's Stone","J.K. Rowling", 1997))

    while True:
        print("\n--- Library Menu ---")
        print("1. List all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Add a new book")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            library.list_books()
        elif choice == "2":
            title = input("Enter the title of the book to borrow: ").strip()
            try:
                message = library.borrow_book(title)
                print(message)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            title = input("Enter the title of the book to return: ").strip()
            try:
                message = library.return_book(title)
                print(message)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "4":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            try:
                year = int(input("Enter publication year: ").strip())
                new_book = Book(title, author, year)
                library.add_book(new_book)
                print(f"Book '{title}' added successfully.")
            except ValueError as ve:
                print(f"Invalid input: {ve}")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
