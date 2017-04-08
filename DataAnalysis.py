import matplotlib.pyplot as plot
import TableReader as table

x = [0, 2, 4, 6]
mru, mra = table.csvParser("data.csv")

print(mru[0])

#plot.plot(x, [0] + mru[0])
#plot.show()
