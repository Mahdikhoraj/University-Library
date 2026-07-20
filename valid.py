__all__ = [
    "Validations",
]


class Validations:
    @staticmethod
    def is_valid_menu_choice(choice: str, menu: dict) -> bool:
        if choice in menu:
            return True
        else:
            return False
        
    @staticmethod
    def is_valid_price(price):
        if price >= 0:
            return True
        return False
