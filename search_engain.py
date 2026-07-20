__all__ = [
    "SearchEngain",
    "total_price",
]


class SearchEngain:
    def __init__(self, library):
        self.library = library

    def __call__(self, Keyboard):
        result = []
        Keyboard = Keyboard.lower()
        for book in self.library.books:
            if Keyboard in book.title.lower():
                result.append(book)
        else :
            print("not found")
        return result


def total_price(books):
    result = 0
    for book in books:
        price = int(book)
        result += price
    return result
