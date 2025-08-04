import arcade
import arcade.gui


class SettingsView(arcade.View):
    def __init__(self, previous_view):
        super().__init__()
        self.previous_view = previous_view

        # Менеджер UI
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Настройки по умолчанию
        self.volume = 0.5
        self.fullscreen = False
        self.resolution_options = ["800x600", "1024x768", "1280x720", "1366x768", "1920x1080"]
        self.current_resolution_index = 2  # Индекс для 1280x720
        self.current_resolution = self.resolution_options[self.current_resolution_index]

        self.setup_ui()

    def setup_ui(self):
        # Основной контейнер
        self.vbox = arcade.gui.UIBoxLayout()

        # Заголовок
        title = arcade.gui.UITextArea(text="Настройки",
                                      width=400,
                                      height=40,
                                      font_size=24,
                                      font_name="Arial")
        self.vbox.add(title)

        # === РАЗРЕШЕНИЕ ===
        resolution_label = arcade.gui.UITextArea(text="Разрешение:",
                                                 width=200,
                                                 height=30,
                                                 font_size=16)
        self.vbox.add(resolution_label)

        # Навигация по разрешению со стрелками
        resolution_hbox = arcade.gui.UIBoxLayout(vertical=False)

        self.resolution_left_button = arcade.gui.UIFlatButton(text="<", width=40, height=40)
        self.resolution_left_button.on_click = self.resolution_previous

        self.resolution_display = arcade.gui.UITextArea(text=self.current_resolution,
                                                        width=120,
                                                        height=40,
                                                        font_size=16)

        self.resolution_right_button = arcade.gui.UIFlatButton(text=">", width=40, height=40)
        self.resolution_right_button.on_click = self.resolution_next

        resolution_hbox.add(self.resolution_left_button)
        resolution_hbox.add(self.resolution_display)
        resolution_hbox.add(self.resolution_right_button)

        self.vbox.add(resolution_hbox)

        # === ГРОМКОСТЬ ===
        volume_label = arcade.gui.UITextArea(text=f"Громкость: {int(self.volume * 100)}%",
                                             width=200,
                                             height=30,
                                             font_size=16)
        self.vbox.add(volume_label)

        # Слайдер громкости
        self.volume_slider = arcade.gui.UISlider(
            value=self.volume,
            min_value=0,
            max_value=1,
            width=200,
            height=20
        )
        self.volume_slider.on_change = self.on_volume_change
        self.volume_label = volume_label  # Сохраняем ссылку для обновления
        self.vbox.add(self.volume_slider)

        # === ПОЛНОЭКРАННЫЙ РЕЖИМ ===
        fullscreen_hbox = arcade.gui.UIBoxLayout(vertical=False)

        self.fullscreen_checkbox = arcade.gui.UIInputText(
            text="",
            width=20,
            height=20
        )
        # Имитация чекбокса через кнопку
        self.fullscreen_button = arcade.gui.UIFlatButton(
            text="☐" if not self.fullscreen else "☑",
            width=30,
            height=30
        )
        self.fullscreen_button.on_click = self.toggle_fullscreen

        fullscreen_text = arcade.gui.UITextArea(text="Полноэкранный режим",
                                                width=200,
                                                height=30,
                                                font_size=16)

        fullscreen_hbox.add(self.fullscreen_button)
        fullscreen_hbox.add(fullscreen_text)
        self.vbox.add(fullscreen_hbox)

        # === КНОПКИ УПРАВЛЕНИЯ ===
        buttons_hbox = arcade.gui.UIBoxLayout(vertical=False)

        # Кнопка "Применить"
        apply_button = arcade.gui.UIFlatButton(text="Применить", width=100, height=40)
        apply_button.on_click = self.apply_settings

        # Кнопка "Назад"
        back_button = arcade.gui.UIFlatButton(text="Назад", width=100, height=40)
        back_button.on_click = self.go_back

        buttons_hbox.add(apply_button)
        buttons_hbox.add(back_button)

        self.vbox.add(buttons_hbox)

        # Добавляем контейнер в менеджер
        self.manager.add(
            arcade.gui.UIAnchorLayout(
                children=[self.vbox]
            )
        )

    def resolution_previous(self, event):
        """Предыдущее разрешение"""
        self.current_resolution_index = (self.current_resolution_index - 1) % len(self.resolution_options)
        self.current_resolution = self.resolution_options[self.current_resolution_index]
        self.resolution_display.text = self.current_resolution

    def resolution_next(self, event):
        """Следующее разрешение"""
        self.current_resolution_index = (self.current_resolution_index + 1) % len(self.resolution_options)
        self.current_resolution = self.resolution_options[self.current_resolution_index]
        self.resolution_display.text = self.current_resolution

    def on_resolution_change(self, event):
        """Обработчик изменения разрешения"""
        self.current_resolution = event.source.value

    def on_volume_change(self, event):
        """Обработчик изменения громкости"""
        self.volume = event.source.value
        self.volume_label.text = f"Громкость: {int(self.volume * 100)}%"
        
        import main_scene
        main_scene.GAME_VOLUME = self.volume
        
        if hasattr(self.previous_view, 'window') and self.previous_view.window.current_view:
            current_view = self.previous_view.window.current_view
            if hasattr(current_view, 'update_music_volume'):
                current_view.update_music_volume()

    def toggle_fullscreen(self, event):
        """Переключение полноэкранного режима"""
        self.fullscreen = not self.fullscreen
        self.fullscreen_button.text = "☑" if self.fullscreen else "☐"
        print(f"Полноэкранный режим: {'Включен' if self.fullscreen else 'Выключен'}")

    def apply_settings(self, event):
        """Применить настройки"""
        try:
            if self.fullscreen:
                self.window.set_fullscreen(True)
            else:
                self.window.set_fullscreen(False)
                
            if not self.fullscreen:
                width, height = map(int, self.current_resolution.split('x'))
                self.window.set_size(width, height)

            print(f"Настройки применены: {self.current_resolution}, "
                  f"Громкость: {int(self.volume * 100)}%, "
                  f"Полноэкранный: {self.fullscreen}")

            self.go_back(event)
        except Exception as e:
            print(f"Ошибка при применении настроек: {e}")

    def go_back(self, event):
        """Вернуться к предыдущему экрану"""
        self.manager.disable()
        self.window.show_view(self.previous_view)

    def on_draw(self):
        """Отрисовка"""
        self.clear()
        self.manager.draw()

    def on_show_view(self):
        """При показе окна"""
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def on_update(self, delta_time):
        """Обновление"""
        self.manager.on_update(delta_time)

    def on_key_press(self, key, modifiers):
        """Обработка нажатий клавиш"""
        if key == arcade.key.ESCAPE:
            self.go_back(None)
        elif key == arcade.key.F11:
            # Переключение полноэкранного режима по F11
            self.fullscreen = not self.fullscreen
            self.fullscreen_button.text = "☑" if self.fullscreen else "☐"
            print(f"Полноэкранный режим (F11): {'Включен' if self.fullscreen else 'Выключен'}")

    def on_mouse_press(self, x, y, button, modifiers):
        """Обработка нажатий мыши"""
        self.manager.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        """Обработка отпускания мыши"""
        self.manager.on_mouse_release(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        """Обработка движения мыши"""
        self.manager.on_mouse_motion(x, y, dx, dy)
