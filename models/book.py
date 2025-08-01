class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.is_avaiable = True
