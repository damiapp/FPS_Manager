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

#Import players and teams from TABLES
t1=Player(0.86, 0.81, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Dami", "Kodan",25,10)
t2=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Veseli", "Ghost",24,10)
t3=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Suki", "Ljuba",24,10)
t4=Player(0.9, 0.9, 0.9, 0.71, 0.82, 0.78, 0.83, 0.89, True, "Srbija", "Subota", "Cane",24,10)
t5=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Sile", "Gile",24,10)

team1=Team("GolaKurcina",[t1,t2,t3,t4,t5],1,0,1,1)

ct1=Player(0.9, 0.9, 0.92, 0.68, 0.92, 0.61, 0.82, 0.86, True, "Srbija", "Skore", "ACE",25,10)
ct2=Player(0.8, 0.9, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Faker", "Ghost",24,10)
ct3=Player(0.8, 0.9, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Mker", "Ljuba",24,10)
ct4=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "FK1ER", "Panzer",24,10)
ct5=Player(0.8, 0.89, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "BR0NER", "Gile",24,10)

team2=Team("GolaPickurina",[ct1,ct2,ct3,ct4,ct5],1,0,1,1)


# Close communication with the database
cur.close()
conn.close()

#g1=0
#g2=0

#for x in range(100):
#w1=abs(numpy.random.randn())
#w2=abs(numpy.random.randn())
#b=numpy.random.randn()
#if(NN(m1,m2,w1,w2,b)>0.5):
#        g1=g1+1
#    else:
#        g2=g2+1
#print(g1)
#print(g2)
sc=Score(0,0)
def Match():
    env=simpy.Environment()
    wipe_out=env.event()
    env.process(Round(team1,team2,env,wipe_out,sc))
    env.run(wipe_out)
    team1.reset_alive()
    team2.reset_alive()
    sc.print_score()
        
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