from playerdata import player
import random as r

class Enemy():
    def __init__(self,name='empty', health=0, damage=0, level=1, armor=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.level = level
        self.max_health = health
        self.armor =  self.level/2
        if self.level <= 0:
            self.level = 1
    def generate(self):
        self.level = player.lvl + r.randint(-2, 0)
        self.enemy_types = {
            1: [("Волк", 15, 3), ("Гоблин", 12, 4), ("Слизень", 10, 2)],
            2: [("Орк", 25, 6), ("Скелет", 20, 5), ("Медведь", 30, 7)],
            3: [("Огр", 40, 10), ("Призрак", 35, 8), ("Тролль", 45, 9)],
            4: [("Дракончик", 60, 12), ("Демон", 55, 14), ("Голем", 70, 10)],
            5: [("Древний Дракон", 100, 20), ("Король Личей", 90, 18), ("Титан", 120, 16)]
        }
        enemy_data = r.choice(self.enemy_types[self.level])
        print(self.level)
        self.name = enemy_data[0]
        self.health = enemy_data[1]
        self.damage = enemy_data[2]

    def take_damage(self, damage: int) -> int:
        actual_damage = max(1, damage - player.armor)
        self.health -= actual_damage
        return actual_damage

    def is_alive(self) -> bool:
        return self.health > 0