# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:37:09 2022

@author: kanor
"""

import numpy as np
import matplotlib.pyplot as plt

class Cspace():
    def __init__(self, xrange:tuple, yrange:tuple, gridsize) ->None:
        self.xrange = xrange
        self.yrange = yrange
        self.gridsize = gridsize
        
class Path_parameters():
    def __init__(self, obs_list:list, start:tuple, goal:tuple, radius) ->None:
        self.obs = obs_list
        self.start = start
        self.goal = goal
        self.rad = radius

class Node():
    def __init__(self, location:tuple, parent_cost, index) ->None:
        self.loc = location
        self.cost = parent_cost
        self.index = index

cspace = Cspace([0,10],[0,10],0.5)
parameters = Path_parameters(([1,5],[5,5],[7,6]),[1,1],[9,9],1)

test_node = Node([2,5],0,15)

if test_node.loc in parameters.obs:
    print("obstacle")
    

    