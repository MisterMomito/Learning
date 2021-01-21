import matplotlib.pyplot as plt
from NumpyandMatplotLib.Numpy import c

k = [1.2, 2.3, 4.5, 10, 11]
plt.plot(k)
plt.ylabel('Y axis')
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # the first list are x coordinates and the second are y
plt.axis([0, 10, 0, 20])  # First two points are range of x axis and last two are range of y
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # x-coord, y-coord, color + o=points, -=lines, ^=tri
plt.axis([0, 10, 0, 20])  # First two points are range of x axis and last two are range of y
plt.show()

plt.plot(c, c**2, 'b^', c)  # idk what happened here
plt.show()

