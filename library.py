class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f"Book '{book}' added to library")
        else:
            print("Book already exists in library")

    def get_books(self):
        for book in self.books:
            print(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed from library")
        else:
            print("Book not found in library")

library = Library()
library.add_book("The Great Gatsby")
library.add_book("To Kill a Mockingbird")
library.add_book("Pride and Prejudice")
library.get_books()
library.remove_book("The Great Gatsby")
library.get_books()