# villan.py
from Character import Character

class Villan(Character):
    def Shadowbolt(self, other):
        damage = 20
        other.health -= damage
        print(f"{self.name} casts Shadowbolt, dealing {damage} damage to {other.name}.")
   
       
    def Dark_Pulse(self, other):
        damage = 15
        other.health -= damage
        print(f"{self.name} casts Dark Pulse, dealing {damage} damage to {other.name}.")
   
    def ShadowClaw(self,other):
        damage = 30
        other.health -= damage
        print(f"{self.name} casts ShadowClaw, dealing {damage} damage to {other.name}.")
   
