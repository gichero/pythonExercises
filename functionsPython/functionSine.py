import math 
import matplotlib.pyplot as plot

def f(x):

    return math.sin(x)


xs = range(-5, 5)
ys = []

for x in xs:
    ys.append(f(x))
plot.plot(xs, ys)
plot.show()