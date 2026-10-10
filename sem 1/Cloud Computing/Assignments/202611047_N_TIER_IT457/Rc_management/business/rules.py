import datetime

def validate_book_data(title, author, isbn, year, quantity):
    if title == "" or title is None:
        raise Exception("Title cannot be empty.")
    
    if author == "" or author is None:
        raise Exception("Author cannot be empty.")
    
    current_year = datetime.datetime.now().year
    if year > current_year:
        raise Exception("Publication year cannot be in the future.")
    
    if len(isbn) != 10 and len(isbn) != 13:
        raise Exception("ISBN must be exactly 10 or 13 digits.")
        
    if not isbn.isdigit():
        raise Exception("ISBN must contain only numbers.")
        
    if quantity < 0:
        raise Exception("Quantity cannot be negative.")
