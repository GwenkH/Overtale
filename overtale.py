from game.base_game import BaseGame

class Overtale(BaseGame):
    def create(self) -> None:
        from game.main_menu import MainMenu
        Overtale.set_current_view(MainMenu())
