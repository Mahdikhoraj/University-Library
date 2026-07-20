__all__ = [
    "Book",
]
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_info(self):

        return f"\nBook:{self.title}\n Author:{self.author}\n Price:{self.price}\n {"-" * 60}"

    def discount(self, percent):
        result = self.price * (percent / 100)
        self.price -= result

    def __str__(self):
        return self.show_info()

    def __repr__(self):
        return f"Book('{self.title}' , '{self.author}' , '{self.price}')"

    def __eq__(self, other):
        if self.title == other.title and self.author == other.author:
            return True
        return False

    def __lt__(self, other):
        if self.price < other.price:
            return True
        return False

    def __gt__(self, other):
        if self.price > other.price:
            return True
        return False

    def __int__(self):
        return self.price
