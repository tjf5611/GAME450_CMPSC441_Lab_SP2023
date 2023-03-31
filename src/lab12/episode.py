''' 
Lab 12: Beginnings of Reinforcement Learning
We will modularize the code in pygame_combat.py from lab 11 together.

Then it's your turn!
Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''

import sys
import pygame
from pathlib import Path
from lab11.pygame_combat import run_turn, draw_combat_on_window, PyGameComputerCombatPlayer
from lab11.turn_combat import CombatPlayer, Combat

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))


def run_episode(player1, player2):
    episode = []
    player1 = CombatPlayer("Player 1")
    player2 = CombatPlayer("Player 2")
    currentGame = Combat()
    observation = (player1.health, player2.health)
    action = PyGameComputerCombatPlayer.weapon_selecting_strategy(player1)

    reward = run_turn(currentGame, player1, player2)

    turn = (observation, action, reward)

    episode.append(turn)

    return episode