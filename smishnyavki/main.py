import arcade
from main_menu import MainMenuView

def main():
    window = arcade.Window(1200, 800, "RPG Game")
    menu = MainMenuView(window)
    window.show_view(menu)
    arcade.run()

if __name__ == "__main__":
    main()