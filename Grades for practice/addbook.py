"""
add_book.py

Handles adding a new book to the library collection.
"""


def is_duplicate_id(books, book_id):
    """Check if a book with the given ID already exists."""
    return any(book["id"] == book_id for book in books)


def get_valid_year(prompt="Year: "):
    """
    Keep asking until the user provides a valid integer year.
    Prevents the program from crashing on bad input (e.g. letters).
    """
    while True:
        year_input = input(prompt)
        try:
            return int(year_input)
        except ValueError:
            print("Invalid year. Please enter a number (e.g. 2020).")


def get_non_empty_input(prompt):
    """Keep asking until the user provides a non-blank string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def add_book(books):
    """
    Prompt the user for book details and add a new book to the list,
    if the ID doesn't already exist.

    Args:
        books (list): the shared list of book dictionaries.
    """
    title = get_non_empty_input("Book title: ")
    author = get_non_empty_input("Author: ")
    year = get_valid_year("Year: ")
    book_id = get_non_empty_input("Book ID: ")

    if is_duplicate_id(books, book_id):
        print(f"Book ID '{book_id}' already exists. Book not added.")
        return

    books.append({
        "title": title,
        "author": author,
        "yea

    print(f"Book '{title}' added successfully.")