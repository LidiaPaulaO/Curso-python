class Book:
    def __init__(self, title: str, author: str, publication_year: int, available: bool = True):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title cannot be empty")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Author cannot be empty")
        if not isinstance(publication_year, int) or publication_year <= 0:
            raise ValueError("Publication year must be a positive integer")
        if not isinstance(available, bool):
            raise ValueError("Available must be a boolean value")

        self._title = title.title()
        self._author = author.title()
        self._publication_year = publication_year
        self._available = available

    def __str__(self) -> str:
        status = "Available" if self._available else "Unavailable"
        return f"{self._title} | {self._author} | {self._publication_year} | {status}"

    # Getters
    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def publication_year(self) -> int:
        return self._publication_year

    @property
    def available(self) -> bool:
        return self._available

    # Setters
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("Title cannot be empty")
        self._title = new_title.title()

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, str) or not new_author.strip():
            raise ValueError("Author cannot be empty")
        self._author = new_author.title()

    @publication_year.setter
    def publication_year(self, new_year):
        if not isinstance(new_year, int) or new_year <= 0:
            raise ValueError("Publication year must be a positive integer")
        self._publication_year = new_year

    @available.setter
    def available(self, new_status):
        if not isinstance(new_status, bool):
            raise ValueError("Available must be a boolean value")
        self._available = new_status

    # Methods
    def borrow(self):
        if not self._available:
            raise Exception(f"The book '{self._title}' is already borrowed.")
        self._available = False

    def return_book(self):
        if self._available:
            raise Exception(f"The book '{self._title}' is already available.")
        self._available = True
