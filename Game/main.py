from Player import Player
from Team import Team
import numpy
import random
import simpy
import schedule
import time

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import psycopg2
import json
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

conn = psycopg2.connect("dbname=majortactics user=postgres password="+os.getenv("PASSWORD"))

cur = conn.cursor()

class Score:
    def __init__(self,t1,t2):
        self.t1=t1
        self.t2=t2
    def set_t1(self,t1):
        self.t1=t1
    def set_t2(self,t2):
        self.t2=t2
    def print_score(self):
        print(str(self.t1) + " : " + str(self.t2))

def check_win(team1,team2,sc):
    k1=0
    k2=0
    for p in team1.players:
        if not p.alive:
            k1=k1+1
    for p in team2.players:
        if not p.alive:
            k2=k2+1
    if k1 == 5:
        sc.set_t2(sc.t2+1)
        return True
    if k2 == 5:
        sc.set_t1(sc.t1+1)
        return True
    return False
    
def Round(team1,team2,env,wipe_out,sc):
    while True:
        yield env.timeout(1)
        t=team1.get_rand()
        ct=team2.get_rand()
        m1=t.get_m_w()
        m2=-ct.get_m_w()
        b=random.uniform(-0.2,0.2)
        if(NN(m1,m2,b)>0.5):
            print(t.name+" has killed " +ct.name+" time: "+str(env.now))
            ct.set_alive(False)
        else:
            print(ct.name+" has killed " +t.name+" time: "+str(env.now))
            t.set_alive(False)
        if(check_win(team1,team2,sc)):
            wipe_out.succeed()

def NN(m1, m2, b):
    z=m1+m2+b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1+numpy.exp(-x))

def weight(p1,p2):
    pass

#Import Team from data
id=str(random.randint(3,12))
cur.execute("SELECT x.* FROM public.team_data x WHERE id="+id+";")
v=cur.fetchone()
team1 = Team(v[1].rstrip(),[],v[2],v[3],v[4],v[5])
#Import players into team from data
cur.execute("SELECT x.* FROM public.player_data x WHERE team_id = "+id+";")    
for i in range(5):
    v=cur.fetchone()
    p=Player(float(v[1]), float(v[2]), float(v[3]), float(v[4]), float(v[5]), float(v[6]),\
        float(v[7]), float(v[8]), v[9], v[10].rstrip(), v[11].rstrip(), v[12].rstrip(), float(v[13]), float(v[14]))
    team1.add_player(p)

#Same as above
id1=random.randint(3,12)
while(id1==int(id)):
    id1=random.randint(3,12)
id1=str(id1)
cur.execute("SELECT x.* FROM public.team_data x WHERE id="+id1+";")
v=cur.fetchone()
team2 = Team(v[1].rstrip(),[],v[2],v[3],v[4],v[5])
#Team1 add players
cur.execute("SELECT x.* FROM public.player_data x WHERE team_id = "+id1+";")
for i in range(5):
    v=cur.fetchone()
    p=Player(float(v[1]), float(v[2]), float(v[3]), float(v[4]), float(v[5]), float(v[6]),\
        float(v[7]), float(v[8]), v[9], v[10].rstrip(), v[11].rstrip(), v[12].rstrip(), float(v[13]), float(v[14]))
    team2.add_player(p)

# Close communication with the database
cur.close()
conn.close()

sc=Score(0,0)
def Match():
    env=simpy.Environment()
    wipe_out=env.event()
    env.process(Round(team1,team2,env,wipe_out,sc))
    env.run(wipe_out)
    team1.reset_alive()
    team2.reset_alive()
    sc.print_score()

print(team1.name+"  VS  "+team2.name)
print('\n')
schedule.every(1).seconds.do(Match)
while True:
    schedule.run_pending()
    time.sleep(1)
    if(sc.t1>15 or sc.t2>15):
        if(sc.t1>15):
            print(team1.name+" wins!")
        if(sc.t2>15):
            print(team2.name+" wins!")
        break
    print("-----------------------")