from flask import Flask, request, jsonify

app = Flask(__name__)

# Examples of books
books = [
    {"id": 1, "book_name": "The Little Seagull", 
     "authors": "Richard Bullock, Michal Brody, Francine Weinberg", 
     "publisher": "W. W. Norton & Company"},
    {"id": 2, "book_name": "My Antonia", 
     "author": "Willa Cather", 
     "publisher": "Houghton Mifflin"}
]

# Read all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Read a specific book
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = [book for book in books if book["id"] == id]
    return jsonify(book)

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    book = {
        "id": len(books) + 1,
        "book_name": request.json["book_name"],
        "author": request.json["author"],
        "publisher": request.json["publisher"]
    }
    books.append(book)
    return jsonify(book)

# Update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = [book for book in books if book["id"] == id]
    book[0]["book_name"] = request.json.get("book_name", book[0]["book_name"])
    book[0]["author"] = request.json.get("author", book[0]["author"])
    book[0]["publisher"] = request.json.get("publisher", book[0]["publisher"])
    return jsonify(book[0])

# Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = [book for book in books if book["id"] == id]
    books.remove(book[0])
    return jsonify({"result":"Book deleted"})

if __name__ == '__main__':
    app.run(debug=True)