from models.book import Book
from models.users import Librarian, Member, User


class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books: list[Book] = []
        self.users: list[User] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def register_user(self, user: User) -> None:
        self.users.append(user)

    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if title == book.title:
                return book
        return None
