class Armor:
    def __init__(self, name, armor_value):
        self.name = name
        self.armor_value = armor_value

    def use(self, game):
        game.armor = self.armor_value
        game.narrative_text.append(f"Экипирована {self.name}: броня теперь {self.armor_value}")

    def __str__(self):
        return f"{self.name} (Броня: {self.armor_value})"