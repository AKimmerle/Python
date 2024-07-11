# mage.py
from Character import Character

class Mage(Character):
     
    def Firebolt(self, other):
        damage = 15
        other.health -= damage
        print(f"{self.name} casts Firebolt on {other.name} for {damage} damage.")

    def Icebolt(self, other):
        damage = 15
        other.health -= damage
        print(f"{self.name} casts Icebolt on {other.name} for {damage} damage.")
    
    def Fireball(self, other):
        damage = 35
        other.health -= damage
        action = "casts Fireball"
        print(f"{self.name} {action} on {other.name} for {damage} damage.")

    def Iceshard(self, other):
        damage = 30
        other.health -= damage
        action = "casts Iceshard" 
        print(f"{self.name} {action} on {other.name} for {damage} damage.")

    def Health_Potion(self, other):
        if self.health < 150:
            heal = 40
            self.health += heal
            print(f"{self.name} uses an Health Potion to heal himself. He gains {heal} health.")

    
