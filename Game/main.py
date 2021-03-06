from Player import Player
from Team import Team
import numpy

def NN(m1, m2, w1, w2, b):
    z=m1*w1+m2*w2+b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1+numpy.exp(-x))

def weight(p1,p2):
    pass

p1=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, "Srbija", "Dami", "Kodan",25)
p2=Player(0.11, 0.9, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, "Srbija", "Veseli", "Ghost",24)
p3=Player(0.11, 0.12, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, "Srbija", "Suki", "Ljuba",24)
p4=Player(0.11, 0.12, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, "Srbija", "Dzoni", "Panzer",24)
p5=Player(0.11, 0.12, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, "Srbija", "Sile", "Gile",24)
p6=Player(0.11, 0.12, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, "Srbija", "Filip", "pilif",24)
p7=Player(0.11, 0.12, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, "Srbija", "Luka", "Kalu",24)

team1=Team([p1,p2,p3,p4,p5,p6,p7],1,0,1,1)

team1.print_team()

print(team1.map_skill)

m1=p1.get_m()
m2=-p2.get_m()
g1=0
g2=0

for x in range(100):
    w1=abs(numpy.random.randn())
    w2=abs(numpy.random.randn())
    b=numpy.random.randn()
    if(NN(m1,m2,w1,w2,b)>0.5):
        g1=g1+1
    else:
        g2=g2+1
print(g1)
print(g2)