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

def instantVelocity(times, x, i):
    if i == 0: return 0
    else: return (x[i]-x[i-1])/(times[i]-times[i-1])

n = 0
total = 0
for i, t in enumerate(mru):
    velocity = averageVelocity(t, x)
    print("Movimento Uniforme, Experimento", i+1, "\n======")
    print("Tempos nas posições [0  2  4  6]:", t)
    print("Velocidade média:", velocity, "m/s")
    total += velocity
    n += 1

    input("Aperte Enter para exibir o gráfico de s(t)")
    plot.scatter(t, x)
    plot.plot(t, list(map(lambda time: plotter.positionUniform(0, velocity, time), t))) # plots the analytic prediction of the position
    plot.show()
    print("")
print("Velocidade média de todos os experimentos:", total/n, "m/s\n\n")

n = 0
total = 0
npoints = 100 # number of points in domain to plot at
for i, t in enumerate(mra):
    acceleration = averageAcceleration(t, x)
    print("Movimento Acelerado, Experimento", i+1, "\n======")
    print("Tempos nas posições [0  2  4  6]:", t)
    v = list(map(lambda time: instantVelocity(t, x, time), range(0,4)))
    print("Velocidades nas posições [0  2  4  6]:", v)
    print("Aceleração 'média': ", acceleration, "m/s^2")
    total += acceleration
    n += 1

    input("Aperte Enter para exibir o gráfico de s(t)")
    plot.scatter(t, x)
    times = [(p/npoints)*(t[len(t)-1]+1) for p in list(range(0, npoints))] # creates npoints points equally spaced from 0 to the last measured time
    plot.plot(times, list(map(lambda time: plotter.positionNoUniform(0, 0, acceleration, time), times))) # plots the analytic prediction of the position
    plot.show()
    input("Aperte Enter para exibir o gráfico de v(t)")
    plot.scatter(t, v)
    plot.plot(t, list(map(lambda time: plotter.velocityInTime(0, time, acceleration), t))) # plots the analytic prediction of the position
    plot.show()
    print("")
print("Aceleração 'média' de todos os experimentos: ", total/n, "m/s^2")
