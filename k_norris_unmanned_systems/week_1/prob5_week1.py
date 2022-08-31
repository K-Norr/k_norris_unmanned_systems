# -*- coding: utf-8 -*-
"""
Problem 5 - Week 1 - Node Distance Finder
Created on Tue Aug 30 23:14:29 2022

@author: kanor
"""

import numpy as np


#declaration of node class with 4 variables:
#x position, y position, parent cost and node index
class node:
    def __init__(self, x, y, parent_cost, index):
        self.x = x
        self.y = y
        self.cost = parent_cost
        self.index = index

#declare grid constraints and determine x and y lengths 
maxx = 10
maxy = 10
gridsize = 0.5
lenx = (maxx / gridsize) + 1
leny = (maxy / gridsize) + 1

#define function to find the node index given x and y
def find_index(x,y):
    found_index = (x / gridsize) + ((y / gridsize) * lenx)  
    return found_index

#define function to find the x value given node index
def find_x(index):
    found_x = (index % lenx)*gridsize
    return found_x

#define function to find the y value given node index
def find_y(index):
    found_y = (((index - (index % lenx)) / leny)*gridsize)
    return found_y

def node_distance(node_1, node_2):
    distance = np.sqrt((node_1.x - node_2.x) ** 2 + (node_1.y - node_2.y)^2)
    return distance

#create test nodes
test_node_1 = node(2,1,0, find_index(2,1))
test_node_2 = node(3,2,0, find_index(3,2))

#verify correct node indices and correct distance
print("Node 1's index = ", test_node_1.index)
print("Node 2's index = ", test_node_2.index)
print("The distance between the nodes is ", node_distance(test_node_1, test_node_2))
