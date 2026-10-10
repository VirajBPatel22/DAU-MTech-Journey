from business.rules import validate_book_data

class BookService:
    def __init__(self, repository):
        self.repository = repository

    def add_book(self, book_data):
        validate_book_data(book_data.title, book_data.author, book_data.isbn, book_data.publication_year, book_data.quantity)
        return self.repository.add(book_data)

    def get_all_books(self):
        return self.repository.get_all()

    def get_book(self, book_id):
        return self.repository.get_by_id(book_id)

    def search_books(self, title=None, author=None):
        return self.repository.search(title, author)

    def update_book(self, book_id, book_data):
        existing = self.repository.get_by_id(book_id)
        if existing is None:
            raise Exception("Book not found.")

        validate_book_data(book_data.title, book_data.author, book_data.isbn, book_data.publication_year, book_data.quantity)
        book_data.id = book_id
        return self.repository.update(book_data)

    def delete_book(self, book_id):
        existing = self.repository.get_by_id(book_id)
        if existing is None:
            raise Exception("Book not found.")
        return self.repository.delete(book_id)

    def checkout_book(self, book_id):
        book = self.repository.get_by_id(book_id)
        if book is None:
            raise Exception("Book not found.")
            
        if book.quantity <= 0:
            raise Exception("Cannot check out: Quantity is already 0.")

        book.quantity -= 1
        return self.repository.update(book)
