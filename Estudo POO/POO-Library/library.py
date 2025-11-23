from book import Book
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        # Verifica se já existe livro com mesmo título
        for b in self.books:
            if b.title.lower() == book.title.lower():
                return f"Book '{book.title}' already exists in the library."
        self.books.append(book)
        return f"Book '{book.title}' added successfully."

    def remove_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return f"Book '{title}' removed successfully."
        return f"Book '{title}' not found in the library."

    def list_books(self):
        print(f"{'Title'.ljust(45)} | {'Author'.ljust(25)} | {'Year'.ljust(5)} | {'Status'.ljust(12)}")
        print("-" * 95)
        for book in self.books:
            status = "Available" if book.available else "Unavailable"
            print(f"{book.title.ljust(45)} | {book.author.ljust(25)} | {str(book.publication_year).ljust(5)} | {status.ljust(12)}")

    def check_availability(self, publication_year: int):
        return [book for book in self.books if book.publication_year == publication_year and book.available]

    def borrow_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                try:
                    book.borrow()
                    return f"Book '{book.title}' borrowed successfully."
                except Exception as e:
                    return str(e)
        return f"Book '{title}' not found in the library."

    def return_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                try:
                    book.return_book()
                    return f"Book '{book.title}' returned successfully."
                except Exception as e:
                    return str(e)
        return f"Book '{title}' not found in the library."
