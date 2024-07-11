# character.py
class Character:
    def __init__(self, name, health, max_health):
        self.name = name
        self.health = health
        self.max_health = max_health
    def attack(self, other):
        raise NotImplementedError("Subclasses must implement this method.")