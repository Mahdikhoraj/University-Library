__all__ = [
    "Library",
]
class Library:

    def __init__(self):
        self.library = []

    def add_book(self, title, author, price):
        if int(price) < 0:
            print("Price cannot be negative.")
            return

        self.library.extend([title, author, price])
        print("Book added.")

    def remove_book(self, title):
        if title in self.library:
            index = self.library.index(title)
            del self.library[index : index + 3]
            print("Book removed.")
        else:
            print("Book not found.")

    def show_list_library(self):
        for book in range(0, len(self.library), 3):
            print(f"Book  : {self.library[book]}")
            print(f"Author: {self.library[book + 1]}")
            print(f"Cost  : {self.library[book + 2]}")
            print("-" * 20)

# lib = Library()
# lib.add_book("mmd", "nas", "1234")
# lib.add_book("mmd", "nas", "1234")
# lib.show_list_library()
# lib.remove_book("mmd")
# lib.add_book("ali", "nas", "-1234")
# lib.show_list_library()
# print(lib.library)


