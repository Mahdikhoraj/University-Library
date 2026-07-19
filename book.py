class Book():
    def __init__(self,book_title,auther,price):
        self.title = book_title
        self.auther  = auther
        self.price = int(price)
        
    def show_info(self):
        print(f"Book : {self.title}")
        print(f"auther : {self.auther}")
        print(f"price : {self.price}")
        
        
    def change_price(self,price):
        self.price = int(price)
        
        
    def __int__(self):
        return self.price
    
    def __len__(self):
        return len( self.title)