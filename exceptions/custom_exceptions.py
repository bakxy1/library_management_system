class BookNotAvailableError(Exception):
    def __init__(self, book_title: str) -> None:
        super().__init__(f"The book '{book_title}' is currently not available")


class BookNotFoundError(Exception):
    def __init__(self, book_title: str) -> None:
        super().__init__(f"The book '{book_title}' can not be found")
