import json
from models.book import Book
from models.library import Library
from models.users import Member
from services.library_service import LibraryService


def main():
    # Create infrastructure
    library = Library("My local library")
    library_service = LibraryService(library)

    # Add books
    books_list = []
    with open("./data/books.json", "r") as file:
        books_list = json.load(file)

    for book in books_list:
        library.add_book(book=Book(book["title"], book["author"], book["isbn"]))

    # Register user
    user = Member("Leykun")
    user2 = Member("Bisrat")
    library.register_user(user)

    try:
        library_service.checkout_book(user, "To Kill a Mockingbird")
        library_service.checkout_book(user, "1984")
        print()
        for book in user.borrowed_books:
            print(book)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
