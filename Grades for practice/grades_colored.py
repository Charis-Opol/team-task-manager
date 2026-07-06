import sys

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"


def color_print(message, color=WHITE):
    print(f"{color}{message}{RESET}")


def color_input(prompt, color=CYAN):
    return input(f"{color}{prompt}{RESET}")


books = []

while True:
    color_print("\n===== LIBRARY MANAGEMENT =====", BOLD + CYAN)
    color_print("1. Add Book", GREEN)
    color_print("2. Borrow Book", YELLOW)
    color_print("3. Return Book", BLUE)
    color_print("4. Search Book", MAGENTA)
    color_print("5. List Books", CYAN)
    color_print("6. Library Statistics", WHITE)
    color_print("7. Exit", RED)

    c = color_input("Choice: ", YELLOW)

    if c == "1":
        t = color_input("Book title: ", CYAN)
        a = color_input("Author: ", CYAN)
        y = int(color_input("Year: ", CYAN))
        i = color_input("Book ID: ", CYAN)

        x = False
        for b in books:
            if b["id"] == i:
                x = True

        if x:
            color_print("Book ID already exists.", RED)
        else:
            books.append({
                "title": t,
                "author": a,
                "year": y,
                "id": i,
                "borrowed": False,
                "borrower": ""
            })
            color_print("Book added.", GREEN)

    elif c == "2":
        i = color_input("Enter Book ID: ", CYAN)
        found = False

        for b in books:
            if b["id"] == i:
                found = True
                if b["borrowed"]:
                    color_print("Book already borrowed.", RED)
                else:
                    name = color_input("Borrower name: ", CYAN)
                    b["borrowed"] = True
                    b["borrower"] = name
                    color_print("Book borrowed successfully.", GREEN)

        if not found:
            color_print("Book not found.", RED)

    elif c == "3":
        i = color_input("Enter Book ID: ", CYAN)
        found = False

        for b in books:
            if b["id"] == i:
                found = True
                if not b["borrowed"]:
                    color_print("Book is already available.", YELLOW)
                else:
                    b["borrowed"] = False
                    b["borrower"] = ""
                    color_print("Book returned.", GREEN)

        if not found:
            color_print("Book not found.", RED)

    elif c == "4":
        s = color_input("Search title: ", CYAN)
        found = False

        for b in books:
            if s.lower() in b["title"].lower():
                found = True
                color_print("\n-------------------------", MAGENTA)
                color_print(f"Title: {b['title']}", WHITE)
                color_print(f"Author: {b['author']}", WHITE)
                color_print(f"Year: {b['year']}", WHITE)
                color_print(f"ID: {b['id']}", WHITE)

                if b["borrowed"]:
                    color_print("Status: Borrowed", RED)
                    color_print(f"Borrower: {b['borrower']}", YELLOW)
                else:
                    color_print("Status: Available", GREEN)

                color_print("-------------------------", MAGENTA)

        if not found:
            color_print("Nothing found.", RED)

    elif c == "5":
        if len(books) == 0:
            color_print("No books.", YELLOW)
        else:
            for b in books:
                color_print("\n-----------------------", CYAN)
                color_print(f"Title: {b['title']}", WHITE)
                color_print(f"Author: {b['author']}", WHITE)
                color_print(f"Year: {b['year']}", WHITE)
                color_print(f"ID: {b['id']}", WHITE)

                if b["borrowed"]:
                    color_print("Status: Borrowed", RED)
                    color_print(f"Borrower: {b['borrower']}", YELLOW)
                else:
                    color_print("Status: Available", GREEN)

                color_print("-----------------------", CYAN)

    elif c == "6":
        total = len(books)
        borrowed = 0
        available = 0
        oldest = None
        newest = None

        for b in books:
            if b["borrowed"]:
                borrowed += 1
            else:
                available += 1

            if oldest is None or b["year"] < oldest["year"]:
                oldest = b

            if newest is None or b["year"] > newest["year"]:
                newest = b

        color_print("\nLibrary Statistics", BOLD + MAGENTA)
        color_print("-------------------------", MAGENTA)
        color_print(f"Total books: {total}", WHITE)
        color_print(f"Borrowed: {borrowed}", RED)
        color_print(f"Available: {available}", GREEN)

        if total > 0:
            color_print(f"Oldest book: {oldest['title']} ({oldest['year']})", YELLOW)
            color_print(f"Newest book: {newest['title']} ({newest['year']})", CYAN)

    elif c == "7":
        color_print("Goodbye", BOLD + RED)
        break

    else:
        color_print("Invalid choice", RED)
