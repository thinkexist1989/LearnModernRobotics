#!/usr/bin/env/python

import roboticstoolbox as rtb
robot = rtb.models.Panda()
print(robot)

# Te = robot.fkine(robot.qr)
# print(Te)

from spatialmath import SE3

Tep = SE3.Trans(0.6, -0.3, 0.1) * SE3.OA([0, 1, 0], [0, 0, -1])
sol = robot.ikine_LM(Tep, q0=robot.qr)
print(sol)

q_pickup = sol.q
print(robot.fkine(q_pickup))    # FK shows that desired end-effector pose was achieved

qt = rtb.jtraj(robot.qr, q_pickup, 50)

print(len(qt.q))
robot.plot(qt.q, backend='pyplot', movie='panda1.gif')
