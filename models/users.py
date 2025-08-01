from abc import ABC, abstractmethod
from models.book import Book


class User(ABC):

    name: str
    borrowed_books: list[Book]

    @abstractmethod
    def get_user_info(self) -> str:
        pass

    @abstractmethod
    def borrow_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def return_book(self, book: Book) -> None:
        pass


class Member(User):
    def __init__(self, name) -> None:
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        self.borrowed_books.remove(book)

    def get_user_info(self) -> str:
        return f"Member: {self.name}"


class Librarian(User):
    def __init__(self, name) -> None:
        self.name = name

    def get_user_info(self) -> str:
        return f"Librarian: {self.name}"

    def borrow_book(self, book: Book) -> None:
        pass

    def return_book(self, book: Book) -> None:
        pass
