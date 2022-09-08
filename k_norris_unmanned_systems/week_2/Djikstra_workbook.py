# -*- coding: utf-8 -*-
"""
Djikstra Workbook
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
    
    def __index__(self, current_position:list) -> int:
        x = float(current_position[0])
        y = float(current_position[1])
        xlen = self.xrange[1] - self.xrange[0]
        index = (x / self.gridsize) + ((y / self.gridsize) * ((xlen / 0.5) + 1))
        return index
        
class Path_parameters():
    def __init__(self, obs_list:list, start:tuple, goal:tuple, radius) ->None:
        self.obs = obs_list
        self.start = start
        self.goal = goal
        self.rad = radius
        
    def __valid_pos__(self, current_position:list, temp_position:list, xrange:tuple, yrange:tuple) -> bool:
        if temp_position in self.obs:
            return False
        elif temp_position == current_position:
            return False
        elif (temp_position[0] < xrange[0]) or (temp_position[0] > xrange[1]):
            return False
        elif (temp_position[1] < yrange[0]) or (temp_position[1] > yrange[1]):
            return False
        else:
            return True

class Node():
    def __init__(self, location:tuple, parent_cost, index) ->None:
        self.loc = location
        self.cost = parent_cost
        self.index = index
 
def node_distance(node1, node2) -> float:
    dx = node1.loc[0] - node2.loc[0]
    dy = node1.loc[1] - node2.loc[0]
    travel_cost = np.sqrt((dx**2)+(dy**2)) 
    return travel_cost

def pathway(goal_location:list) ->list:
    track = []
    path_loc = goal_location
    path_index = cspace.__index__(path_loc)
    track.append(path_index)
    path_node = visited_nodes[path_index]
    while path_node.index != -1:
        path_index = path_node.index
        path_node = visited_nodes[path_index]
        track.append(path_index)
    return track    
    

    
#Declare CSpace and Path Parameters
cspace = Cspace([0,10],[0,10],0.5)
parameters = Path_parameters(([0.5,0.5],[5,5],[7,6]),[1,1],[9,9],0)

#Initialize dictionaries
unvisited_nodes = dict()
visited_nodes = dict()


#Initialize Start node
current_position = parameters.start
current_index = cspace.__index__(current_position)
current_node = Node(current_position, 0, -1)
unvisited_nodes[current_index] = current_node

while len(unvisited_nodes) > 0:
    
    min_id = min(unvisited_nodes, key = lambda x: unvisited_nodes[x].cost)
    current_node = unvisited_nodes[min_id]
    visited_nodes[min_id] = unvisited_nodes[min_id]
    del unvisited_nodes[min_id]
    
    for i in (-cspace.gridsize, 0, cspace.gridsize):
        for j in (-cspace.gridsize, 0, cspace.gridsize):
            temp_location = [current_node.loc[0] + i, current_node.loc[1] + j]
            temp_node = Node(temp_location, 0, min_id)
            temp_index = cspace.__index__(temp_location)
            temp_cost = node_distance(temp_node, current_node)
            temp_node.cost = current_node.cost + temp_cost
            if parameters.__valid_pos__(current_position, temp_location, cspace.xrange, cspace.yrange) == True:
                if temp_index in visited_nodes:
                    None
                elif temp_index in unvisited_nodes:
                    if temp_node.cost < unvisited_nodes[temp_index].cost:
                        unvisited_nodes[temp_index].cost = temp_node.cost
                else:
                    unvisited_nodes[temp_index] = temp_node
                
       
print(len(unvisited_nodes))
print(len(visited_nodes))  

final_path = pathway(parameters.goal)
print(final_path)   