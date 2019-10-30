from matplotlib import pyplot as plt # for plotting
from random import randint # for sorting and creating data pts
from math import atan2 # for computing polar angle

def create_points(ct, min=0, max=50):
    return [[randint(min,max), randint(min,max)] \
        for _ in range(ct)]

def scatter_plot(coords, convex_hull=None):
    xs, ys = zip(*coords) # unzip into x and y coord lists
    plt.scatter(xs, ys) # plot the data points

    if convex_hull != None:
        for i in range(1, len(convex_hull)+1):
            if i == len(convex_hull): i = 0 # wrap
            c0 = convex_hull[i-1]
            c1 = convex_hull[i]
            plt.plot((c0[0],c1[0]), (c0[1],c1[1]), 'r')
    plt.show()

scatter_plot(create_points(10))