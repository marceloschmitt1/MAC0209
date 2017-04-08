import math
import matplotlib.pyplot as plot
import numpy as np
import Physics as physics

x = [0, 2, 4, 6]

# analyze data for the uniform moviment experiments. mru has the positions measured by the LDRs, pt is the data from the accelerometer in the cellphone
def analyzeMRU(mru, pt):
    n = 0
    total = 0
    for i, t in enumerate(mru):
        velocity = physics.averageVelocity(t, x)
        print("Movimento Uniforme, Experimento", i+1, "\n======")
        print("Tempos:", t)
        print("Velocidade média:", velocity, "m/s")
        analyticPositions = list(map(lambda time: physics.positionUniform(0, velocity, time), t))
        errors = [abs(x - a) for (x,a) in zip(x, analyticPositions)]
        print("Erros experimentais:", errors)
        total += velocity
        n += 1

        input("Aperte Enter para exibir o gráfico de s(t)")
        plot.scatter(t, x, color="green", label="Posição (experimental)")
        plot.scatter(t, errors, color="red", label="Erro (posição)")
        plot.plot(t, analyticPositions, label="Posição (modelo)")
        plot.plot(pt[i][0], pt[i][1], color="cyan", label="Força (acelerômetro)")
        plot.xlabel('segundos', fontsize=18)
        plot.ylabel('metros', fontsize=16)
        plot.legend()
        plot.show()
        print("")
    print("Velocidade média de todos os experimentos:", total/n, "m/s\n\n")

# analyze data for the accelerated moviment experiments. mra has the positions measured by the LDRs, pt is the data from the accelerometer in the cellphone
def analyzeMRA(mra, pt):
    n = 0
    total = 0
    npoints = 100 # number of points in domain to plot at
    for i, t in enumerate(mra):
        acceleration = physics.averageAcceleration(t, x)
        print("Movimento Acelerado, Experimento", i+1, "\n======")
        print("Tempos:", t)
        v = list(map(lambda time: physics.instantVelocity(t, x, time), range(0,4)))
        print("Velocidades:", v)
        print("Aceleração 'média': ", acceleration, "m/s^2")
        times = [(p/npoints)*(t[len(t)-1]+1) for p in list(range(0, npoints))] # creates npoints points equally spaced from 0 to the last measured time
        analyticPositions = list(map(lambda time: physics.positionNoUniform(0, 0, acceleration, time), times))
        analyticPositionsOnMeasuredTimes = list(map(lambda time: physics.positionNoUniform(0, 0, acceleration, time), t))
        errors = [abs(x - a) for (x,a) in zip(x, analyticPositionsOnMeasuredTimes)]
        print("Erros experimentais (posição):", errors)
        analyticVelocities = list(map(lambda time: physics.velocityInTime(0, time, acceleration), t))
        vErrors = [abs(x - a) for (x,a) in zip(v, analyticVelocities)]
        print("Erros experimentais (velocidade):", vErrors)
        total += acceleration
        n += 1    

        input("Aperte Enter para exibir o gráfico de s(t) e v(t)")
        f,plots = plot.subplots(2, sharex=True)
        plots[0].scatter(t, x, color="green", label="Posição (experimental)")
        plots[0].scatter(t, errors, color="red", label="Erro (posição)")
        plots[0].plot(times, analyticPositions, label="Posição (modelo)")
        plots[0].plot(pt[i][0], pt[i][1], color="cyan", label="Força (acelerômetro)")
        plots[0].legend()
        plots[0].set_xlabel('segundos', fontsize=12)
        plots[0].set_ylabel('metros', fontsize=12)
        
        plots[1].scatter(t, v, color="green", label="Velocidade (experimental)")
        plots[1].scatter(t, vErrors, color="red", label="Erro (velocidade)")
        plots[1].plot(t, analyticVelocities, label="Velocidade (modelo)")
        plots[1].plot(pt[i][0], pt[i][1], color="cyan", label="Força (acelerômetro)")
        plots[1].legend()
        plots[1].set_xlabel('segundos', fontsize=12)
        plots[1].set_ylabel('m/s', fontsize=12)
        
        plot.show()
        print("")
        
    print("Aceleração 'média' de todos os experimentos: ", total/n, "m/s^2")
