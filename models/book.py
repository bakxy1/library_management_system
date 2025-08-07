from uuid import uuid4


class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.__id = str(uuid4())
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.is_avaiable = True

    def __repr__(self):
        return f"id: {self.__id} title: {self.title} | author: {self.author} | available: {self.is_avaiable}"
