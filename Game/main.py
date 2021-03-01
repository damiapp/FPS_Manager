from Player import Player
import numpy

def NN(m1, m2, w1, w2, b):
    z=m1*w1+m2*w2+b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1+numpy.exp(-x))

p1=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, "Srbija", "Dami", "Kodan",25)
p2=Player(0.41, 0.42, 0.84, 0.22, 0.62, 0.71, 0.32, 0.16, "Srbija", "Veseli", "Ghost",24)

w1=numpy.random.randn()
w2=numpy.random.randn()
b=numpy.random.randn()
m1=p1.get_m()
m2=p2.get_m()

if(NN(m1,m2,w1,w2,b)>0.5):
    print("Player2 won")
else:
    print("Player1 won")
