#! /usr/bin/python
import TableReader as table
import DataAnalysis as data

mru, mra = table.csvParser("data.csv")

physicsToolboxDataUniform = []
for i in range(1, 8):
    t, f = table.csvParser("PhysicsToolboxData/mru" + str(i) + ".csv")
    physicsToolboxDataUniform.append([t, f])

physicsToolboxDataAccelerated = []
for i in range(1, 4):
    t, f = table.csvParser("PhysicsToolboxData/mra" + str(i) + ".csv")
    physicsToolboxDataAccelerated.append([t, f])

data.analyzeMRU(mru, physicsToolboxDataUniform)
data.analyzeMRA(mra, physicsToolboxDataAccelerated)
