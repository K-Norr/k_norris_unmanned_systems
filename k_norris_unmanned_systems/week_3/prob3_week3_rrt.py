# -*- coding: utf-8 -*-
"""
RRT Workbook
Created on Wed Sep  7 10:39:03 2022

@author: kanor
"""
#import modules
import utility as util
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
time_start = datetime.now()

#import obstacle list from csv
f = open('biggrids.csv','r')
    
raw = np.genfromtxt(f,delimiter=',',autostrip=True)
obs = []
for line in raw:
    obs.append([line[0],line[1]])
print("Import complete")

#declare config space parameters
xrange = [0,50]
yrange = [0,50]
gridsize = 0.5

#declare path scenario parameters
obs_list = obs
start = [49,0.5]
goal = [0.5,49]
bot_rad = 0.25

#initialize objects and input into path junction object
cspace = util.Cspace(xrange, yrange, gridsize)
parameters = util.Path_parameters(obs_list, start, goal, bot_rad)
rrt = util.PathRRT(cspace,parameters)
print("Initializing Pathfinding")

#run pathfinding function
path = rrt.get_path()

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
plt.scatter(xobs,yobs, marker=".",color='r')
plt.show()

print(datetime.now() - time_start)