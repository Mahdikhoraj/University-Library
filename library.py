from book import Book
__all__ = [
    "Library",
]
class Library:

    def __init__(self):
        self.library = []

    def add_book(self, title, auther, price):
        if int(price) < 0:
            print("Price cannot be negative.")
            return
        book = Book(title,auther,price)
        self.library.append(book)
        print("Book added")
    def remove_book(self, title):
            for book in self.library:
                if book.title == title:
                    self.library.remove(book)
                    print("Book removed.")
                    return

            print("Book not found.")

    def show_books(self):
        print("-" * 20)
        for book in self.library:
            book.show_info()
            print("-" * 20)
            
            
    def update_price(self,title,new_price):
        for book in self.library:
            if book.title == title:
                book.change_price(new_price)
                return
        else:
            print("book not found")
            
    def find_book(self,title):
        for book in self.library:
            if book.title ==title:
                return book
        return None
        

# lib = Library()

# lib.add_book("mmd", "nas", "1234")
# lib.add_book("mmd", "nas", "1234")
# lib.add_book("mmd", "nas", "1234")
# lib.remove_book("mmd")

# lib.show_books()


