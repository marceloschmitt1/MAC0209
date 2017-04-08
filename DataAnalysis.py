import matplotlib.pyplot as plot
import numpy as np
import TableReader as table

x = [0, 2, 4, 6]
mru, mra = table.csvParser("data.csv")

for t in mru:
    plot.scatter(t, x)
    plot.show()

for t in mra:
    plot.scatter(t, x)
    plot.show()
