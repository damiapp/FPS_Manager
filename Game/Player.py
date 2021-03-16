import statistics 
import random
class Player:
    def __init__(self, talent, map_skill, weapon_skill, utility_usage, game_sense, communication, mood, motivation, alive, nationality, name, surname, age, cost):
        self.talent = talent
        self.map_skill = map_skill
        self.weapon_skill = weapon_skill
        self.utility_usage = utility_usage
        self.game_sense = game_sense
        self.communication = communication
        self.mood = mood
        self.motivation = motivation
        self.alive=True
        self.nationality = nationality
        self.name = name
        self.surname = surname
        self.age = age
        self.cost = cost
    def get_m_w(self):
        data=[self.talent, self.map_skill, self.weapon_skill]
        d1=statistics.mean(data)
        data=[self.utility_usage, self.game_sense, self.communication]
        d2=statistics.mean(data)
        data=[self.mood, self.motivation]
        d3=statistics.mean(data)
        w1=random.uniform(0.8,1)
        w2=random.uniform(0.8,1)
        w3=random.uniform(0.9,1)
        return d1*w1+d2*w2+d3*w3
    def set_alive(self,alive):
        self.alive = alive