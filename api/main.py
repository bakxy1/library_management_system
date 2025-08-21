from flask import Flask, jsonify, g
from flask_cors import CORS

from db.connection import get_connection
from models.book import Book

app = Flask(__name__)
CORS(app)


def get_db():
    if "db" not in g:
        print("New connection")
        g.db = get_connection()
    else:
        print("Old connection")
    return g.db


@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop("db", None)

    if db is not None:
        db.close()


@app.route("/books", methods=["GET"])
def get_all_books():
    db = get_db()
    query = "select * from books"
    cursor = db.cursor(dictionary=True)
    cursor.execute(query)
    books_data = cursor.fetchall()

    return jsonify(books_data)
