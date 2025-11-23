
from book import Book
class Library:
    
    def __init__(self):
        self.books = []
    
    
    def add_book(self,book):
        self.books.append(book)
        return f"Book {book.title} added successfully"
        
    
    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return f"Book {title} removed successfully"
        return "Book not found"
    
    
    def list_books(self):
        print(f"{'Título'.ljust(45)} | {'Author'.ljust(25)} | {'Publication Year'.ljust(15)} | {'Status'.ljust(12)}")
        print("-" * 100)

        for book in self.books:
            status_str = "Avaliable" if book.available else "Unavailable"
            print(
                f"{book.title.ljust(45)} | "
                f"{book.author.ljust(25)} | "
                f"{str(book.publication_year).ljust(16)} | "
                f"{status_str.ljust(12)}"
            )
    
    
    def check_availability(self, publication_year: int):
        return [ book for book in self.books if book.publication_year == publication_year and book.available]
    
    
    def borrow_book(self, title: str):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return f"Book {title} borroed successfully"
        
    def return_book(self, title: str):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return f"Book {title} returned successfully"
    