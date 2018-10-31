import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry.polygon import LinearRing
import random

def circles_polyline(ellipses, n=800):
    t = np.linspace(0, 2*np.pi, n, endpoint=False)
    st = np.sin(t)
    ct = np.cos(t)
    result = []
    for x0, y0, a in ellipses:
        p = np.empty((n, 2))
        p[:, 0] = x0 + a * ct
        p[:, 1] = y0 + a * st
        result.append(p)
    return result

def intersections(a, b):
    ea = LinearRing(a)
    eb = LinearRing(b)
    mp = ea.intersection(eb)

    x = [p.x for p in mp]
    y = [p.y for p in mp]
    return zip(x, y)

circles = [(1, 1, 5), (2, 0.5, 5)]
a, b = circles_polyline(circles)

for x,y in intersections(a, b):
    plt.plot(x, y, "x")

plt.plot(a[:,0], a[:,1])
plt.plot(b[:,0], b[:,1])

plt.show()
