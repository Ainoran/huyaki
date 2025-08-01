import arcade
import arcade.gui
from arcade.gui import UIFlatButton
from arcade.gui.widgets.buttons import UIFlatButton
import random
import math
from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple, Optional
from potion import Potion
from weapon import Weapon
from armor import Armor
from playerdata import player
from enemydata import Enemy
from eventsdata import Event

class LocationType(Enum):
    FOREST = "forest"
    SHRINE = "shrine"
    RUINS = "ruins"
    VILLAGE = "village"
    CAMP = "camp"
    CHEST = "chest"
    SHOP = "shop"
    BOSS = "boss"


class EventType(Enum):
    FIGHT = "fight"
    TREASURE = "treasure"
    HEALING = "healing"
    SHOP = "shop"
    STORY = "story"
    BOSS_FIGHT = "boss_fight"


@dataclass
class WorldLocation:
    x: float
    y: float
    location_type: LocationType
    event_type: EventType
    name: str
    description: str
    discovered: bool = False
    completed: bool = False
    sprite_name: str = ""

    def get_sprite_color(self):
        """Возвращает цвет спрайта в зависимости от типа локации"""
        color_map = {
            LocationType.FOREST: arcade.color.DARK_GREEN,
            LocationType.SHRINE: arcade.color.GOLD,
            LocationType.RUINS: arcade.color.GRAY,
            LocationType.VILLAGE: arcade.color.BROWN,
            LocationType.CAMP: arcade.color.ORANGE,
            LocationType.CHEST: arcade.color.YELLOW,
            LocationType.SHOP: arcade.color.PURPLE,
            LocationType.BOSS: arcade.color.RED
        }
        return color_map.get(self.location_type, arcade.color.WHITE)


class World2D:
    def __init__(self, width: int = 1200, height: int = 800):
        self.width = width
        self.height = height
        self.locations: List[WorldLocation] = []
        self.player_x = width // 2
        self.player_y = height // 2
        self.camera_x = 0
        self.camera_y = 0
        self.player_speed = 3
        self.zoom = 1.0
        self.min_zoom = 0.5
        self.max_zoom = 2.0

        # Генерируем мир
        self.generate_world()

    def generate_world(self):
        """Генерирует случайные локации по всему миру"""
        self.locations.clear()

        # Центральная стартовая локация
        self.locations.append(WorldLocation(
            self.width // 2, self.height // 2,
            LocationType.FOREST, EventType.STORY,
            "Стартовая поляна",
            "Место, где ты проснулась",
            discovered=True
        ))

        # Генерируем случайные локации
        location_configs = [
            (LocationType.SHRINE, EventType.HEALING, "Лесное святилище", "Здесь можно восстановить силы"),
            (LocationType.RUINS, EventType.TREASURE, "Древние руины", "Таинственные руины с сокровищами"),
            (LocationType.VILLAGE, EventType.SHOP, "Заброшенная деревня", "Здесь можно найти торговца"),
            (LocationType.CAMP, EventType.FIGHT, "Лагерь разбойников", "Опасное место с врагами"),
            (LocationType.CHEST, EventType.TREASURE, "Загадочный сундук", "Сундук посреди поляны"),
            (LocationType.SHOP, EventType.SHOP, "Лавка торговца", "Странная лавка посреди леса"),
        ]

        # Размещаем по 3-5 локаций каждого типа
        for config in location_configs:
            count = random.randint(3, 5)
            for _ in range(count):
                x = random.randint(100, self.width - 100)
                y = random.randint(100, self.height - 100)

                # Проверяем, что локация не слишком близко к другим
                if self.is_position_valid(x, y, 80):
                    self.locations.append(WorldLocation(x, y, *config))

        # Добавляем несколько боссов
        for i in range(2):
            x = random.randint(100, self.width - 100)
            y = random.randint(100, self.height - 100)
            if self.is_position_valid(x, y, 120):
                self.locations.append(WorldLocation(
                    x, y, LocationType.BOSS, EventType.BOSS_FIGHT,
                    f"Логово {['Дракона', 'Лича'][i]}",
                    f"Опасное место, где обитает могущественный {['дракон', 'лич'][i]}"
                ))

    def is_position_valid(self, x: float, y: float, min_distance: float) -> bool:
        """Проверяет, что позиция не слишком близко к существующим локациям"""
        for location in self.locations:
            distance = math.sqrt((x - location.x) ** 2 + (y - location.y) ** 2)
            if distance < min_distance:
                return False
        return True

    def move_player(self, dx: float, dy: float):
        """Перемещает игрока с проверкой границ"""
        new_x = max(20, min(self.width - 20, self.player_x + int(dx) * self.player_speed))
        new_y = max(20, min(self.height - 20, self.player_y + int(dy) * self.player_speed))

        self.player_x = new_x
        self.player_y = new_y

        # Обновляем камеру
        self.update_camera()

    def update_camera(self):
        """Обновляет позицию камеры для следования за игроком"""
        self.camera_x = self.player_x
        self.camera_y = self.player_y

    def get_nearby_location(self, distance: float = 50) -> Optional[WorldLocation]:
        """Возвращает ближайшую локацию в радиусе distance"""
        for location in self.locations:
            dist = math.sqrt((self.player_x - location.x) ** 2 + (self.player_y - location.y) ** 2)
            if dist <= distance:
                return location
        return None

    def discover_nearby_locations(self, radius: float = 100):
        """Открывает локации в радиусе обзора игрока"""
        for location in self.locations:
            dist = math.sqrt((self.player_x - location.x) ** 2 + (self.player_y - location.y) ** 2)
            if dist <= radius:
                location.discovered = True

class EventSystem:
    def __init__(self):
        self.event = Event()
        self.event_log = []
        self.player_turn_in_event = True
        self.event_active = False
    def start_event(self):
        self.event.generate()
        self.event_log = [self.event.desc]
        self.event_active = True
        self.player_turn_in_event = True

    def end_event(self):
        self.event_active = False

class FightSystem:
    def __init__(self):
        self.enemy = Enemy()
        self.fight_log = []
        self.player_turn = True
        self.fight_active = False



    def start_fight(self):
        """Начинает бой с врагом указанного уровня"""
        self.enemy.generate()
        self.fight_log = [f"Началась битва с {self.enemy.name}!"]
        self.fight_active = True
        self.player_turn = True
        return self.enemy # А это вообще надо?

    def player_attack(self):

        """Обычная атака игрока"""
        if not self.fight_active or not self.player_turn:
            return False

        damage_in_this_turn = player.damage

        # Проверка критического удара
        if random.random() * 100 < player.critch:
            damage_in_this_turn *= 2
            crit_text = " (КРИТИЧЕСКИЙ УДАР!)"
        else:
            crit_text = ""
        actual_damage = self.enemy.take_damage(damage_in_this_turn)
        self.fight_log.append(f"Ты наносишь {actual_damage} урона{crit_text}")

        if not self.enemy.is_alive():
            self.end_fight(victory=True)
            return True

        self.player_turn = False
        return True

    def player_power_attack(self):
        """Мощная атака с шансом удвоения урона"""
        if not self.fight_active or not self.player_turn:
            return False

        base_damage = player.damage

        # Шанс удвоения урона
        if random.random() * 100 < player.critch:
            damage = base_damage * 2
            self.fight_log.append("Мощная атака удалась!")
        else:
            damage = base_damage

        # Проверка обычного крита поверх мощной атаки
        if random.random() * 100 < player.critch:
            damage *= 2
            self.fight_log.append("НЕВЕРОЯТНЫЙ КРИТИЧЕСКИЙ УДАР!")

        actual_damage = self.enemy.take_damage(damage)
        self.fight_log.append(f"Ты наносишь {actual_damage} урона мощной атакой!")

        if not self.enemy.is_alive():
            self.end_fight(victory=True)
            return True

        self.player_turn = False
        return True

    def player_block(self):
        """Блок - урезает урон и может нанести контрудар"""
        if not self.fight_active or not self.player_turn:
            return False

        self.fight_log.append("Ты принимаешь оборонительную стойку")
        self.player_turn = False
        return True

    def player_counter(self):
        """Контратака - шанс увернуться и нанести урон"""
        if not self.fight_active or not self.player_turn:
            return False

        if random.random() < 0.4:  # 40% шанс
            damage = random.randint(2, 3)
            actual_damage = self.enemy.take_damage(damage)
            self.fight_log.append(f"Контратака удалась! Ты наносишь {actual_damage} урона")

            if not self.enemy.is_alive():
                self.end_fight(victory=True)
                return True
        else:
            self.fight_log.append("Контратака не удалась")

        self.player_turn = False
        return True

    def player_flee(self):
        """Попытка сбежать из боя"""
        if not self.fight_active or not self.player_turn:
            return False

        if random.random() < 0.2:  # 20% шанс
            self.fight_log.append("Тебе удалось сбежать!")
            self.end_fight(victory=False, fled=True)
            return True
        else:
            self.fight_log.append("Побег не удался!")
            self.player_turn = False
            return True

    def enemy_turn(self):
        """Ход врага"""
        if not self.fight_active or self.player_turn:
            return

        damage = self.enemy.damage

        # Проверяем, был ли блок на прошлом ходу
        if len(self.fight_log) > 0 and "оборонительную стойку" in self.fight_log[-1]:
            if random.random() < 0.2:  # 20% шанс ошибки при блоке
                self.fight_log.append("Блок не удался!")
            else:
                damage //= 2
                self.fight_log.append("Блок частично поглотил урон!")

                # 50% шанс контрудара при блоке
                if random.random() < 0.5:
                    counter_damage = self.enemy.take_damage(1)
                    self.fight_log.append(f"Контрудар! Враг получает {counter_damage} урона")
                    if not self.enemy.is_alive():
                        self.end_fight(victory=True)
                        return

        # Наносим урон игроку
        actual_damage = max(1, damage - player.armor)
        player.health -= actual_damage
        health = player.health
        self.fight_log.append(f"{self.enemy.name} наносит тебе {actual_damage} урона, у тебя {health} здоровья")


        if player.health <= 0:
            self.end_fight(victory=False)
            return

        self.player_turn = True

    def end_fight(self, victory: bool, fled: bool = False):
        """Заканчивает бой"""
        self.fight_active = False

        if fled:
            self.fight_log.append("Ты сбежала из боя!")
        elif victory:
            # Награды за победу
            exp_reward = self.enemy.level * 10
            gold_reward = random.randint(10, 30) * self.enemy.level

            player.money += gold_reward
            self.fight_log.append(f"Победа! Ты получаешь {gold_reward} монет")

            # Шанс на предмет
            if random.random() < 0.3:
                items = [
                    Potion("Зелье здоровья"),
                    Weapon(f"Оружие ур.{self.enemy.level}",),
                    Armor(f"Броня ур.{self.enemy.level}")
                ]
                item = random.choice(items)
                self.fight_log.append(f"Ты находишь {item.name}!")
        else:
            self.fight_log.append("Поражение... Ты теряешь сознание")
            # При поражении восстанавливаем немного здоровья и телепортируем в начало
            player.health = max(1, player.maxhealth // 4)



class WorldView(arcade.View):
    def __init__(self, game_window):
        super().__init__()
        self.game_window = game_window
        self.world = World2D()
        self.fight_system = FightSystem()
        self.event_system = EventSystem()
        self.player = player
        # UI менеджер для кнопок боя
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Клавиши управления
        self.keys_pressed = set()

        # Состояние просмотра мира
        self.in_fight = False
        self.in_event = False
        self.current_location = None

        # Настройка UI боя
        self.setup_fight_ui()
        self.setup_event_ui()

    # Обработчики кнопок боя # Разве это нельзя вписать напрямую в setup_fight_ui?
    def on_attack_click(self, event):
        if self.fight_system.player_turn:
            self.fight_system.player_attack()

    def on_power_attack_click(self, event):
        if self.fight_system.player_turn:
            self.fight_system.player_power_attack()

    def on_block_click(self, event):
        if self.fight_system.player_turn:
            self.fight_system.player_block()

    def on_counter_click(self, event):
        if self.fight_system.player_turn:
            self.fight_system.player_counter()

    def on_flee_click(self, event):
        if self.fight_system.player_turn:
            self.fight_system.player_flee()
    def on_continue_click (self, event):
        if self.in_event:
            pass ###ДОПИСАТЬ КНОПКУ ИВЕНТА!!!

    def setup_fight_ui(self):
        """Настройка UI для боевой системы"""
        # Создаем панель кнопок боя
        self.fight_panel = arcade.gui.UIBoxLayout(vertical=True, space_between=10)

        # Получаем дефолтный стиль и модифицируем его
        default_style = arcade.gui.UIFlatButton.DEFAULT_STYLE

        # Создаем кнопки с дефолтным стилем
        self.attack_button = arcade.gui.UIFlatButton(
            text="Атака", width=100, height=35, style=default_style
        )
        self.attack_button.on_click = self.on_attack_click

        self.power_attack_button = arcade.gui.UIFlatButton(
            text="Мощная атака", width=100, height=35, style=default_style
        )
        self.power_attack_button.on_click = self.on_power_attack_click

        self.block_button = arcade.gui.UIFlatButton(
            text="Блок", width=100, height=35, style=default_style
        )
        self.block_button.on_click = self.on_block_click

        self.counter_button = arcade.gui.UIFlatButton(
            text="Контратака", width=100, height=35, style=default_style
        )
        self.counter_button.on_click = self.on_counter_click

        self.flee_button = arcade.gui.UIFlatButton(
            text="Побег", width=100, height=35, style=default_style
        )
        self.flee_button.on_click = self.on_flee_click

        # Добавляем кнопки в панель
        self.fight_panel.add(self.attack_button)
        self.fight_panel.add(self.power_attack_button)
        self.fight_panel.add(self.block_button)
        self.fight_panel.add(self.counter_button)
        self.fight_panel.add(self.flee_button)

        # Позиционируем панель
        self.fight_anchor = arcade.gui.UIAnchorLayout(
            anchor_x="right",
            anchor_y="center",
            align_x=-20,
            child=self.fight_panel
        )

        self.manager.add(self.fight_anchor)
        self.fight_anchor.visible = False

    def setup_event_ui(self):
        """Настройка UI для событий"""
        self.event_panel = arcade.gui.UIBoxLayout(vertical=True, space_between=10)

        # Создаем кнопку продолжить
        self.continue_button = arcade.gui.UIFlatButton(
            text="Продолжить", width=100, height=35
        )
        self.continue_button.on_click = self.on_continue_click

        self.event_panel.add(self.continue_button)

        # Создаем якорь с правильной панелью
        self.event_anchor = arcade.gui.UIAnchorLayout(
            anchor_x="right",
            anchor_y="center",
            align_x=-20,
            child=self.event_panel
        )

        # Добавляем в тот же менеджер
        self.manager.add(self.event_anchor)
        self.event_anchor.visible = False

    def on_draw(self):
        self.clear()

        # Вычисляем смещение камеры
        camera_x = self.world.player_x - self.window.width // 2
        camera_y = self.world.player_y - self.window.height // 2

        # Рисуем фон
        arcade.draw_lbwh_rectangle_filled(
            0, 0,  # left, bottom
            self.window.width, self.window.height,  # width, height
            arcade.color.DARK_GREEN
        )

        # Рисуем локации
        for location in self.world.locations:
            screen_x = location.x - camera_x
            screen_y = location.y - camera_y

            # Рисуем только видимые локации
            if (-50 <= screen_x <= self.window.width + 50 and
                    -50 <= screen_y <= self.window.height + 50):

                if location.discovered:
                    color = location.get_sprite_color()
                    if location.completed:
                        color = tuple(c // 2 for c in color)  # Затемняем завершенные

                    arcade.draw_circle_filled(screen_x, screen_y, 15, color)
                    arcade.draw_text(location.name, screen_x - 40, screen_y + 20,
                                     arcade.color.WHITE, 10, anchor_x="center")
                else:
                    # Неоткрытые локации рисуем как серые точки
                    arcade.draw_circle_filled(screen_x, screen_y, 8, arcade.color.GRAY)

        # Рисуем игрока
        player_screen_x = self.world.player_x - camera_x
        player_screen_y = self.world.player_y - camera_y
        arcade.draw_circle_filled(player_screen_x, player_screen_y, 10, arcade.color.BLUE)

        # Рисуем информацию о ближайшей локации
        nearby = self.world.get_nearby_location(30)
        if nearby and nearby.discovered:
            arcade.draw_text(f"[E] {nearby.name}", 10, self.window.height - 30,
                             arcade.color.YELLOW, 14)
            arcade.draw_text(nearby.description, 10, self.window.height - 50,
                             arcade.color.WHITE, 12)

        # Рисуем UI боя если активен
        if self.in_fight:
            self.draw_fight_ui()

        if self.in_event:
            self.draw_event_ui()

        # Рисуем миникарту
        self.draw_minimap()

        # UI элементы
        self.manager.draw()

    def draw_fight_ui(self):
        """Рисует интерфейс боя"""
        if not self.fight_system.fight_active:
            return

        # Панель боя
        fight_panel_width = 400
        fight_panel_height = 300
        panel_x = self.window.width // 2
        panel_y = self.window.height // 2

        panel_left = panel_x - fight_panel_width // 2
        panel_bottom = panel_y - fight_panel_height // 2

        # Фон панели
        arcade.draw_lbwh_rectangle_filled(
            panel_left, panel_bottom,
            fight_panel_width, fight_panel_height,
            (0, 0, 0, 150)  # Black with alpha 150
        )
        # Контур прямоугольника
        arcade.draw_lbwh_rectangle_outline(
            panel_left, panel_bottom,
            fight_panel_width, fight_panel_height,
            arcade.color.WHITE, 2
        )

        # Информация о враге
        enemy = self.fight_system.enemy
        if enemy:
            y_offset = panel_y + 100
            arcade.draw_text(f"Враг: {enemy.name} (Ур.{enemy.level})",
                             panel_x, y_offset, arcade.color.RED, 16, anchor_x="center")

            arcade.draw_text(f"Здоровье: {enemy.health}/{enemy.max_health}",
                             panel_x, y_offset - 25, arcade.color.WHITE, 14, anchor_x="center")

            arcade.draw_text(f"Урон: {enemy.damage} | Броня: {enemy.armor}",
                             panel_x, y_offset - 45, arcade.color.WHITE, 12, anchor_x="center")

        # Лог боя
        log_y = panel_y - 20
        for i, log_entry in enumerate(self.fight_system.fight_log[-4:]):
            arcade.draw_text(log_entry, panel_x, log_y - i * 20,
                             arcade.color.YELLOW, 10, anchor_x="center")

        # Индикатор хода
        turn_text = "Твой ход" if self.fight_system.player_turn else "Ход врага"
        turn_color = arcade.color.GREEN if self.fight_system.player_turn else arcade.color.RED
        arcade.draw_text(turn_text, panel_x, panel_y - 120,
                         turn_color, 14, anchor_x="center")

    def draw_event_ui(self):
        """Рисует интерфейс боя"""
        if not self.event_system.event_active:
            return

        # Панель ивента
        fight_panel_width = 400
        fight_panel_height = 300
        panel_x = self.window.width // 2
        panel_y = self.window.height // 2

        panel_left = panel_x - fight_panel_width // 2
        panel_bottom = panel_y - fight_panel_height // 2

        # Фон панели
        arcade.draw_lbwh_rectangle_filled(
            panel_left, panel_bottom,
            fight_panel_width, fight_panel_height,
            (0, 0, 0, 150)  # Black with alpha 150
        )
        # Контур прямоугольника
        arcade.draw_lbwh_rectangle_outline(
            panel_left, panel_bottom,
            fight_panel_width, fight_panel_height,
            arcade.color.WHITE, 2
        )

        # Вводное описание ивента
        event = self.event_system.event
        if event:
            y_offset = panel_y + 100
            arcade.draw_text("1",
                             panel_x, y_offset, arcade.color.RED, 16, anchor_x="center")
        # Лог боя
        # log_y = panel_y - 20
        # for i, log_entry in enumerate(self.event_system.event_log[-4:]):
        #     arcade.draw_text(log_entry, panel_x, log_y - i * 20,
        #                      arcade.color.YELLOW, 10, anchor_x="center")

    def draw_minimap(self):
        """Рисует миникарту в правом верхнем углу"""
        minimap_size = 150
        minimap_x = self.window.width - minimap_size // 2 - 10
        minimap_y = self.window.height - minimap_size // 2 - 10

        minimap_left = minimap_x - minimap_size // 2
        minimap_bottom = minimap_y - minimap_size // 2

        # Закрашенный прямоугольник
        arcade.draw_lbwh_rectangle_filled(
            minimap_left, minimap_bottom,
            minimap_size, minimap_size,
            (0, 0, 0, 150)  # Black with alpha 150
        )

        # Контур прямоугольника
        arcade.draw_lbwh_rectangle_outline(
            minimap_left, minimap_bottom,
            minimap_size, minimap_size,
            arcade.color.WHITE, 1
        )

        # Масштаб миникарты
        scale_x = minimap_size / self.world.width
        scale_y = minimap_size / self.world.height

        # Рисуем локации на миникарте
        for location in self.world.locations:
            if location.discovered:
                mini_x = minimap_x - minimap_size // 2 + location.x * scale_x
                mini_y = minimap_y - minimap_size // 2 + location.y * scale_y

                color = location.get_sprite_color()
                if location.completed:
                    color = tuple(c // 2 for c in color)

                arcade.draw_circle_filled(mini_x, mini_y, 2, color)

        # Рисуем игрока на миникарте
        player_mini_x = minimap_x - minimap_size // 2 + self.world.player_x * scale_x
        player_mini_y = minimap_y - minimap_size // 2 + self.world.player_y * scale_y
        arcade.draw_circle_filled(player_mini_x, player_mini_y, 3, arcade.color.BLUE)

    def on_update(self, delta_time):
        # Обработка движения
        dx = dy = 0
        if arcade.key.W in self.keys_pressed or arcade.key.UP in self.keys_pressed:
            dy = 1
        if arcade.key.S in self.keys_pressed or arcade.key.DOWN in self.keys_pressed:
            dy = -1
        if arcade.key.A in self.keys_pressed or arcade.key.LEFT in self.keys_pressed:
            dx = -1
        if arcade.key.D in self.keys_pressed or arcade.key.RIGHT in self.keys_pressed:
            dx = 1

        if not self.in_fight and (dx != 0 or dy != 0):
            self.world.move_player(dx, dy)
            self.world.discover_nearby_locations()

        # Обработка хода врага в бою
        if (self.in_fight and self.fight_system.fight_active and
                not self.fight_system.player_turn):
            self.fight_system.enemy_turn()

        # Проверяем, закончился ли бой
        if self.in_fight and not self.fight_system.fight_active:
            self.end_fight()

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)

        # Взаимодействие с локациями
        if key == arcade.key.E and not self.in_fight:
            self.interact_with_location()

        # Выход из боя (для тестирования)
        if key == arcade.key.ESCAPE and self.in_fight:
            self.end_fight()

    def on_key_release(self, key, modifiers):
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)

    def interact_with_location(self):
        """Взаимодействие с ближайшей локацией"""
        nearby = self.world.get_nearby_location(30)
        if not nearby or not nearby.discovered:
            return

        self.current_location = nearby

        if nearby.event_type == EventType.FIGHT:
            self.start_fight()
        elif nearby.event_type == EventType.BOSS_FIGHT:
            self.start_fight()
        elif nearby.event_type == EventType.HEALING:
            self.handle_healing(nearby)
        elif nearby.event_type == EventType.TREASURE:
            self.handle_treasure(nearby)
        elif nearby.event_type == EventType.SHOP:
            self.handle_shop(nearby)

        nearby.completed = True

    def start_fight(self, leveldefined = False):        #Дописать конструктор определнного уровня
        """Начинает бой"""
        self.in_fight = True
        self.fight_anchor.visible = True
        self.fight_system.start_fight()

        # Останавливаем фоновую музыку и включаем боевую
        if hasattr(self.game_window, 'play_music'):
            self.game_window.play_music("epic")

    def end_fight(self):
        """Заканчивает бой"""
        self.in_fight = False
        self.fight_anchor.visible = False

        # Возвращаем фоновую музыку
        if hasattr(self.game_window, 'play_music'):
            self.game_window.play_music("ambient")

    def end_event(self):
        self.in_event = False
        self.event_anchor.visible = False
        if hasattr(self.game_window, 'play_music'):
            self.game_window.play_music("ambient")

    def starthandle_healing(self, location):
        """Обрабатывает событие исцеления"""
        heal_amount = random.randint(30, 50)
        old_health = player.health
        player.health = min(player.maxhealth,
                                      player.health + heal_amount)
        actual_heal = player.health - old_health

        self.game_window.narrative_text.append(
            f"Ты восстанавливаешь {actual_heal} здоровья в {location.name}"
        )

    def start_handle_treasure(self, location):
        pass


    def start_handle_shop(self, location):
        """Обрабатывает событие магазина"""
        # Здесь можно добавить полноценный интерфейс магазина
        self.game_window.narrative_text.append(f"Добро пожаловать в {location.name}!")

        # Простой автоматический магазин для примера
        if player.money >= 50:
            choice = random.choice(["health", "weapon", "armor"])
            if choice == "health":
                potion = Potion()
                self.game_window.inventory.append(potion)
                player.money -= 50
                self.game_window.narrative_text.append("Ты покупаешь зелье за 50 золота")
            elif choice == "weapon":
                weapon = Weapon()
                self.game_window.inventory.append(weapon)
                player.money -= 50
                self.game_window.narrative_text.append("Ты покупаешь оружие за 50 золота")
            else:
                armor = Armor()
                self.game_window.inventory.append(armor)
                player.money -= 50
                self.game_window.narrative_text.append("Ты покупаешь броню за 50 золота")
        else:
            self.game_window.narrative_text.append("У тебя недостаточно золота для покупок")




# Дополнительные классы для интеграции с основной игрой
class WorldManager:
    def __init__(self, main_game):
        self.main_game = main_game

    def enter_world_mode(self):
        """Переход в режим 2D мира"""
        if not self.main_game.world_view:
            self.main_game.world_view = WorldView(self.main_game)

        self.main_game.in_world_mode = True
        self.main_game.manager.disable()
        self.main_game.window.show_view(self.main_game.world_view)

        if hasattr(self.main_game, 'play_music'):
            self.main_game.play_music("ambient")

    def exit_world_mode(self):
        """Возврат к текстовой игре"""
        self.main_game.in_world_mode = False

        # Включаем обратно UI менеджер
        self.main_game.manager.enable()
    def sync_stats(self):
        """Синхронизация статистик между режимами"""
        if self.world_view and self.world_view.fight_system:
            # Синхронизируем здоровье, деньги, инвентарь и т.д.
            pass


# Пример интеграции с основным файлом
class WorldIntegratedGame(arcade.View):
    """Расширенная версия основной игры с интеграцией 2D мира"""

    def __init__(self, original_game):
        super().__init__()
        self.original_game = original_game
        self.world_manager = WorldManager(original_game)

        # Добавляем кнопку для входа в мир
        self.setup_world_button()

    def setup_world_button(self):
        """Настройка кнопки входа в мир"""
        world_button = arcade.gui.UIFlatButton(
            text="Исследовать мир",
            width=150,
            height=40,
            style={
                "font_name": ("calibri", "arial"),
                "font_size": 12,
                "font_color": arcade.color.WHITE,
                "border_width": 2,
                "border_color": arcade.color.WHITE,
                "bg_color": arcade.color.DARK_GREEN,
                "bg_color_pressed": arcade.color.GREEN,
            }
        )
        world_button.on_click = self.on_world_button_click

        # Добавляем кнопку в UI менеджер основной игры
        world_anchor = arcade.gui.UIAnchorLayout(
            anchor_x="left",
            anchor_y="bottom",
            align_x=20,
            align_y=20,
            child=world_button
        )

        if hasattr(self.original_game, 'manager'):
            self.original_game.manager.add(world_anchor)

    def on_world_button_click(self, event):
        """Обработчик кнопки входа в мир"""
        self.world_manager.enter_world_mode()