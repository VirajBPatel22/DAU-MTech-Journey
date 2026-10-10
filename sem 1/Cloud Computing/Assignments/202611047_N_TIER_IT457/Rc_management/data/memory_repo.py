from business.interfaces import BookRepository

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books_dictionary = {}
        self.next_id = 1

    def add(self, book):
        book.id = self.next_id
        self.books_dictionary[self.next_id] = book
        self.next_id += 1
        return book

    def get_all(self):
        return list(self.books_dictionary.values())

    def get_by_id(self, book_id):
        if book_id in self.books_dictionary:
            return self.books_dictionary[book_id]
        return None

    def search(self, title=None, author=None):
        results = []
        for book in self.books_dictionary.values():
            if title and title.lower() in book.title.lower():
                results.append(book)
            elif author and author.lower() in book.author.lower():
                results.append(book)
            elif not title and not author:
                results.append(book)
        return results

    def update(self, book):
        self.books_dictionary[book.id] = book
        return book

    def delete(self, book_id):
        if book_id in self.books_dictionary:
            del self.books_dictionary[book_id]
            return True
        return False
