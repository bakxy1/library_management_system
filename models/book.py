from uuid import uuid4


class Book:
    def __init__(
        self,
        isbn: str,
        title: str,
        author: str,
        publisher: str,
        year: int,
        genre: str,
        copies: int,
        available: int = 1,
        status: str = "Available",
    ):
        self.id = str(uuid4())
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.copies = copies
        self.available = available
        self.status = status

    def __repr__(self):
        return (
            f"id: {self.id} | title: {self.title} | author: {self.author} | "
            f"publisher: {self.publisher} | year: {self.year} | genre: {self.genre} | "
            f"available: {self.available}"
        )
