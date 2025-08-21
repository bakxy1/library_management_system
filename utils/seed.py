# create books table
# Populate it with books data
from mysql.connector import Connect, Error
from db.connection import get_connection
import json
from uuid import uuid4

from models.book import Book

conn = get_connection()
cursor = conn.cursor()


def create_books_table():
    try:
        query = """
        CREATE TABLE IF NOT EXISTS books (
            id VARCHAR(36) PRIMARY KEY,
            isbn VARCHAR(20) NOT NULL,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            genre VARCHAR(100),
            publisher VARCHAR(255),
            year INT,
            copies INT NOT NULL,
            available INT NOT NULL,
            status VARCHAR(50)
        );
        """
        cursor.execute(query)
    except Error as e:
        print(e)
    pass


def populate_books_table():
    with open("./data/books.json", "r") as file:
        books_data = json.load(file)
        books = [Book(**book) for book in books_data]

        for book in books:
            query = """
            INSERT INTO books (
                id, isbn, title, author, genre, publisher, year, copies, available, status
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            );
            """
            cursor.execute(
                query,
                (
                    book.id,
                    book.isbn,
                    book.title,
                    book.author,
                    book.genre,
                    book.publisher,
                    book.year,
                    book.copies,
                    book.available,
                    book.status,
                ),
            )
            conn.commit()
    pass


if __name__ == "__main__":
    create_books_table()
    populate_books_table()
