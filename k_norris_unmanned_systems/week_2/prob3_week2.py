# -*- coding: utf-8 -*-
"""
Week 2 - Problem 3
Created on Wed Sep  7 10:39:03 2022

@author: kanor
"""
#import modules
import utility as util
import matplotlib.pyplot as plt
import numpy as np

#declare config space parameters
xrange = [0,10]
yrange = [0,10]
gridsize = 0.5

#declare path scenario parameters
obs_list = ([1,1],[4,4],[3,4],[5,0],[5,1],[0,7],[1,7],[2,7],[3,7])
start = [2,2]
goal = [8,9]
bot_rad = 1

#initialize objects and input into path junction object
cspace = util.Cspace(xrange, yrange, gridsize)
parameters = util.Path_parameters(obs_list, start, goal, bot_rad)
djik = util.Path_Djik(cspace,parameters)

#run pathfinding function
path = djik.find_path()

#separate results for plotting
xs = [x[0] for x in path]
ys = [x[1] for x in path]
xobs = [x[0] for x in obs_list]
yobs = [x[1] for x in obs_list]

#plot
fig = plt.figure()
plt.xlim(xrange[0],xrange[1])
plt.ylim(yrange[0],yrange[1])
plt.grid()
plt.plot(xs,ys)
plt.scatter(xobs,yobs, marker='x')
plt.show()
