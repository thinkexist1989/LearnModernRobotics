#!/usr/bin/env/python
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

# T = SE3(1,2,3)*SE3.Rx(30, 'deg')
# T.print()
# T.printline()
# T.plot()

# trplot( transl(1,2,3), frame='A', rviz=True, width=1, dims=[0, 10, 0, 10, 0, 10])
# tranimate(transl(4, 3, 4)@trotx(2)@troty(-2), frame='A', arrow=False, dims=[0, 5], nframes=200)


X = SE2.Rand()
X.print()
X.animate(frame='A', arrow=False,dims=[-5,5, -5, 5])

plt.show()