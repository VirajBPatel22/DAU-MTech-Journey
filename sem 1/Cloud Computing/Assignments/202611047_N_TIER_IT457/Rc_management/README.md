# Library Management System

This is my project for building a 3-tier Library Management application. I used Python, FastAPI, and SQLite to create this.

## Folder Structure
I separated my code into three main folders to follow the 3-tier architecture rules:

* **presentation**: This folder handles the web side of things. I used FastAPI to create the routes, and I also added a simple HTML dashboard (in the static folder) so you can easily add, search, edit, and delete books from a web browser.
* **business**: This is where all the logic lives. The `rules.py` file checks things like making sure the ISBN is exactly 10 or 13 digits and that you can't have negative quantities. The `service.py` file connects the web routes to these rules.
* **data**: This folder handles saving data. I made two versions: one that saves to a real SQLite database (`sqlite_repo.py`), and one that just saves to a simple Python dictionary (`memory_repo.py`) which I use for testing.

## Design Decision
For my design decision, I decided to create a base class called `BookRepository` inside the business folder, which both of my database files inherit from. I chose to do this because the assignment asked us to prove that we can swap out a data source without changing the business logic. 

By having this base class, my `BookService` doesn't care if it's talking to SQLite or a dictionary. As long as the database has functions like `add()` and `get_all()`, it works perfectly. You can run my `swap_test.py` file to see this in action—it runs the exact same book logic on both databases successfully!

## How to Run the Project

1. Open your terminal in this folder and set up the environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Start the web server:
   ```bash
   uvicorn main:app --reload
   ```
   
3. Open your browser and go to `http://localhost:8000/` to use the Library Dashboard.

## How to Run the Tests

To run the 5 unit tests for the business rules (these tests use the fake dictionary database so they don't mess up the real one):
```bash
pytest tests/
```

To run the swap test script:
```bash
python3 swap_test.py
```
