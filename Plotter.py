import matplotlib.pyplot as plt

#Uniform Move
def positionUniform(yo,vo,to):
    return (yo + vo*to)
#Acceleration Move
def positionNoUniform(yo,vo,a,to):
    return (yo + vo*to + a*(to*to)/2)
#Update velocity
def velocityInTime(vo,to,a):
    return (vo + to*a)

#Make the points for plotting
def notUniformDotPlot(yo,vo,a,tf,step):
    t = 0
    v = []
    p = []
    x = []
    while(t <= tf):
        p.append(positionNoUniform(yo,vo,a,t))
        v.append(velocityInTime(vo,t,a))
        x.append(t)
        t += step
    return p,v,x

#Make the points for plotting
def uniformDotPlot(yo,vo,tf,step):
    t = 0
    v = []
    p = []
    x = []
    while(t <= tf):
        p.append(positionUniform(yo,vo,t))
        x.append(t)
        v.append(vo)
        t += step
    return p,v,x
#Show the plot itself
def uniformShow(yo,vo,tf,step):
    p,v,x = uniformDotPlot(yo, vo, tf, step)
    plt.scatter(x,p)
    plt.scatter(x,v)
    plt.show()
    
#Show the plot itself
def noUniformShow(yo,vo,a,tf,step):
    p,v,x = notUniformDotPlot(yo, vo, a,tf, step)
    plt.plot(x,p)
    plt.plot(x,v)
    

#Dots from experiment
def dotVector(v):
    p = [10,20,30]
    x = v
    return p,x
#Plot experiment dots
def dotVectorShow(v):
    p,x = dotVector(v);
    plt.scatter(x,p)