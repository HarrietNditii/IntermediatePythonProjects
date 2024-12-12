class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked out"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = set()

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book
        print(f"Book added: {book}")

    def add_member(self, member):
        self.members[member.member_id] = member
        print(f"Member added: {member}")

    def borrow_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member:
            print(f"No member found with ID {member_id}")
            return

        if not book:
            print(f"No book found with ISBN {isbn}")
            return

        if not book.is_available:
            print(f"Book is already checked out: {book}")
            return

        book.is_available = False
        member.borrowed_books.add(book.isbn)
        print(f"{member.name} has borrowed {book.title}")

    def return_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member or isbn not in member.borrowed_books:
            print(f"No record of {isbn} being borrowed by {member_id}")
            return

        book.is_available = True
        member.borrowed_books.remove(isbn)
        print(f"{member.name} has returned {book.title}")

    def list_books(self):
        print("Books in the library:")
        for book in self.books.values():
            print(book)

    def list_members(self):
        print("Library members:")
        for member in self.members.values():
            print(member)


# Example Usage
if __name__ == "__main__":
    library = Library()

    # Add books
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    library.add_book(book1)
    library.add_book(book2)

    # Add members
    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")
    library.add_member(member1)
    library.add_member(member2)

    # Borrow and return books
    library.borrow_book("M001", "1234567890")
    library.borrow_book("M002", "1234567890")  # Should show it's already checked out
    library.return_book("M001", "1234567890")
    library.borrow_book("M002", "1234567890")

    # List books and members
    library.list_books()
    library.list_members()
