import numpy
import matplotlib.pyplot  as plt


x = range(0, 10)
ax = numpy.array(x)
ay1 = ax * ax * ax
ay2 = ax ** 2 + numpy.sin(ax)
plt.plot(ax, ay1, 'ro--',)

plt.show()
