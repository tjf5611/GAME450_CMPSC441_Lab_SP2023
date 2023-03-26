import pygame
import random
from lab11.turn_combat import ComputerCombatPlayer

""" Create PyGameAIPlayer class here"""


class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        city = random.randint(0,9)
        city = str(city)
        return ord(city)




""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer(ComputerCombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        choice = 3
        self.weapon = choice - 1
        return self.weapon