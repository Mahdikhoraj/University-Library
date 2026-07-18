from valid import Validations
class Mainmenu:
    def __init__(self):
        self.option = {
            "1" : "Show book information",
            "2" : "change price",
            "3" : "compare books",
            "4" : "borrow book",
            "5" : "add book",
            "6" : "delete book",
            "7" : "show book list",
            "8" : "search"
        }
    def show_menu(self):
        for key , value in self.option.items():
            print(f"{key} : {value}")
            
    def get_choice(self,prompt:str = "Enter your choice from menu:"):
        while True:
            choice = input(prompt)
            if Validations.is_valid_menu_choice(choice,self.option):
                return choice
            else:
                print("Its not true, please try again..!")
                
                
                
# user = Mainmenu()
# user.show_menu()
# user.get_choice()
            