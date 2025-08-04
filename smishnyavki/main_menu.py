import arcade
import arcade.gui
from main_scene import Game
from settings import SettingsView
class MainMenuView(arcade.View):
    def __init__(self, window):
        super().__init__(window)
        self.manager = arcade.gui.UIManager()

        # Кнопки
        self.vbox = arcade.gui.UIBoxLayout(space_between=20)

        self.play_button = arcade.gui.UIFlatButton(text="Играть", width=200)
        self.play_button.on_click = self.on_play_click
        self.vbox.add(self.play_button)

        self.settings_button = arcade.gui.UIFlatButton(text="Настройки", width=200)
        self.settings_button.on_click = self.on_settings_click
        self.vbox.add(self.settings_button)

        self.quit_button = arcade.gui.UIFlatButton(text="Выйти", width=200)
        self.quit_button.on_click = self.on_quit_click
        self.vbox.add(self.quit_button)

        # В новой версии используется UIAnchorLayout
        self.manager.add(
            arcade.gui.UIAnchorLayout(
                children=[self.vbox],
                # позиционирование:
                # anchor_x="center_x", anchor_y="center_y" - по центру (по умолчанию)
                # anchor_x="left", anchor_y="top" - левый верхний угол
                # anchor_x="right", anchor_y="bottom" - правый нижний угол
            )
        )

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        # В новой версии используется self.clear() вместо arcade.start_render()
        self.clear()

        arcade.draw_text("Главное меню",
                         self.window.width // 2,
                         self.window.height - 100,
                         arcade.color.WHITE,
                         font_size=32,
                         anchor_x="center")

        self.manager.draw()

    def on_key_press(self, key, modifiers):
        """Обработка нажатий клавиш"""
        if key == arcade.key.ESCAPE:
            # Открываем настройки
            settings_view = SettingsView(self)
            self.window.show_view(settings_view)

    def on_play_click(self, event):
        game = Game(self.window)
        self.window.show_view(game)

    def on_settings_click(self, event):
        settings_view = SettingsView(self)
        self.window.show_view(settings_view)

    def on_quit_click(self, event):
        arcade.close_window()