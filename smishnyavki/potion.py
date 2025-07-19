class Potion:
    def __init__(self, name, heal_amount):
        self.name = name
        self.heal_amount = heal_amount

    def use(self, game):
        game.health = min(game.maxhealth, game.health + self.heal_amount)
        game.narrative_text.append(f"Использовано {self.name}: восстановлено {self.heal_amount} здоровья")

    def __str__(self):
        return f"{self.name} (Лечение: {self.heal_amount})"
