books = []

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. List Books")
    print("6. Library Statistics")
    print("7. Exit")

    c = input("Choice: ")

    if c == "1":

        t = input("Book title: ")
        a = input("Author: ")
        y = int(input("Year: "))
        i = input("Book ID: ")

        x = False

        for b in books:
            if b["id"] == i:
                x = True

        if x:
            print("Book ID already exists.")
        else:
            books.append({
                "title": t,
                "author": a,
                "year": y,
                "id": i,
                "borrowed": False,
                "borrower": ""
            })
            print("Book added.")

    elif c == "2":

        i = input("Enter Book ID: ")

        found = False

        for b in books:

            if b["id"] == i:

                found = True

                if b["borrowed"] == True:
                    print("Book already borrowed.")

                else:
                    name = input("Borrower name: ")

                    b["borrowed"] = True
                    b["borrower"] = name

                    print("Book borrowed successfully.")

        if found == False:
            print("Book not found.")

    elif c == "3":

        i = input("Enter Book ID: ")

        found = False

        for b in books:

            if b["id"] == i:

                found = True

                if b["borrowed"] == False:
                    print("Book is already available.")

                else:

                    b["borrowed"] = False
                    b["borrower"] = ""

                    print("Book returned.")

        if found == False:
            print("Book not found.")

    elif c == "4":

        s = input("Search title: ")

        found = False

        for b in books:

            if s.lower() in b["title"].lower():

                found = True

                print("-------------------------")
                print("Title:", b["title"])
                print("Author:", b["author"])
                print("Year:", b["year"])
                print("ID:", b["id"])

                if b["borrowed"]:
                    print("Status: Borrowed")
                    print("Borrower:", b["borrower"])
                else:
                    print("Status: Available")

                print("-------------------------")

        if found == False:
            print("Nothing found.")

    elif c == "5":

        if len(books) == 0:
            print("No books.")

        else:

            for b in books:

                print("-----------------------")
                print("Title:", b["title"])
                print("Author:", b["author"])
                print("Year:", b["year"])
                print("ID:", b["id"])

                if b["borrowed"]:
                    print("Status: Borrowed")
                    print("Borrower:", b["borrower"])
                else:
                    print("Status: Available")

                print("-----------------------")

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

            if oldest == None:
                oldest = b

            if newest == None:
                newest = b

            if b["year"] < oldest["year"]:
                oldest = b

            if b["year"] > newest["year"]:
                newest = b

        print("\nLibrary Statistics")
        print("-------------------------")
        print("Total books:", total)
        print("Borrowed:", borrowed)
        print("Available:", available)

        if total > 0:
            print("Oldest book:", oldest["title"], oldest["year"])
            print("Newest book:", newest["title"], newest["year"])

    elif c == "7":
        print("Goodbye")
        break

    else:
        print("Invalid choice")