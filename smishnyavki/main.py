import arcade
from main_menu import MainMenuView

def main():
    window = arcade.Window(800, 600, "RPG Game", resizable=True)
    menu = MainMenuView(window)
    window.show_view(menu)
    arcade.run()

if __name__ == "__main__":
    main()