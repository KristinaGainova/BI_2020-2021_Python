import numpy as np
import pylab
from random import randint

def midpoint(point1, point2):
    return [(point1[0] + point2[0])/2, (point1[1] + point2[1])/2]

curr_point = [0,0]
vertice1 = [0,0]
vertice2 = [1,0]
vertice3 = [.5,np.sqrt(3)/2]

# Plot with 5000 points
for _ in range(5000):
    val = randint(0,2)
    if val == 0:
        curr_point = midpoint(curr_point, vertice1)
    if val == 1:
        curr_point = midpoint(curr_point, vertice2)
    if val == 2:
        curr_point = midpoint(curr_point, vertice3)
    pylab.plot(curr_point[0],curr_point[1],'go',markersize=2)
    pylab.title('Sierpinski Triangle')

pylab.show()