from pycode.models.vector import Vector
from pycode.models.matrix import Matrix
from math import sin, cos, pi

t = pi / 2

A = 1.5 * Matrix([[cos(t), -sin(t)], [sin(t), cos(t)]])

u1 = Vector([1, 1])
u2 = Vector([2, 2])
u3 = Vector([2.5, 3])
u4 = Vector([0.5, 2])

U = [u1, u2, u3, u4]

V = [A @ u for u in U]

print(V)

print(A @ Vector([1.2, 1.8]))
