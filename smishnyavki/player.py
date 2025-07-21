class Player():
    def __init__(self, name='', lvl=1, damage=2, hp=10, armor = 0, money = 100, critch = 10, maxhealth = 25):
        self.name = name
        self.lvl = lvl
        self.damage = damage
        self.health = hp
        self.armor = armor
        self.money = money
        self.critch = critch
        self.maxhealth = maxhealth

player = Player('Oleg', lvl=3)