import numpy as np

"""Read a csv file of the first experiment then create
   the numpy vectors for plotting"""
def csvParser(filename):
    mru = []
    mra = []
    time = []
    acc = []
    
    f = open(filename, "r")
    for line in f:
        temp = [0]
        values = line.split(';')
        if len(values) == 4:
            experimentParser(values,mru,mra,temp)           
        else:
            if len(values) == 5:
                toolBoxParser(values, time, acc)
    
    if (len(mru) > 0 and len(mra) > 0):
        mru = np.asarray(mru)
        mra = np.asarray(mra)
        return mru,mra 
    
    time = np.asanyarray(time)
    acc = np.asanyarray(acc)
    return time,acc

""" Return a vector wichh each member is the mean
    of the col values of the Matrix v"""
def meanOfMesuaremnt(v):
    return np.mean(v,0)

""" Parse a line of velocity """
def experimentParser(values,mru,mra,temp):
    if values[0] == "0":
        del values[0]
        for item in values:
            temp.append(float(item))
        mru.append(temp)            
    else: 
        if values[0] == "1":
            del values[0]
            for item in values:
                temp.append(float(item))
            mra.append(temp)

""" Parse a line of accelerometer toolbox """
def toolBoxParser(values,time,acc):
    time.append(values[0])
    acc.append(values[4])