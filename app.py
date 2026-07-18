from menus import*
import time

def main()->None:
    print("Welcome to the Iniversity library")
    time.sleep(1)
    menu = Mainmenu()
    menu.show_menu()
    choice = menu.get_choice()
    print(choice)
    
if __name__ == "__main__":
    main()