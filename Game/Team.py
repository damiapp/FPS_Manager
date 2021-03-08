from Player import Player
import statistics 
import random
class Team:
    def __init__(self, players, unity, map_skill, expenses, strat):
        self.players = players
        self.unity=unity
        data = 0
        for p in players:
            data = p.map_skill + data
        self.map_skill=data/7
        self.expenses=expenses #todo
        self.strat=strat #todo
    def print_team(self):
        for p in self.players:
            print(p.name)
        
    def reset_alive(self):
        for p in self.players:
            p.set_alive(True)

    def get_rand(self):
        r=random.randint(0,4)
        while not self.players[r].alive:
            r=random.randint(0,4)
        return self.players[r]
