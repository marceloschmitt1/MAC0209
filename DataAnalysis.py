import math
import matplotlib.pyplot as plot
import numpy as np
import Plotter as plotter
import TableReader as table

x = [0, 2, 4, 6]
mru, mra = table.csvParser("data.csv")

# given a vector t of times and x of positions, calculates the average velocity, assuming initial position = 0
def averageVelocity(t, x):
    return x[len(x)-1]/t[len(t)-1]

# given a vector t of times and x of positions, calculates the 'average' acceleration (that which produces the final point, assuming initial velocity = 0 and position = 0)
def averageAcceleration(t, x):
    return 2*x[len(x)-1]/(t[len(t)-1]**2)

n = 0
total = 0
for t in mru:
    velocity = averageVelocity(t, x)
    print("Velocidade média:", velocity, "m/s")
    total += velocity
    n += 1

    plot.scatter(t, x)
    plot.plot(t, list(map(lambda time: plotter.positionUniform(0, velocity, time), t)))
    plot.show()
print("Velocidade média de todos os experimentos:", total/n, "m/s")

n = 0
total = 0
npoints = 100 # number of points in domain to plot at
for t in mra:
    acceleration = averageAcceleration(t, x)
    print("Aceleração 'média': ", acceleration, "m/s^2")
    total += acceleration
    n += 1

    plot.scatter(t, x)
    times = [(p/npoints)*(t[len(t)-1]+1) for p in list(range(0, npoints))]
    plot.plot(times, list(map(lambda time: plotter.positionNoUniform(0, 0, acceleration, time), times)))
    plot.show()
print("Aceleração 'média' de todos os experimentos: ", total/n, "m/s^2")
