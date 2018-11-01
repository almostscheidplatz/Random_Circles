import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from shapely.geometry.polygon import LinearRing
from shapely.geometry import Point, LineString
import random
import math

cmap = matplotlib.cm.get_cmap('BuGn')

plt.axis('equal')
plt.axis('off')
plt.xlim(20,80)
plt.ylim(20,80)

def circles_polyline(ellipses, n=1000):
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

def intersectionsline(a, b):
    ea = a
    eb = LinearRing(b)
    mp = eb.intersection(ea)

    x = [p.x for p in mp]
    y = [p.y for p in mp]
    return zip(x, y)

def create_circles(name):
    circles = []

    for i in range(6):
        if i==0:
            circles.append((random.randint(80,120),random.randint(40,60), random.randint(40,60)))
        if i==1:
            a_ = circles_polyline(circles)
            circles.append((a_[0][:,0][400]-random.randint(5,10), a_[0][:,1][400]-random.randint(5,10), random.randint(5,15)))
            #circles.append((circles[0][0]-circles[0][2]-random.randint(3,10),circles[0][0]+circles[0][1]-random.randint(3,10), random.randint(5,10)))
        if i==2:
            x = random.uniform(15,25)
            y = random.uniform(75,90)

            dx = circles[i-1][0]-x
            dy = circles[i-1][1]-y

            r = math.sqrt((dx**2)+(dy**2))

            # print "line"
            # print x,y
            # print circles[i-1][0], circles[i-1][1]
            # l = LineString([(int(x), int(y)), (int(circles[i-1][0]), int(circles[i-1][1]))])
            # print "endline"
            #
            # p = LineString([[5,5], [2,0]])
            # plt.plot(p)
            # plt.plot(l,color="black")
            #a_ = circles_polyline(circles)
            #print intersectionsline(l,a_[i-1])

            # print r,circles[i-1][2]
            circles.append((x, y, r-circles[i-1][2]+0.001))
            #circles.append((circles[0][0]-circles[0][2]-random.randint(3,10),circles[0][0]+circles[0][1]-random.randint(3,10), random.randint(5,10)))
        if i==3:
            a_ = circles_polyline(circles)
            circles.append((random.randint(20,30), random.randint(45,55), random.randint(5,15)))
            #circles.append((circles[0][0]-circles[0][2]-random.randint(3,10),circles[0][0]+circles[0][1]-random.randint(3,10), random.randint(5,10)))
        if i==4:
            a_ = circles_polyline(circles)
            circles.append((random.randint(10,20), random.randint(30,45), random.randint(5,15)))
            #circles.append((circles[0][0]-circles[0][2]-random.randint(3,10),circles[0][0]+circles[0][1]-random.randint(3,10), random.randint(5,10)))
        if i==5:
            a_ = circles_polyline(circles)
            circles.append((random.randint(0,10), random.randint(0,20), random.randint(5,25)))
            #circles.append((circles[0][0]-circles[0][2]-random.randint(3,10),circles[0][0]+circles[0][1]-random.randint(3,10), random.randint(5,10)))


    for idc,c_ in enumerate(circles_polyline(circles)):
        print idc
        print circles[idc][1]
        print circles[idc][1]/100.0
        plt.plot(c_[:,0], c_[:,1],color = cmap(1-circles[idc][1]/100.0))

    for idc,c_ in enumerate(circles_polyline(circles)):
        for idcint,cint_ in enumerate(circles_polyline(circles)):
            if idc==idcint:
                continue
            print "interslength",len(intersections(c_, cint_))
            if intersections(c_, cint_):
                if Point(intersections(c_, cint_)[0][0],intersections(c_, cint_)[0][1]).distance(Point(intersections(c_, cint_)[1][0],intersections(c_, cint_)[1][1]))<0.5:
                    for x,y in intersections(c_, cint_):
                        #plt.plot(x, y, "x")

                        spot=[(x,y,1),(x,y,2+random.randint(0,2))]
                        a_=circles_polyline(spot)
                        plt.fill(a_[0][:,0], a_[0][:,1],color=cmap(1-circles[idc][1]/100.0),zorder=10)
                        plt.plot(a_[1][:,0], a_[1][:,1],linestyle="--",dashes=(2, 4),color=cmap(0.4),zorder=10)
                        break
                    continue

            for x,y in intersections(c_, cint_):
                #plt.plot(x, y, "x")

                spot=[(x,y,1),(x,y,2)]
                a_=circles_polyline(spot)
                plt.fill(a_[0][:,0], a_[0][:,1],color=cmap(1-circles[idc][1]/100.0),zorder=10)
                plt.plot(a_[1][:,0], a_[1][:,1],linestyle="--",dashes=(2, 4),color=cmap(0.4),zorder=10)
    #plt.show()
    plt.savefig("%s.pdf"%(name), dpi=800)
    plt.gcf().clear()

for i in range(15):
    create_circles(i)
