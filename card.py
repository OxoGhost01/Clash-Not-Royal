from utils import *

class Card:
    def __init__(self, name, attack, defense, health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health

    def __str__(self):
        return f"{self.name} - ATK: {self.attack}, DEF: {self.defense}, PV: {self.health}"
    
    def attack_target(self, target):
        print(f"{self.name} attacks {target.name}")
        if self.attack - target.defense > 0:
            if target.health - (self.attack - target.defense) < 0: 
                target.health = 0
            else:
                target.health -= self.attack - target.defense
