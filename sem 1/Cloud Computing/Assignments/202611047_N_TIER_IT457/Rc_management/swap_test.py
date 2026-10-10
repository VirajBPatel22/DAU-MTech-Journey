from business.models import Book
from business.service import BookService
from data.sqlite_repo import SQLiteBookRepository
from data.memory_repo import InMemoryBookRepository

def test_my_service(service_name, service_object):
    print("Testing:", service_name)
    
    # 1. Create a book
    new_book = Book(title="Swap Test Book", author="John Doe", isbn="1234567890", publication_year=2023, quantity=2)
    
    # 2. Add book
    saved_book = service_object.add_book(new_book)
    print("Added book ID:", saved_book.id)
    
    # 3. Check out
    service_object.checkout_book(saved_book.id)
    updated_book = service_object.get_book(saved_book.id)
    print("Quantity after checkout:", updated_book.quantity)
    
    print("-" * 30)

if __name__ == "__main__":
    
    # Use SQLite database
    sqlite_db = SQLiteBookRepository("test_swap.db")
    sqlite_service = BookService(sqlite_db)
    
    # Use Python Dictionary memory database
    memory_db = InMemoryBookRepository()
    memory_service = BookService(memory_db)

    # Test both to show they work exactly the same!
    test_my_service("Memory Dictionary Database", memory_service)
    test_my_service("SQLite Database", sqlite_service)
