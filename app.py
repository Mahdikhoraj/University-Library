from menus import*
from library import*
from book import*
from user import*
from search_engain import*



import time

def main()->None:
    print("Welcome to the University library")
    time.sleep(1)
    # menu = Mainmenu()
    # menu.show_menu()
    # choice = menu.get_choice()
    # print(choice)
    book1 = Book("Clean Code", "Robert C. Martin", 750000)
    book2 = Book("Python Crash Course", "Eric Matthes", 1200000)
    book3 = Book("front_end","sasani",1660000)
    print(book1)
    print(f" == : {book1 == book2}")
    print(f" grader then : {book1 < book2}")
    print(f" less than : {book1 > book2}")
    print(int(book2))
    
    user1 = User("mahdi")
    user2 = User("sara")
    
    user1.borrow(book1)
    user1.borrow(book2)
    user2.borrow(book3)
    
    print(f"borrow books:{len(user1)}")
    print(f"borrow books:{len(user2)}")
    
    print(f"Info User 1 : {user1.name}")
    print(f"Info User 1 : {user2.name}")
    
    user1.return_book(book1)
    print(f"borrow books:{len(user1)}")
    
    
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    book4 = Book("mahdi", "ali" , -122222)
    library.add_book(book4)
    library.show_list_book()
    
    
    search = SearchEngain(library)
    result = search("clean")
    print(result)
    
    
    all_books = library.books
    print(total_price(all_books))


    
    
    
if __name__ == "__main__":
    main()