import random
import itertools
from collections import defaultdict, deque
from turn_combat import CombatPlayer,ComputerCombatPlayer

class PyGameAIPlayer:
    def __init__(self):
        self.path = []
        self.path_index = 0

class PyGameAIPlayer:
    def __init__(self):
            self.path = []
            self.path_index = 0
 
    def selectAction(self, state):
        current_city = state.current_city
        destination_city = state.destination_city
        routes = state.routes
        
        # Find the routes from the current city
        valid_routes = [i for i, r in enumerate(routes) if r[0] == current_city]
        
        # If no valid routes, return a random action 
        if not valid_routes:
            return random.randint(48, 57)
        
        # Find the neighboring cities
        neighbors = [r[1] for i, r in enumerate(routes) if i in valid_routes]
        
        # If the player is traveling, return the current destination
        if state.travelling:
            return str(destination_city).encode()[0]
        
        # Otherwise, select a random neighbor as the destination city
        destination_city = random.choice(neighbors)
        route_index = valid_routes[neighbors.index(destination_city)]
        
        # Return the index of the selected route as the action
        return str(route_index).encode()[0]


class PyGameAICombatPlayer(ComputerCombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        if 30 < self.health <= 50:
            self.weapon = 0
        elif self.health <= 30:
            self.weapon = 2
        else:
            self.weapon = 1
        return self.weapon