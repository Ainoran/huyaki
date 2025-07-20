import arcade
import random
import platform
import asyncio
from potion import Potion
from weapon import Weapon
from armor import Armor


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


class Game(arcade.Window):
    def __init__(self):
        super().__init__(MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)

        self.background = None
        self.background = arcade.load_texture("assets/hahaha.jpg")


        # Инициализация переменных игры
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

        # К buttons инвентаря
        self.inventory_buttons = []

        # Параметры масштабирования
        self.font_size_base = 12
        self.button_width_base = 100
        self.button_height_base = 40


    def initgame(self):
        """Инициализация игровых переменных"""
        self.enemylvldefined = 0
        self.map = 0
        self.critch = 10
        self.maxhealth = 25
        self.health = 10
        self.money = 700
        self.damage = 2
        self.enemycounter = 0
        self.armor = 0
        self.keygirl = 0
        self.ctticket = 0
        self.meetmap = 0
        self.maptoct = 0
        self.meetshop1 = 0
        self.fighthealing = 0
        self.inventory = []
        self.username = ""



        # Список событий (mv1-mv20)
        self.events = [
            ''
            "Ты видишь небольшой храм или святилище посреди леса. Здесь можно хорошо отдохнуть и восстановить силы.",#1
            "Наступила плохая погода. В густых тропинках ты не заметила корень дерева и споткнулся об него.",
            "Ты встретила сундук посредине поляны, рядом была табличка с надписью: 'Впереди - мимик'",
            "Ты встретила сундук посредине поляны, рядом была табличка с надписью: 'Впереди - не мимик'",
            "Ты понимаешь, что третий раз выходишь на одно и то же место.", #5
            "Ты увидела бледную женщину в белом платье за одним из деревьев.",
            "Перед тобой женщина, это охотница, вышедшая проверить силки. Она угодила в ловушку и просит о помощи.",
            "Странные следы пересекают твой путь - такое ощущение, что прошёл кто-то весом несколько тонн",
            "На одном из деревьев ты увидела листовку с надписью 'Ведётся набор в маги-ученики'",
            "Ты видишь руины башни, здесь вполне можно остановиться на ночлег.",#10
            "Среди деревьев стоит заброшенная лачуга, вид которой не вызывает никаких положительных эмоций.",
            "Ты наткнулась на деревню. Звучит так будто в ней никого нет. Или точнее... Не звучит?",
            "Ты учуяла запах жареного мяса совсем близко.",
            "Остановившись на пару секунд чтобы отдохнуть, ты почувствовала, что на тебя кто-то смотрит",
            "Ты вышла из леса и увидела перед собой тропу ведущую в огромную крепость", #15
            "Ты увидела отблеск в земле. Подойдя ближе ты поняла, что это закопанное НЛО.",
            "Ты увидела как кто-то нацарапал «9,3,7» на дереве и превратился в прах.",
            "Услышав жужание ты резко осознала, что вокруг тебя чертовски много пчел...",
            "Внезапно ты почувствовала жуткую усталость. Вокруг тебя совсем тихо и только деревья.",
            "Из ниоткуда подошла девочка и спросила\n-Тётенька, а это не вы меня спасли тогда?"
        ]

    def setup(self):
        self.narrative_text = [f"{self.username} ты проснулась на опушке леса и пошла куда глаза глядят"]

        self.game_started = False
        self.update_layout()

    def update_layout(self):
        screen_width = max(self.width, MIN_SCREEN_WIDTH)
        screen_height = max(self.height, MIN_SCREEN_HEIGHT)

        # Масштабирование шрифтов
        scale_factor = min(screen_width / MIN_SCREEN_WIDTH, screen_height / MIN_SCREEN_HEIGHT)
        self.font_size_stats = self.font_size_base * scale_factor * 1.2
        self.font_size_narrative = self.font_size_base * scale_factor * 1.2
        self.font_size_instructions = self.font_size_base * scale_factor * 0.9

        # Обновление кнопок Продолжить/Да
        self.continue_button = {
            "x": screen_width * 0.75, "y": screen_height * 0.1,
            "width": self.button_width_base * scale_factor, "height": self.button_height_base * scale_factor,
            "text": "Продолжить", "hover": False
        }
        self.yes_button = {
            "x": screen_width * 0.65, "y": screen_height * 0.1,
            "width": self.button_width_base * scale_factor * 0.8, "height": self.button_height_base * scale_factor,
            "text": "Да", "hover": False, "visible": False
        }

        # Обновление кнопок инвентаря
        self.inventory_buttons = []
        y = screen_height * 0.35
        for i, item in enumerate(self.inventory):
            if y < screen_height * 0.1:
                break
            self.inventory_buttons.append({
                "x": screen_width * 0.30, "y": y,
                "width": self.button_width_base * scale_factor * 0.5,
                "height": self.button_height_base * scale_factor * 0.8,
                "text": "Исп.", "hover": False, "item_index": i
            })
            y -= screen_height * 0.05

    def on_resize(self, width, height):
        super().on_resize(max(width, MIN_SCREEN_WIDTH), max(height, MIN_SCREEN_HEIGHT))
        self.update_layout()

    def draw_background_cover(self, texture, window_width, window_height):
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
        self.draw_background_cover(self.background, self.width, self.height)
        screen_width = max(self.width, MIN_SCREEN_WIDTH)
        screen_height = max(self.height, MIN_SCREEN_HEIGHT)

        # Панель статистики
        stats_width = screen_width * 0.35
        arcade.draw_rectangle_filled(stats_width / 2, screen_height / 2, stats_width, screen_height, arcade.float_to_byte_color((0.8, 0.8, 0.8, 0.4)))

        y = screen_height * 0.9
        arcade.draw_text(f"Имя: {self.username}", 20, y, COLOR_PLAYER, self.font_size_stats, bold=True)
        y -= screen_height * 0.05
        arcade.draw_text(f"Здоровье: {self.health}/{self.maxhealth}", 20, y, arcade.color.WHITE, self.font_size_stats)
        y -= screen_height * 0.05
        arcade.draw_text(f"Деньги: {self.money}", 20, y, arcade.color.WHITE, self.font_size_stats)
        y -= screen_height * 0.05
        arcade.draw_text(f"Урон: {self.damage}", 20, y, arcade.color.WHITE, self.font_size_stats)
        y -= screen_height * 0.05
        arcade.draw_text(f"Шанс крита: {self.critch}%", 20, y, arcade.color.WHITE, self.font_size_stats)
        y -= screen_height * 0.05
        arcade.draw_text(f"Броня: {self.armor}", 20, y, arcade.color.WHITE, self.font_size_stats)

        # Инвентарь
        y -= screen_height * 0.05
        arcade.draw_text("Инвентарь:", 20, y, COLOR_PLAYER, self.font_size_stats, bold=True)
        y -= screen_height * 0.05
        for i, item in enumerate(self.inventory):
            if y < screen_height * 0.1:
                break
            arcade.draw_text(str(item), 20, y, arcade.color.WHITE, self.font_size_stats)
            if i < len(self.inventory_buttons):
                button = self.inventory_buttons[i]
                button_color = COLOR_BUTTON_HOVER if button["hover"] else COLOR_BUTTON
                arcade.draw_rectangle_filled(button["x"], button["y"], button["width"], button["height"], button_color)
                arcade.draw_text(button["text"], button["x"] - button["width"] * 0.3,
                                 button["y"] - button["height"] * 0.25,
                                 arcade.color.WHITE, self.font_size_narrative * 0.8)
            y -= screen_height * 0.05

        # Панель сюжета
        # arcade.draw_rectangle_filled(stats_width + (screen_width * 0.65 / 2), screen_height / 2,
        #                              screen_width * 0.65, screen_height, arcade.color.DARK_GRAY, )
        y = screen_height * 0.9
        for line in self.narrative_text[-5:]:
            arcade.draw_text(line, stats_width + 20, y, COLOR_NARRATIVE, self.font_size_narrative)
            y -= screen_height * 0.05
            if y < screen_height * 0.3:
                break

        # Инструкции
        if not self.game_started:
            y = screen_height * 0.4
            for line in self.instructions:
                arcade.draw_text(line, stats_width + 20, y, COLOR_INSTRUCTIONS, self.font_size_instructions)
                y -= screen_height * 0.03
                if y < screen_height * 0.1:
                    break

        # Кнопки Продолжить/Да
        button_color = COLOR_BUTTON_HOVER if self.continue_button["hover"] else COLOR_BUTTON
        arcade.draw_rectangle_filled(self.continue_button["x"], self.continue_button["y"],
                                     self.continue_button["width"], self.continue_button["height"], button_color)
        arcade.draw_text(self.continue_button["text"], self.continue_button["x"] - self.continue_button["width"] * 0.4,
                         self.continue_button["y"] - self.continue_button["height"] * 0.25,
                         arcade.color.WHITE, self.font_size_narrative)

        if self.yes_button["visible"]:
            button_color = COLOR_BUTTON_HOVER if self.yes_button["hover"] else COLOR_BUTTON
            arcade.draw_rectangle_filled(self.yes_button["x"], self.yes_button["y"],
                                         self.yes_button["width"], self.yes_button["height"], button_color)
            arcade.draw_text(self.yes_button["text"], self.yes_button["x"] - self.yes_button["width"] * 0.3,
                             self.yes_button["y"] - self.yes_button["height"] * 0.25,
                             arcade.color.WHITE, self.font_size_narrative)

    def on_mouse_motion(self, x, y, dx, dy):
        self.continue_button["hover"] = (self.continue_button["x"] - self.continue_button["width"] / 2 < x <
                                         self.continue_button["x"] + self.continue_button["width"] / 2 and
                                         self.continue_button["y"] - self.continue_button["height"] / 2 < y <
                                         self.continue_button["y"] + self.continue_button["height"] / 2)
        self.yes_button["hover"] = (self.yes_button["x"] - self.yes_button["width"] / 2 < x <
                                    self.yes_button["x"] + self.yes_button["width"] / 2 and
                                    self.yes_button["y"] - self.yes_button["height"] / 2 < y <
                                    self.yes_button["y"] + self.yes_button["height"] / 2 and self.yes_button["visible"])

        for button in self.inventory_buttons:
            button["hover"] = (button["x"] - button["width"] / 2 < x < button["x"] + button["width"] / 2 and
                               button["y"] - button["height"] / 2 < y < button["y"] + button["height"] / 2)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.continue_button["hover"]:
            self.handle_continue()
        if self.yes_button["hover"] and self.yes_button["visible"]:
            self.handle_yes()
        for button in self.inventory_buttons:
            if button["hover"]:
                self.use_item(button["item_index"])

    def on_key_press(self, key, modifiers):
        if not self.game_started:
            if key == arcade.key.ENTER:
                self.username = "Игрок"
                self.narrative_text = [
                    f"Привет {self.username}, по сюжету ты просыпаешься в густом лесу мира фентези, пытаешься выжить и попасть обратно в реальный мир"]
                self.game_started = True
                self.handle_continue()
        else:
            if key == arcade.key.ENTER:
                self.handle_continue()
            elif key in [arcade.key.D, arcade.key.Y]:
                if self.yes_button["visible"]:
                    self.handle_yes()

    def use_item(self, index):
        """Использование предмета из инвентаря"""
        if 0 <= index < len(self.inventory):
            item = self.inventory[index]
            item.use(self)
            if isinstance(item, Potion):
                self.inventory.pop(index)
            self.update_layout()

    def handle_continue(self):
        if not self.game_started:
            return
        self.current_event = random.choice(self.events)
        if self.current_event == '':
            self.current_event = random.choice(self.events)
        self.narrative_text.append(self.current_event)
        self.yes_button["visible"] = self.current_event in [self.events[8], self.events[20]]
        if self.current_event in [self.events[3], self.events[4]]:
            if random.random() < 0.2:
                item = random.choice([
                    Potion("Малое зелье", 10),
                    Weapon("Меч", 6),
                    Armor("Кожаная броня", 3)
                ])
                self.inventory.append(item)
                self.narrative_text.append(f"Ты нашла {item.name} в сундуке!")
            else:
                self.narrative_text.append("Сундук оказался пустым...")
        if self.current_event == self.events[8]:
            self.meettrollshop()
        elif self.current_event == self.events[20]:
            self.keygirl = 1
        self.update_layout()

    def handle_yes(self):
        self.narrative_text.append("Ты ответила 'Да'")
        self.yes_button["visible"] = False
        if self.current_event == self.events[6]:
            self.meettrollshop()
        elif self.current_event == self.events[19]:
            self.keygirl = 1
        self.update_layout()

    def update_stats(self):
        pass

    def meettrollshop(self):
        pass

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


async def main():
    game = Game()
    game.setup()
    arcade.run()


if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())