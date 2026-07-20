from book import Book
from valid import Validations

__all__ = [
    "Library",
]


class Library:
    def __init__(self):
        self.books = list()

    def add_book(self, book):
        if Validations.is_valid_price(book.price):
            self.books.append(book)
        else:
            print("The price cant be negetive or etc")

    def remove_book(self, book):
        if self.is_valid_price(book):
            self.books.remove(book)

    def show_list_book(self):
        for book in self.books:
            print(book)
