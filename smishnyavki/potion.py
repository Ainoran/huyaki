import random as r

class Potion:
    def __init__(self, name = "Зельe здоровья"):
        self.name = name
        self.heal_amount = r.randint(20, 40)

    def use(self, game, player):
        player.health = min(player.maxhealth, player.health + self.heal_amount)
        game.narrative_text.append(f"Использовано {self.name}: восстановлено {self.heal_amount} здоровья")

    def __str__(self):
        return f"{self.name} (Лечение: {self.heal_amount})"

    def gener(self):
        pass