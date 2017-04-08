#Uniform Move
def positionUniform(yo,vo,to):
    return (yo + vo*to)
#Acceleration Move
def positionNoUniform(yo,vo,a,to):
    return (yo + vo*to + a*(to*to)/2)
#Update velocity
def velocityInTime(vo,to,a):
    return (vo + to*a)

# given a vector t of times and x of positions, calculates the average velocity, assuming initial position = 0
def averageVelocity(t, x):
    return x[len(x)-1]/t[len(t)-1]

# given a vector t of times and x of positions, calculates the 'average' acceleration (that which produces the final point, assuming initial velocity = 0 and position = 0)
def averageAcceleration(t, x):
    return 2*x[len(x)-1]/(t[len(t)-1]**2)

def instantVelocity(times, x, i):
    if i == 0: return 0
    else: return (x[i]-x[i-1])/(times[i]-times[i-1])

