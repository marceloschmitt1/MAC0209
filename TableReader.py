import numpy as np

"""Read a csv file of the first experiment then create
   the numpy vectors for plotting"""
def csvParser(filename):
    mru = []
    mra = []
    f = open(filename, "r")
    for line in f:
        temp = []
        values = line.split(',')
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
    mru = np.asarray(mru)
    mra = np.asarray(mra)
    return mru,mra 

""" Return a vector wich each menber is the mean
    of the col values of the Matrix v"""
def meanOfMesuaremnt(v):
    return np.mean(v,0)
