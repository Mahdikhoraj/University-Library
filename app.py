from menus import*
from library import*
import time

def main()->None:
    print("Welcome to the Iniversity library")
    time.sleep(1)
    # menu = Mainmenu()
    # menu.show_menu()
    # choice = menu.get_choice()
    # print(choice)
    lib = Library()
    lib.add_book("mmd", "nas", "1234")
    lib.add_book("mmd", "nas", "1234")
    lib.show_list_library()
    lib.remove_book("mmd")
    lib.add_book("ali", "nas", "-1234")
    lib.show_list_library()
    print(lib.library)
    
    
if __name__ == "__main__":
    main()