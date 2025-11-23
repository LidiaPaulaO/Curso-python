

class Book:
    _all_books = []
    def __init__(self,_title: str, _author: str, _publication_year: int, _available: bool = True):
        if not isinstance(_title,str ) or not _title.strip():
            raise ValueError("Title cannot be empty")
        
        if not isinstance(_author,str) or not _author.strip():
            raise ValueError("Author cannot be empty")
        
        if not isinstance(_publication_year, int) or _publication_year <= 0:
            raise ValueError("Publication year must be a number greater than 0")
        
        if not isinstance(_available,bool):
            raise ValueError("Available must be a boolean value")
        
        
        self._title = _title.title()
        self._author = _author.title()
        self._publication_year = _publication_year
        self._available = _available
        Book._all_books.append(self)
        
    def __str__(self) -> str:
        status = "Avaliable" if self._available else "Unavailable"
        return f"Book: {self._title} | Author: {self._author} | Publication Year: {self._publication_year} | Status: {status}"

    # getters
    @property
    def title(self) -> str:       
        return self._title   
    @property
    def author(self) -> str:
        return self._author
    @property
    def  publication_year(self) -> int:
        return self._publication_year
    @property
    def available(self) -> bool:
        return self._available
    
    # setters
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
            raise ValueError("Publication year must be a number greater than 0")
        self._publication_year = new_year

    @available.setter
    def available(self, new_status):
        if not isinstance(new_status, bool):
            raise ValueError("Available must be a boolean value")
        self._available = new_status
    
    def borrow(self):
        if not self._available:
            raise Exception(f"The book '{self.title}' is already borrowed.")
        self._available = False

    def return_book(self):
        if self._available:
            raise Exception(f"The book '{self.title}' is already available.")
        self._available = True

    