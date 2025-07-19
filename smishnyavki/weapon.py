class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def use(self, game):
        game.damage = self.damage
        game.narrative_text.append(f"Экипировано {self.name}: урон теперь {self.damage}")

    def __str__(self):
        return f"{self.name} (Урон: {self.damage})"