from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    isbn: str
    publication_year: int
    quantity: int
