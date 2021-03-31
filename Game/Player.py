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
        return (self.talent*(self.map_skill + self.weapon_skill + self.utility_usage)*self.game_sense*random.uniform(0.8,1.1) \
            + self.communication*random.uniform(0.9,1))*random.uniform(0.95,1)*((self.mood + self.motivation)*random.uniform(0.5,1.5))
    def set_alive(self,alive):
        self.alive = alive
    def assert_team(self,team_id):
        self.team=team_id