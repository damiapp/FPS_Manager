from Player import Player
from Team import Team
import numpy
import simpy

def check_win(team1,team2):
    k1=0
    k2=0
    for p in team1.players:
        if not p.alive:
            k1=k1+1
    for p in team2.players:
        if not p.alive:
            k2=k2+1
    if k1 is 5:
        print("Team 2 has won")
        return True
    if k2 is 5:
        print("Team 1 has won")
        return True
    return False
    
def Round(team1,team2,env,wipe_out):
    while True:
        yield env.timeout(2)
        ct=team2.get_rand()
        t=team1.get_rand()
        m1=t.get_m()
        m2=-ct.get_m()
        w1=abs(numpy.random.randn())
        w2=abs(numpy.random.randn())
        b=numpy.random.randn()
        if(NN(m1,m2,w1,w2,b)>0.5):
            print(t.name+" has killed " +ct.name+" time: "+str(env.now))
            ct.set_alive(False)
        else:
            print(ct.name+" has killed " +t.name+" time: "+str(env.now))
            t.set_alive(False)
        if(check_win(team1,team2)):
            wipe_out.succeed(15)

def NN(m1, m2, w1, w2, b):
    z=m1*w1+m2*w2+b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1+numpy.exp(-x))

def weight(p1,p2):
    pass

t1=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Dami", "Kodan",25)
t2=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Veseli", "Ghost",24)
t3=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Suki", "Ljuba",24)
t4=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Dzoni", "Panzer",24)
t5=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Sile", "Gile",24)
t6=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Filip", "pilif",24)
t7=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Luka", "Kalu",24)

team1=Team([t1,t2,t3,t4,t5,t6,t7],1,0,1,1)

ct1=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Peter", "Kodan",25)
ct2=Player(0.11, 0.9, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, True, "Srbija", "Faker", "Ghost",24)
ct3=Player(0.11, 0.12, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, True, "Srbija", "Mker", "Ljuba",24)
ct4=Player(0.11, 0.12, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, True, "Srbija", "FK1ER", "Panzer",24)
ct5=Player(0.11, 0.12, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, True, "Srbija", "BR0NER", "Gile",24)
ct6=Player(0.11, 0.12, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, True, "Srbija", "My2p", "pilif",24)
ct7=Player(0.11, 0.12, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, True, "Srbija", "Gip1", "Kalu",24)

team2=Team([ct1,ct2,ct3,ct4,ct5,ct6,ct7],1,0,1,1)

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
env=simpy.Environment()
wipe_out=env.event()
env.process(Round(team1,team2,env,wipe_out))
env.run(wipe_out)
