import pygame
from lab11.turn_combat import ComputerCombatPlayer

""" Create PyGameAIPlayer class here"""


class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        city = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0],[9, 0]]

        for i in range(city):
            if city[i][1] == 0:
                city[i][1] = 1
                return str(city[i][0])

        

        return ord(str(state.current_city))  # Not a safe operation for >10 cities


""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer(ComputerCombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        choice = 3
        self.weapon = choice - 1
        return self.weapon
