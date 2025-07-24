import arcade
from main_menu import MainMenuView

def main():
    window = arcade.Window(800, 600, "RPG Game", resizable=True)
    menu = MainMenuView(window)
    window.set_min_size(800, 600)

    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()