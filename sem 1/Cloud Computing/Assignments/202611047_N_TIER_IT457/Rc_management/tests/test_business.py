import pytest
from business.models import Book
from business.service import BookService
from business.rules import ValidationError, BusinessLogicError
from data.memory_repo import InMemoryBookRepository

@pytest.fixture
def service():
    repo = InMemoryBookRepository()
    return BookService(repo)

def test_add_valid_book(service):
    book = Book(title="Test", author="Author", isbn="1234567890", publication_year=2020, quantity=5)
    added = service.add_book(book)
    assert added.id == 1
    assert added.title == "Test"

def test_add_book_empty_title(service):
    book = Book(title="", author="Author", isbn="1234567890", publication_year=2020, quantity=5)
    with pytest.raises(ValidationError, match="Title cannot be empty"):
        service.add_book(book)

def test_add_book_future_year(service):
    book = Book(title="Test", author="Author", isbn="1234567890", publication_year=3000, quantity=5)
    with pytest.raises(ValidationError, match="Publication year cannot be in the future"):
        service.add_book(book)

def test_checkout_book_success(service):
    book = Book(title="Test", author="Author", isbn="1234567890", publication_year=2020, quantity=1)
    added = service.add_book(book)
    checked_out = service.checkout_book(added.id)
    assert checked_out.quantity == 0

def test_checkout_book_zero_quantity(service):
    book = Book(title="Test", author="Author", isbn="1234567890", publication_year=2020, quantity=0)
    added = service.add_book(book)
    with pytest.raises(BusinessLogicError, match="Cannot check out: Quantity is already 0"):
        service.checkout_book(added.id)
