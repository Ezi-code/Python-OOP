# library management system


class Book:
    """Book object."""

    def __init__(self, title, author, isbn, is_available=True):
        """book object init method."""
        self.title = title
        self.isbn = isbn
        self.author = author
        self.is_available = is_available

    def __str__(self):
        """book object string method."""
        return f"{self.title}, {self.author} {self.is_available}"

    def mark_borrowed(self, patron=None):
        """mark book as borrowed."""
        if patron:
            self.is_available = False
            return f"Borrowed {patron.name}"
        return "Borrowed"

    def mark_returned(self, patron=None):
        """mark book as returned."""
        if patron:
            self.is_available = True
            return f"Returned by {patron.name}"
        return "Returned"


class Patron:

    def __init__(self, name: str, id: int, borrowed_books: list = []):
        """patron object init method."""
        self.name = name
        self.id = id
        self.borrowed_books: list = borrowed_books

    def __str__(self):
        """patron object string method."""
        return f"{self.name}, borrowed books:{self.borrowed_books}"

    def process_borrow(self, book=None):
        """process borrowed book."""
        self.borrowed_books.append(book)
        book.is_available = False
        return f"book {book.title} borrowed by {self.name}"

    def process_return(self, return_book=None):
        """process returned book."""
        if self.borrowed_books:
            for book in self.borrowed_books:
                if book == return_book:
                    self.borrowed_books.remove(book)
                    book.is_available = True
                    return "Book returned"
            return "book not found in borrowed books"
        return "No borrowed books found"


class Library:
    """Library object."""

    def __init__(self):
        self.books = []
        self.patrons = []

    def __str__(self):
        """str method."""
        return "Library Object"

    def create_books(self, title, isbn, author, is_available=True):
        """create book method."""
        book = Book(
            title=title,
            author=author,
            isbn=isbn,
            is_available=is_available,
        )
        self.books.append(book)
        return book

    def create_patrons(self, name, id, borrowed_books: list = []):
        """create patron method."""
        patron = Patron(name=name, id=id, borrowed_books=borrowed_books)
        self.patrons.append(patron)
        return patron

    def borrow_book(self, patron_id, book):
        """borrow book method."""
        patron = next((p for p in self.patrons if p.id==patron_id), None)
        book = next((b for b in self.books if b.title=book), None)

        if not patron:
            return "Patron not found."
        
        if not book:
            return "Book not found."
        
        patron.process_borrow(book)

    def return_book(self, patron_id, book):
        """return book method."""

        patron = next((p for p in self.patrons if p.id == patron_id), None)
        book = next((b for b in self.books if b.title == book), None)

        if not book:
            return "Book not found"

        if not patron:
            return "Patron not found"

        return patron.process_return(book)

    def search_book(self, query) -> str:
        """search for a book method."""
        for book in self.books:
            if (
                query.lower() == book.title
                or query.lower() == book.author
                or query.lower == book.isbn
            ):
                return f"Book found: {book}"
        return "book not found!"

    def list_patrons(self) -> None:
        """list all patrons."""
        for patron in self.patrons:
            print(f" - {patron}")

    def list_books(self) -> None:
        """list all books."""
        for book in self.books:
            print(book)


if __name__ == "__main__":
    lib = Library()

    b = lib.create_books(title="title", isbn="1234", author="Pope")
    p = lib.create_patrons("Pope", 12312)
    lib.borrow_book(patron=p, book=b)
    print(lib.list_books())
