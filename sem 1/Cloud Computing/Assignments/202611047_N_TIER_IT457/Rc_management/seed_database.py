from business.models import Book
from business.service import BookService
from data.sqlite_repo import SQLiteBookRepository

def seed_initial_data():
    # Connect to the live database
    my_database = SQLiteBookRepository("library_prod.db")
    my_service = BookService(my_database)

    # List of classic books to populate the library for demonstration
    books_to_add = [
        Book(title="The Great Gatsby", author="F. Scott Fitzgerald", isbn="9780743273565", publication_year=1925, quantity=5),
        Book(title="To Kill a Mockingbird", author="Harper Lee", isbn="9780060935467", publication_year=1960, quantity=3),
        Book(title="1984", author="George Orwell", isbn="9780451524935", publication_year=1949, quantity=8),
        Book(title="Pride and Prejudice", author="Jane Austen", isbn="9780141439518", publication_year=1813, quantity=4),
        Book(title="The Catcher in the Rye", author="J.D. Salinger", isbn="9780316769488", publication_year=1951, quantity=6),
        Book(title="The Hobbit", author="J.R.R. Tolkien", isbn="9780345339683", publication_year=1937, quantity=12),
        Book(title="Fahrenheit 451", author="Ray Bradbury", isbn="9781451673319", publication_year=1953, quantity=2),
        Book(title="The Story of My Experiments with Truth", author="Mahatma Gandhi", isbn="9780807059098", publication_year=1927, quantity=10),
        Book(title="The Alchemist", author="Paulo Coelho", isbn="9780061122415", publication_year=1988, quantity=15),
        Book(title="Sapiens: A Brief History of Humankind", author="Yuval Noah Harari", isbn="9780062316097", publication_year=2011, quantity=7),
        Book(title="Thinking, Fast and Slow", author="Daniel Kahneman", isbn="9780374533557", publication_year=2011, quantity=5),
        Book(title="To the Lighthouse", author="Virginia Woolf", isbn="9780156907392", publication_year=1927, quantity=4),
        Book(title="Moby-Dick", author="Herman Melville", isbn="9781503280786", publication_year=1851, quantity=3),
        Book(title="Brave New World", author="Aldous Huxley", isbn="9780060850524", publication_year=1932, quantity=8),
        Book(title="The Lord of the Rings", author="J.R.R. Tolkien", isbn="9780544003415", publication_year=1954, quantity=6),
        Book(title="Crime and Punishment", author="Fyodor Dostoevsky", isbn="9780486415871", publication_year=1866, quantity=4),
        Book(title="The Diary of a Young Girl", author="Anne Frank", isbn="9780553296983", publication_year=1947, quantity=9)
    ]

    print("Adding books to the database...")
    for book in books_to_add:
        try:
            my_service.add_book(book)
            print(f"Success: Added '{book.title}'")
        except Exception as e:
            print(f"Skipped '{book.title}' - It might already exist. (Error: {e})")
            
    print("Database seeding completed!")

if __name__ == "__main__":
    seed_initial_data()
