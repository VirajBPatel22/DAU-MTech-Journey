from fastapi import APIRouter, HTTPException
from business.models import Book
from business.service import BookService
from data.sqlite_repo import SQLiteBookRepository

router = APIRouter()

# Simple setup
my_database = SQLiteBookRepository("library_prod.db")
my_service = BookService(my_database)

@router.post("/books")
def add_book(book: Book):
    try:
        return my_service.add_book(book)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/books")
def get_books(title: str = None, author: str = None):
    return my_service.search_books(title=title, author=author)

@router.get("/books/{book_id}")
def get_book(book_id: int):
    book = my_service.get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    try:
        return my_service.update_book(book_id, book)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    try:
        my_service.delete_book(book_id)
        return {"message": "Book deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/books/{book_id}/checkout")
def checkout_book(book_id: int):
    try:
        return my_service.checkout_book(book_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
