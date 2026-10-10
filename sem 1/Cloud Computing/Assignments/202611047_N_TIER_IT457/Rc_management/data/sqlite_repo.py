import sqlite3
from business.interfaces import BookRepository
from business.models import Book

class SQLiteBookRepository(BookRepository):
    def __init__(self, db_path="library.db"):
        self.db_path = db_path
        
        # Setup database table
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                isbn TEXT,
                publication_year INTEGER,
                quantity INTEGER
            )
        ''')
        conn.commit()
        conn.close()

    def _convert_to_book(self, row):
        if row is None:
            return None
        return Book(
            id=row[0],
            title=row[1],
            author=row[2],
            isbn=row[3],
            publication_year=row[4],
            quantity=row[5]
        )

    def add(self, book):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO books (title, author, isbn, publication_year, quantity)
            VALUES (?, ?, ?, ?, ?)
        ''', (book.title, book.author, book.isbn, book.publication_year, book.quantity))
        conn.commit()
        book.id = cursor.lastrowid
        conn.close()
        return book

    def get_all(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()
        conn.close()
        
        books = []
        for row in rows:
            books.append(self._convert_to_book(row))
        return books

    def get_by_id(self, book_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
        row = cursor.fetchone()
        conn.close()
        return self._convert_to_book(row)

    def search(self, title=None, author=None):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if title:
            search_term = "%" + title + "%"
            cursor.execute('SELECT * FROM books WHERE title LIKE ?', (search_term,))
        elif author:
            search_term = "%" + author + "%"
            cursor.execute('SELECT * FROM books WHERE author LIKE ?', (search_term,))
        else:
            cursor.execute('SELECT * FROM books')
            
        rows = cursor.fetchall()
        conn.close()
        
        books = []
        for row in rows:
            books.append(self._convert_to_book(row))
        return books

    def update(self, book):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE books
            SET title = ?, author = ?, isbn = ?, publication_year = ?, quantity = ?
            WHERE id = ?
        ''', (book.title, book.author, book.isbn, book.publication_year, book.quantity, book.id))
        conn.commit()
        conn.close()
        return book

    def delete(self, book_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        deleted_count = cursor.rowcount
        conn.commit()
        conn.close()
        
        if deleted_count > 0:
            return True
        else:
            return False
