"""
Library statistics module.
Provides functions to compute and display various statistics.
"""

from typing import List, Dict, Optional
from models import Book   # We'll define Book in library.py or separate, but for simplicity we can reuse dict
# To avoid circular import, we'll pass books as dict or use a protocol. We'll use dict.
# Actually we'll keep using dict for compatibility.

def compute_statistics(books: Dict[str, dict]) -> dict:
    """
    Compute statistics from a dictionary of books (id -> book data).
    Returns a dict with keys: total, borrowed, available, oldest, newest,
    most_borrowed, avg_year, borrowed_list.
    """
    total = len(books)
    if total == 0:
        return {
            "total": 0,
            "borrowed": 0,
            "available": 0,
            "oldest": None,
            "newest": None,
            "most_borrowed": None,
            "avg_year": 0,
            "borrowed_list": []
        }

    borrowed = 0
    available = 0
    total_years = 0
    max_borrow = -1
    most_borrowed_book = None
    borrowed_titles = []

    for book in books.values():
        if book["borrowed"]:
            borrowed += 1
            borrowed_titles.append(book["title"])
        else:
            available += 1

        total_years += book["year"]

        # Track most borrowed (borrow_count must exist)
        count = book.get("borrow_count", 0)
        if count > max_borrow:
            max_borrow = count
            most_borrowed_book = book

    oldest = min(books.values(), key=lambda b: b["year"])
    newest = max(books.values(), key=lambda b: b["year"])

    return {
        "total": total,
        "borrowed": borrowed,
        "available": available,
        "oldest": oldest,
        "newest": newest,
        "most_borrowed": most_borrowed_book,
        "avg_year": total_years / total,
        "borrowed_list": borrowed_titles
    }


def display_statistics(stats: dict) -> None:
    """Print the statistics in a formatted way."""
    print("\nLibrary Statistics")
    print("-------------------------")
    print(f"Total books: {stats['total']}")
    print(f"Borrowed: {stats['borrowed']}")
    print(f"Available: {stats['available']}")

    if stats['total'] > 0:
        print(f"Oldest book: {stats['oldest']['title']} ({stats['oldest']['year']})")
        print(f"Newest book: {stats['newest']['title']} ({stats['newest']['year']})")
        print(f"Average publication year: {stats['avg_year']:.1f}")

        if stats['most_borrowed']:
            most = stats['most_borrowed']
            print(f"Most borrowed book: {most['title']} (borrowed {most.get('borrow_count', 0)} times)")

        if stats['borrowed_list']:
            print("Currently borrowed books:")
            for title in stats['borrowed_list']:
                print(f"  - {title}")
        else:
            print("No books currently borrowed.")
    print("-------------------------")