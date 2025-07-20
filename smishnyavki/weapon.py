import random as r
from player import Player, player

class Weapon:
    def __init__(self, weapontype='melee', lvl=1, rarity = 0, name='emty', damage=0, crit=0, critmodifier=0, speed = 0.1, cost=0, ib=0, ha = 0):
        self.weapontype = weapontype
        self.lvl = lvl
        self.rarity = rarity
        self.name = name
        self.damage = damage
        self.crit = crit
        self.crithmodifier = critmodifier
        self.attackspeed = speed
        self.cost = cost
        self.isbought = ib
        self.haveanability = ha

    weaponrarsnames = ['Дряхлый', "Простой", 'Прочный']
    weapontypes = ['melee','longmelee', 'range', 'magic', 'specific', 'differentive']
    def genermelee(self):
        weaponsnames = ['Кортик', "Кинжал", "Стилет", 'Нож', 'Топор']
        weaponrars = ['Дряхлый', "Простой", 'Прочный', 'Эпический', 'Легенадрный', 'Уникальный']

        self.name = r.choice(weaponsnames)
        self.lvl = player.level + r.randint(-2, 3)
        if self.lvl <= 0:
            self.lvl = 1
        elif self.lvl >11:
            self.lvl = 11
        self.rarity = r.randint(0, 5)
        self.damage = player.lvl*0.5+self.lvl*(r.randint(4,8)/2)
        self.crit = r.randint(10,20)/100 + self.lvl*0.02
        self.crithmodifier = 3
        self.attackspeed = 80
        self.cost = self.damage *3 +self.crit*100+self.attackspeed*2
        self.isbought = 0
        if self.rarity>=3:
            self.haveanability = 1
        else:
            self.haveanability = 0



    def generlongmelee(self):
        weaponsnames = ['Цвайхендер', "Доска для серфинга", "Копьё", 'Чья-то оторванная нога', 'Булава']












        pass
    def generrange(self):
        weaponsnames = ['Лук', "Арбалет", "Куча камней", 'SIG Sauer M7', 'Рогатка']









        pass
    def genermagic(self):
        weaponsnames = ['Шар из фольги', "Некрономикон", "Астральный вестник", 'Какая-то необычная палка']













        pass
    def generspecific(self):
        weaponsnames = ['Гусь', "Сковорода", "Лютня"]










        pass
    def generdifferantive(self):
        weaponsnames = ['Телефон', "Фростморн", 'Перцовый баллончик', 'Утюг с углями']










        pass





    def use(self, game):
        game.damage = self.damage
        game.narrative_text.append(f"Экипировано {self.name}: урон теперь {self.damage}")
    def __str__(self):
        return f"{self.name} (Урон: {self.damage})"