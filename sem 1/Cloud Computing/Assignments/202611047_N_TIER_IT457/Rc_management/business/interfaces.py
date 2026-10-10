from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Book

class BookRepository(ABC):
    @abstractmethod
    def add(self, book: Book) -> Book: pass
    @abstractmethod
    def get_all(self) -> List[Book]: pass
    @abstractmethod
    def get_by_id(self, book_id: int) -> Optional[Book]: pass
    @abstractmethod
    def search(self, query: str = None, title: str = None, author: str = None) -> List[Book]: pass
    @abstractmethod
    def update(self, book: Book) -> Book: pass
    @abstractmethod
    def delete(self, book_id: int) -> bool: pass
