from datetime import date

library_books = {
    "978-3-16": {"title": "Clean Code", "is_available": False}
}

active_borrow_records = {
    "978-3-16": {"borrower_id": "STD001", "due_date": date(2026, 6, 30)}
}

DAILY_FINE_RATE = 500  # UGX charged per day overdue


def calculate_overdue_fine(due_date, actual_return_date):
    """Returns the fine amount based on how many days the book was overdue."""
    number_of_days_overdue = (actual_return_date - due_date).days

    if number_of_days_overdue <= 0:
        return 0

    return number_of_days_overdue * DAILY_FINE_RATE


def return_book(book_isbn, borrower_id):
    """Handles returning a book: checks the record, updates status, calculates fine."""

    borrow_record = active_borrow_records.get(book_isbn)

    if borrow_record is None or borrow_record["borrower_id"] != borrower_id:
        return "No matching borrow record found."

    return_date = date.today()
    due_date = borrow_record["due_date"]
    overdue_fine = calculate_overdue_fine(due_date, return_date)

    # Update book status back to available
    library_books[book_isbn]["is_available"] = True
    del active_borrow_records[book_isbn]

    if overdue_fine > 0:
        return f"Book returned. Overdue — Fine: UGX {overdue_fine}"
    return "Book returned successfully. No fine."


# Example usage
if __name__ == "__main__":
    result_message = return_book("978-3-16", "STD001")
    print(result_message)