import random as r


class Armor:
    def __init__(self, name = 'ARMORTEST'):
        self.name = name
        self.armor_value = r.randint(1, 3)

    def use(self, game, player):
        player.armor = self.armor_value
        game.narrative_text.append(f"Экипирована {self.name}: броня теперь {self.armor_value}")

    def __str__(self):
        return f"{self.name} (Броня: {self.armor_value})"

    def gener(self):
        pass