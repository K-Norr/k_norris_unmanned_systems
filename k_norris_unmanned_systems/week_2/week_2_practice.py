# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

class Djikstras():
    def __init__(self, obs_list:list, start:tuple, goal:tuple) ->None:
        self.obs = obs_list
        self.start = start
        self.goal = goal
        
start = [1,1]
goal = [9,9]
obs_list = ([4,5], [3,2], [8,4])
current_loc = ([4,16])
xrange = [0,10]
yrange = [0,10]


djikstra = Djikstras(obs_list, start, goal)


def distance_checker(obs_list:list, location:tuple):
    for obs in obs_list:
        distance = np.sqrt((obs[0]-location[0])**2 + (obs[1]-location[1])**2)
        if distance <= 0.5:
            return True

def obs_checker(obs_list:list, location:tuple):
    if location in obs_list:
       return True
    else:
       return False
   
def range_checker(xrange:tuple, yrange:tuple, location:tuple):
    if (location[0] < xrange[0]) or (location[0] > xrange[1]):
        return True
    if (location[1] < yrange[0]) or (location[1] > yrange[1]):
        return True
        

def collision_checker(obs_list:list, current_loc:tuple):
      if obs_checker(obs_list, current_loc) == True:
          return True
      if distance_checker(obs_list, current_loc) == True:
          return True
      if range_checker(xrange, yrange, current_loc) == True:
          return True
      else:
          return False
      
print(collision_checker(obs_list, current_loc))        

