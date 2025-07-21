import arcade
import arcade.gui
import random
import platform
import asyncio

from potion import Potion
from weapon import Weapon
from armor import Armor
from player import player
from world import WorldManager

# Константы
MIN_SCREEN_WIDTH = 800
MIN_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Лесное Приключение"

# Цвета
COLOR_NARRATIVE = arcade.color.BLUE
COLOR_INSTRUCTIONS = arcade.color.YELLOW
COLOR_PLAYER = arcade.color.GREEN
COLOR_BUTTON = arcade.color.LIGHT_BLUE
COLOR_BUTTON_HOVER = arcade.color.SKY_BLUE



class Game(arcade.View):
    def __init__(self, window):
        super().__init__(window)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.in_world_mode = False
        self.world_view = None
        self.world_manager = WorldManager(self)

        try:
            self.background = arcade.load_texture("assets/bg.png")
        except:
            self.background = None

        self.initgame()

        # Состояние игры
        self.current_event = None
        self.narrative_text = []
        self.is_question = False
        self.game_started = False
        self.instructions = [
            "Инструкция:",
            "Если вам не задаётся вопрос, жмите Enter или кнопку 'Продолжить' для продолжения",
            "Если задаётся вопрос, ответом будет 'да' или слова в скобках",
            "Любой другой ответ распознаётся как 'нет'",
            "Механики боя: блок - урезает урон противника в 2 раза и с шансом 50% наносит 1 урона, но есть 20% шанс ошибки",
            "Контратака - 40% шанс увернуться и нанести 2-3 урона",
            "Побег - 20% шанс сбежать из боя",
            "Мощная атака - шанс удвоения урона, изначально 10%",
            "Для использования предмета кликните по кнопке 'Исп.' рядом с ним"
        ]

        # UI элементы
        self.continue_button = None
        self.yes_button = None
        self.inventory_buttons = []

        self.music = {
            "ambient": "DnD Calm Fantasy Music for Adventure and Exploration _ 3 Hour Mix for Dungeons & Dragons.mp3",
            "tavern": "Reverse Dance. Medieval Dance. Hurdy-Gurdy, Organ & Drum.mp3",
            "epic": "Fantasy Celtic Music - Spirit of the Wild.mp3"
        }

        # Полные пути к файлам (предполагая, что они в папке assets/music)
        for key in self.music:
            self.music[key] = f"music/{self.music[key]}"

        self.current_music = None
        self.music_player = None

        # Параметры масштабирования
        self.font_size_base = 12

        self.setup_ui()

    def initgame(self):
        """Инициализация игровых переменных"""
        self.enemylvldefined = 0 #половина под снос
        self.map = 0
        self.critch = 10

        self.enemycounter = 0
        self.keygirl = 0
        self.ctticket = 0
        self.meetmap = 0
        self.maptoct = 0
        self.meetshop1 = 0
        self.fighthealing = 0
        self.inventory = []
        self.username = player.name

        # Список событий (mv1-mv20)
        self.events = [
            '',
            "Ты видишь небольшой храм или святилище посреди леса. Здесь можно хорошо отдохнуть и восстановить силы.",#1
            "Наступила плохая погода. В густых тропинках ты не заметила корень дерева и споткнулся об него.",
            "Ты встретила сундук посредине поляны, рядом была табличка с надписью: 'Впереди - мимик'",
            "Ты встретила сундук посредине поляны, рядом была табличка с надписью: 'Впереди - не мимик'",
            "Ты понимаешь, что третий раз выходишь на одно и то же место.",  # 5
            "Ты увидела бледную женщину в белом платье за одним из деревьев.",
            "Перед тобой женщина, это охотница, вышедшая проверить силки. Она угодила в ловушку и просит о помощи.",
            "Странные следы пересекают твой путь - такое ощущение, что прошёл кто-то весом несколько тонн",
            "На одном из деревьев ты увидела листовку с надписью 'Ведётся набор в маги-ученики'",
            "Ты видишь руины башни, здесь вполне можно остановиться на ночлег.",  # 10
            "Среди деревьев стоит заброшенная лачуга, вид которой не вызывает никаких положительных эмоций.",
            "Ты наткнулась на деревню. Звучит так будто в ней никого нет. Или точнее... Не звучит?",
            "Ты учуяла запах жареного мяса совсем близко.",
            "Остановившись на пару секунд чтобы отдохнуть, ты почувствовала, что на тебя кто-то смотрит",
            "Ты вышла из леса и увидела перед собой тропу ведущую в огромную крепость",  # 15
            "Ты увидела отблеск в земле. Подойдя ближе ты поняла, что это закопанное НЛО.",
            "Ты увидела как кто-то нацарапал «9,3,7» на дереве и превратился в прах.",
            "Услышав жужание ты резко осознала, что вокруг тебя чертовски много пчел...",
            "Внезапно ты почувствовала жуткую усталость. Вокруг тебя совсем тихо и только деревья.",
            "Из ниоткуда подошла девочка и спросила\n-Тётенька, а это не вы меня спасли тогда?"
        ]

    def play_music(self, music_type):
        """Воспроизводит выбранную музыку, останавливая предыдущую"""
        # Проверяем, что тип музыки есть в словаре
        if music_type not in self.music:
            return

        # Если тип музыки совпадает с текущим, ничего не делаем
        if music_type == self.current_music:
            return

        # Останавливаем текущую музыку если она играет
        if self.music_player:
            self.music_player.stop()

        # Загружаем и проигрываем новую музыку
        self.current_music = music_type
        try:
            sound = arcade.load_sound(self.music[music_type])
            self.music_player = arcade.play_sound(
                sound,
                looping=True,  # Зацикливаем музыку
                volume=0.1  # Громкость (0.0-1.0) # Блин вот бы еще регулировку сделать
            )
        except Exception as e:
            print(f"Ошибка при загрузке музыки: {e}")

    def setup_ui(self):
        """Настройка UI элементов"""
        # Очищаем старые элементы
        self.manager.clear()

        # Создаем основную панель для кнопок
        self.button_panel = arcade.gui.UIBoxLayout(vertical=False, space_between=10)

        # Кнопка "Продолжить"
        button_style = {
            "font_name": ("calibri", "arial"),
            "font_size": 14,
            "font_color": arcade.color.WHITE,
            "border_width": 2,
            "border_color": arcade.color.WHITE,
            "bg_color": COLOR_BUTTON,
            "bg_color_pressed": COLOR_BUTTON_HOVER,
            "border_color_pressed": arcade.color.WHITE,
            "font_color_pressed": arcade.color.WHITE,
        }


        self.continue_button = arcade.gui.UIFlatButton(
            text="Продолжить",
            width=120,
            height=40,
            style=button_style
        )
        self.continue_button.on_click = self.on_continue_click

        # Кнопка "Да"
        self.yes_button = arcade.gui.UIFlatButton(
            text="Да",
            width=80,
            height=40,
            style=button_style
        )
        self.yes_button.on_click = self.on_yes_click
        self.yes_button.visible = False

        # Кнопка "Войти в мир"
        self.world_button = arcade.gui.UIFlatButton(
            text="Войти в мир",
            width=120,
            height=40,
            style=button_style
        )
        self.world_button.on_click = self.on_world_button_click

        # Добавляем кнопки в панель
        self.button_panel.add(self.continue_button)
        self.button_panel.add(self.yes_button)
        self.button_panel.add(self.world_button)

        # Создаем контейнер для кнопок внизу экрана
        self.button_anchor = arcade.gui.UIAnchorWidget(
            anchor_x="right",
            anchor_y="bottom",
            align_x=-20,
            align_y=20,
            child=self.button_panel
        )

        self.manager.add(self.button_anchor)

        # Создаем панель для инвентаря
        self.setup_inventory_ui()

    def setup_inventory_ui(self):
        """Настройка UI инвентаря"""
        # Удаляем старые кнопки инвентаря
        for button in self.inventory_buttons:
            if hasattr(button, 'parent') and button.parent:
                self.manager.remove(button.parent)
        self.inventory_buttons.clear()

        # Создаем новые кнопки для каждого предмета в инвентаре
        for i, item in enumerate(self.inventory):
            use_button = arcade.gui.UIFlatButton(
                text="Исп.",
                width=60,
                height=30,
                style={
                    "font_name": ("calibri", "arial"),
                    "font_size": 10,
                    "font_color": arcade.color.WHITE,
                    "border_width": 1,
                    "border_color": arcade.color.WHITE,
                    "bg_color": arcade.color.DARK_BLUE,
                    "bg_color_pressed": arcade.color.BLUE,
                }
            )

            # Создаем замыкание для сохранения индекса
            def make_use_handler(index):
                def handler(event):
                    self.use_item(index)

                return handler

            use_button.on_click = make_use_handler(i)

            # Позиционируем кнопку
            button_anchor = arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="top",
                align_x=250,
                align_y=-(220 + i * 35),
                child=use_button
            )

            self.manager.add(button_anchor)
            self.inventory_buttons.append(use_button)

    def setup(self):
        self.narrative_text = [f"{self.username} ты проснулась на опушке леса и пошла куда глаза глядят"]
        self.game_started = False

        self.play_music("ambient")

    def on_resize(self, width, height):
        super().on_resize(max(width, MIN_SCREEN_WIDTH), max(height, MIN_SCREEN_HEIGHT))
        self.set_min_size(MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT) #минимальный размер окна

    def draw_background_cover(self, texture, window_width, window_height):
        if texture is None:
            # Рисуем простой градиентный фон
            arcade.draw_lrwh_rectangle_textured(
                0, 0, window_width, window_height,
                arcade.Texture.create_filled("bg", (window_width, window_height), arcade.color.DARK_GREEN)
            )
            return

        window_ratio = window_width / window_height
        texture_ratio = texture.width / texture.height

        if window_ratio > texture_ratio:
            scale = window_width / texture.width
            draw_width = window_width
            draw_height = texture.height * scale
            x = 0
            y = (window_height - draw_height) / 2
        else:
            scale = window_height / texture.height
            draw_width = texture.width * scale
            draw_height = window_height
            x = (window_width - draw_width) / 2
            y = 0

        arcade.draw_lrwh_rectangle_textured(
            x, y, draw_width, draw_height, texture
        )

    def on_draw(self):
        arcade.start_render()
        if self.in_world_mode and self.world_view:
            self.world_view.on_draw()
            return

        # Рисуем фон
        if self.background:
            self.draw_background_cover(self.background, self.window.width, self.window.height)
        else:
            arcade.draw_rectangle_filled(self.window.width // 2, self.window.height // 2,
                                         self.window.width, self.window.height,
                                         arcade.color.DARK_GREEN)

        screen_width = max(self.window.width, MIN_SCREEN_WIDTH)
        screen_height = max(self.window.height, MIN_SCREEN_HEIGHT)

        # Панель статистики
        stats_width = screen_width * 0.35
        arcade.draw_rectangle_filled(stats_width / 2, screen_height / 2, stats_width, screen_height,
                                     arcade.color.BLACK + (100,))

        # Масштабирование шрифтов
        scale_factor = min(screen_width / MIN_SCREEN_WIDTH, screen_height / MIN_SCREEN_HEIGHT)
        font_size_stats = self.font_size_base * scale_factor * 1.2
        font_size_narrative = self.font_size_base * scale_factor * 1.2
        font_size_instructions = self.font_size_base * scale_factor * 0.9

        # Статистики игрока
        y = screen_height * 0.9
        arcade.draw_text(f"Имя: {player.name}", 20, y, COLOR_PLAYER, font_size_stats, bold=True)
        y -= screen_height * 0.05
        arcade.draw_text(f"Здоровье: {player.health}/{player.maxhealth}", 20, y, arcade.color.WHITE, font_size_stats)
        y -= screen_height * 0.05
        arcade.draw_text(f"Деньги: {player.money}", 20, y, arcade.color.WHITE, font_size_stats)
        y -= screen_height * 0.05
        arcade.draw_text(f"Урон: {player.damage}", 20, y, arcade.color.WHITE, font_size_stats)
        y -= screen_height * 0.05
        arcade.draw_text(f"Шанс крита: {player.critch}%", 20, y, arcade.color.WHITE, font_size_stats)
        y -= screen_height * 0.05
        arcade.draw_text(f"Броня: {player.armor}", 20, y, arcade.color.WHITE, font_size_stats)

        # Инвентарь
        y -= screen_height * 0.05
        arcade.draw_text("Инвентарь:", 20, y, COLOR_PLAYER, font_size_stats, bold=True)
        y -= screen_height * 0.05
        for i, item in enumerate(self.inventory):
            if y < screen_height * 0.1:
                break
            arcade.draw_text(str(item), 20, y, arcade.color.WHITE, font_size_stats)
            y -= screen_height * 0.05

        # Панель сюжета
        y = screen_height * 0.9
        max_lines = min(len(self.narrative_text), 12)  # Ограничиваем количество строк
        for line in self.narrative_text[-max_lines:]:
            # Разбиваем длинные строки
            words = line.split()
            current_line = ""
            max_width = screen_width * 0.6 - 40  # Максимальная ширина строки

            for word in words:
                test_line = current_line + " " + word if current_line else word
                # Приблизительная проверка ширины (нужно улучшить)
                if len(test_line) * font_size_narrative * 0.5 > max_width and current_line:
                    arcade.draw_text(current_line, stats_width + 20, y, COLOR_NARRATIVE, font_size_narrative)
                    y -= screen_height * 0.04
                    current_line = word
                    if y < screen_height * 0.15:
                        break
                else:
                    current_line = test_line

            if current_line and y >= screen_height * 0.15:
                arcade.draw_text(current_line, stats_width + 20, y, COLOR_NARRATIVE, font_size_narrative)
                y -= screen_height * 0.04

            if y < screen_height * 0.15:
                break

        # Инструкции (показываем только если игра не начата)
        if not self.game_started:
            y = screen_height * 0.4
            for line in self.instructions:
                if y < screen_height * 0.1:
                    break
                arcade.draw_text(line, stats_width + 20, y, COLOR_INSTRUCTIONS, font_size_instructions)
                y -= screen_height * 0.03

        # Рисуем UI элементы
        self.manager.draw()

    def on_continue_click(self, event):
        """Обработчик нажатия кнопки 'Продолжить'"""
        if not self.game_started:
            self.username = player.name
            self.narrative_text = [
                f"Привет {self.username}, по сюжету ты просыпаешься в густом лесу мира фентези, пытаешься выжить и попасть обратно в реальный мир"
            ]
            self.game_started = True

        self.handle_continue()

    def on_world_button_click(self, event):
        """Обработчик кнопки входа в мир"""
        self.world_manager.enter_world_mode()

    def on_yes_click(self, event):
        """Обработчик нажатия кнопки 'Да'"""
        self.handle_yes()

    def on_key_press(self, key, modifiers):
        if not self.game_started:
            if key == arcade.key.ENTER:

                self.narrative_text = [
                    f"Привет {self.username}, по сюжету ты просыпаешься в густом лесу мира фентези, пытаешься выжить и попасть обратно в реальный мир"
                ]
                self.game_started = True
                self.handle_continue()
        else:
            if key == arcade.key.ENTER:
                self.handle_continue()
            elif key in [arcade.key.D, arcade.key.Y]:
                if self.yes_button.visible:
                    self.handle_yes()

    def use_item(self, index):
        """Использование предмета из инвентаря"""
        if 0 <= index < len(self.inventory):
            item = self.inventory[index]
            item.use(self, player)
            if isinstance(item, Potion):
                self.inventory.pop(index)
            self.setup_inventory_ui()  # Обновляем кнопки инвентаря

    def handle_continue(self):
        if not self.game_started:
            return
        self.current_event = random.choice(self.events)
        self.narrative_text.append(self.current_event)

        # Показываем кнопку "Да" для определенных событий
        self.yes_button.visible = self.current_event in [self.events[8], self.events[20]]

        # Обработка сундуков
        if self.current_event in [self.events[3], self.events[4]]:
            if random.random() < 0.9:
                itemtype = random.randint(1,3)
                if itemtype == 1:
                    item = Weapon()
                    item.generate()
                elif itemtype == 2:
                    item = Potion()
                elif itemtype == 3:
                    item = Armor()

                # item = random.choice([
                #     Potion("Малое зелье", 10),
                #     Weapon(),
                #     Armor("Кожаная броня", 3)
                # ])

                self.inventory.append(item)
                self.narrative_text.append(f"Ты нашла {item.name} в сундуке!")
                self.setup_inventory_ui()
            else:
                self.narrative_text.append("Сундук оказался пустым...")

        # Особые события
        if self.current_event == self.events[8]:
            self.meettrollshop()
        elif self.current_event == self.events[20]:
            self.keygirl = 1

    def handle_yes(self):
        self.narrative_text.append("Ты ответила 'Да'")
        self.yes_button.setVisible(False)

        if self.current_event == self.events[8]:
            self.meettrollshop()
        elif self.current_event == self.events[20]:
            self.keygirl = 1

    def update_stats(self):
        pass

    def meettrollshop(self):
        self.narrative_text.append("Ты встретила торговца-тролля!")

    def meetshop(self):
        pass

    def meetmapper(self):
        pass

    def meetcity(self):
        pass

    def fight(self):
        pass

    def meetctshop(self):
        pass

    def enter_shop(self):
        # Переключаем на музыку таверны
        self.play_music("tavern")

    def exit_shop(self):
        # Возвращаем фоновую музыку
        self.play_music("ambient")


async def main():
    game = Game()
    game.setup()
    arcade.run()


# if platform.system() == "Emscripten":
#     asyncio.ensure_future(main())
# else:
#     if __name__ == "__main__":
#         asyncio.run(main())