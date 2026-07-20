__all__=[
    "User"
]
class User():
    def __init__(self,name):
        self.name = name
        self.borrowed_books = list()
        
    def borrow(self,book):
        if not book in self.borrowed_books:
            self.borrowed_books.append(book)
            
    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            
    def __len__(self):
        return len(self.borrowed_books)
    
    def __str__(self):
        return f"Name:{self.name}\n Book:{self.borrowed_books}"
    
    def __repr__(self):
        return f"User('{self.name}' , '{self.borrowed_books}')"