from Team import Team

class Manager:
    def __init__(self, budget, expenses, staff, match_calendar, scout_finds, team):
        self.budget=budget
        self.expenses=expenses
        self.match_calendar=match_calendar
        self.scout_finds=scout_finds
        self.team=Team(team,1,1,1,1)
    def buyPlayer(self, player):
        if(self.budget-player.cost<0):
            print("Insufficient funds.")
        else:
            self.team.players.append(player)
            self.scout_finds.remove(player)
            self.budget=self.budget-player.cost
