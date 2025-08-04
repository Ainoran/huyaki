import random as r
from playerdata import player
class Weapon:
    def __init__(self, weapontype='melee', lvl=1, rarity = 0, name='emty', damage=0, crit=0, critmodifier=0,
                 speed = 0.1, cost=0, ib=0, ha = 0):
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

    weapontypes = ['melee','longmelee', 'range', 'magic', 'specific', 'differentive']
    def genermelee(self):
        weaponsnames = ['Кортик', "Кинжал", "Стилет", 'Нож', 'Топор']
        weaponrars = ['Дряхлый', "Простой", 'Прочный', 'Эпический', 'Легенадрный', 'Уникальный']

        self.name = r.choice(weaponsnames)
        self.lvl = player.lvl + r.randint(0, 3)
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
        
        self.name = r.choice(weaponsnames)
        self.lvl = player.lvl + r.randint(0, 3)
        if self.lvl <= 0:
            self.lvl = 1
        elif self.lvl > 11:
            self.lvl = 11
        self.rarity = r.randint(0, 5)
        self.damage = player.lvl * 0.8 + self.lvl * (r.randint(6, 12) / 2)
        self.crit = r.randint(8, 15) / 100 + self.lvl * 0.015
        self.crithmodifier = 2.5
        self.attackspeed = 60
        self.cost = self.damage * 3 + self.crit * 100 + self.attackspeed * 2
        self.isbought = 0
        if self.rarity >= 3:
            self.haveanability = 1
        else:
            self.haveanability = 0
    def generrange(self):
        weaponsnames = ['Лук', "Арбалет", "Куча камней", 'SIG Sauer M7', 'Рогатка']
        
        self.name = r.choice(weaponsnames)
        self.lvl = player.lvl + r.randint(0, 3)
        if self.lvl <= 0:
            self.lvl = 1
        elif self.lvl > 11:
            self.lvl = 11
        self.rarity = r.randint(0, 5)
        self.damage = player.lvl * 0.6 + self.lvl * (r.randint(5, 10) / 2)
        self.crit = r.randint(15, 25) / 100 + self.lvl * 0.025
        self.crithmodifier = 3.5
        self.attackspeed = 70
        self.cost = self.damage * 3 + self.crit * 100 + self.attackspeed * 2
        self.isbought = 0
        if self.rarity >= 3:
            self.haveanability = 1
        else:
            self.haveanability = 0
    def genermagic(self):
        weaponsnames = ['Шар из фольги', "Некрономикон", "Астральный вестник", 'Какая-то необычная палка']
        
        self.name = r.choice(weaponsnames)
        self.lvl = player.lvl + r.randint(0, 3)
        if self.lvl <= 0:
            self.lvl = 1
        elif self.lvl > 11:
            self.lvl = 11
        self.rarity = r.randint(0, 5)
        self.damage = player.lvl * 0.7 + self.lvl * (r.randint(7, 15) / 2)
        self.crit = r.randint(12, 22) / 100 + self.lvl * 0.03
        self.crithmodifier = 4.0
        self.attackspeed = 50
        self.cost = self.damage * 3 + self.crit * 100 + self.attackspeed * 2
        self.isbought = 0
        if self.rarity >= 3:
            self.haveanability = 1
        else:
            self.haveanability = 0
    def generspecific(self):
        weaponsnames = ['Гусь', "Сковорода", "Лютня"]
        
        self.name = r.choice(weaponsnames)
        self.lvl = player.lvl + r.randint(0, 3)
        if self.lvl <= 0:
            self.lvl = 1
        elif self.lvl > 11:
            self.lvl = 11
        self.rarity = r.randint(0, 5)
        self.damage = player.lvl * 0.4 + self.lvl * (r.randint(3, 8) / 2)
        self.crit = r.randint(5, 15) / 100 + self.lvl * 0.01
        self.crithmodifier = 2.0
        self.attackspeed = 90
        self.cost = self.damage * 3 + self.crit * 100 + self.attackspeed * 2
        self.isbought = 0
        if self.rarity >= 3:
            self.haveanability = 1
        else:
            self.haveanability = 0
    def generdifferantive(self):
        weaponsnames = ['Телефон', "Фростморн", 'Перцовый баллончик', 'Утюг с углями']
        
        self.name = r.choice(weaponsnames)
        self.lvl = player.lvl + r.randint(0, 3)
        if self.lvl <= 0:
            self.lvl = 1
        elif self.lvl > 11:
            self.lvl = 11
        self.rarity = r.randint(0, 5)
        self.damage = player.lvl * 0.9 + self.lvl * (r.randint(8, 16) / 2)
        self.crit = r.randint(18, 30) / 100 + self.lvl * 0.035
        self.crithmodifier = 4.5
        self.attackspeed = 40
        self.cost = self.damage * 3 + self.crit * 100 + self.attackspeed * 2
        self.isbought = 0
        if self.rarity >= 3:
            self.haveanability = 1
        else:
            self.haveanability = 0

    def generate(self):
        if self.weapontype == 'melee':
            self.genermelee()
        elif self.weapontype == 'longmelee':
            self.generlongmelee()
        elif self.weapontype == 'range':
            self.generrange()
        elif self.weapontype == 'magic':
            self.genermagic()
        elif self.weapontype == 'specific':
            self.generspecific()
        elif self.weapontype == 'differentive':
            self.generdifferantive()
        else:
            # По умолчанию генерируем ближнее оружие
            self.weapontype = 'melee'
            self.genermelee()



    def use(self, game, player):
        player.damage = self.damage
        game.narrative_text.append(f"Экипировано {self.name}: урон теперь {self.damage}")



    def __str__(self):
        rarity_names = ['Дряхлый', 'Простой', 'Прочный', 'Эпический', 'Легендарный', 'Уникальный']
        rarity_name = rarity_names[self.rarity] if self.rarity < len(rarity_names) else 'Неизвестный'
        return f"{rarity_name} {self.name} (Урон: {self.damage:.1f}, Крит: {self.crit*100:.1f}%, Скорость: {self.attackspeed})"