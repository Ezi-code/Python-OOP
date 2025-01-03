# library management system


class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.is_available = is_available

    def __str__(self):
        return f"{self.author}, {self.title} {self.is_available}"

    def mark_borrowed(self, patron=None):
        self.is_available = False
        return f"Borrowed {patron.name}"

    def mark_returned(self, patron=None):
        self.is_available = True
        return f"Returned by {patron.name}"


class Patron:

    def __init__(self, name: str, id: int, borrowed_books: list = []):
        self.name = name
        self.id = id
        self.borrowed_books: list = borrowed_books

    def __str__(self):
        return f"{self.name}, borrowed books:{self.borrowed_books}"

    def process_borrow(self, book=None):
        self.borrowed_books.append(book)
        book.is_available = False
        return f"book {book.title} borrowed by {self.name}"

    def process_return(self, return_book=None):
        if self.borrowed_books:
            for book in self.borrowed_books:
                if book == return_book:
                    self.borrowed_books.remove(book)
                    book.is_available = True
                    return "Book returned"
        return "No borrowed books found"


class Library:
    """Library object."""

    books = []

    def __str__(self):
        """str method."""
        return "Library Object"

    def create_books(self, title, isbn, author, is_available=True):
        """create book method."""
        book = Book(is_available, isbn, title, author)
        return book

    def create_patrons(self, name, id, borrowed_books: list = []):
        """create patron method."""
        patron = Patron(name, id, borrowed_books)
        return patron

    def borrow_book(self, patron, book):
        """borrow book method."""
        return Patron.process_borrow(patron, book)

    def return_book(self, patron, book):
        """return book method."""
        return Patron.process_return(patron, book)

    def search_book(self, indexed):
        """search for a book method."""
        return indexed if indexed in books else "Book not found"


if __name__ == "__main__":

    books = Library.books

    books.append(
        Book(title="new book", isbn="1232433", author="Pope", is_available=False)
    )
    books.append(Book(title="another book", isbn="1232433", author="Ezi"))

    book4 = Book(title="Last book", isbn="1232433", author="Aaa")
    book1 = books[0]
    book2 = books[1]

    patron = Patron(name="new patron", id="212121")
    patron.process_borrow(book1)
    patron.process_return(book1)

    lib = Library()
