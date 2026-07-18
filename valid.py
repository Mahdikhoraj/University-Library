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
