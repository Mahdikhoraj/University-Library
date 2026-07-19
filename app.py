from menus import*
from library import*
import time

def main()->None:
    print("Welcome to the University library")
    time.sleep(1)
    # menu = Mainmenu()
    # menu.show_menu()
    # choice = menu.get_choice()
    # print(choice)
    lib = Library()
    lib.add_book("Clean Code", "Robert C. Martin", "850")
    lib.add_book("Python Crash Course", "Eric Matthes", "1200")
    lib.add_book("The Pragmatic Programmer", "Andrew Hunt", "1500")
    lib.remove_book("Clean Code")
    lib.add_book("ali", "nas", "1234")
    lib.update_price("ali","1387")
    lib.show_books()
    
    book1 = lib.find_book("The Pragmatic Programmer")
    book2  = lib.find_book("Python Crash Course")
    print(book1 == book2)
    print(int(book1))
    print(len(book1))
    
if __name__ == "__main__":
    main()