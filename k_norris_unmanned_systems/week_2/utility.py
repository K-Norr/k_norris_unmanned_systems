# -*- coding: utf-8 -*-
"""
Week 2 - Utility Module
Path Finding Utility Package
Created on Wed Sep  7 10:28:44 2022

@author: kanor
"""

import numpy as np
import matplotlib.pyplot as plt

class Cspace():
    def __init__(self, xrange:tuple, yrange:tuple, gridsize:float) ->None:
        self.xrange = xrange
        self.yrange = yrange
        self.grid = gridsize
        
    def __index__(self, curr_pos:list) ->int:
        index = (curr_pos[0] / self.grid) + ((curr_pos[1] / self.grid)*(((self.xrange[1]-self.xrange[0])/self.grid)+1))
        return index

class Path_parameters():
    def __init__(self, obs_list:list, start:tuple, goal:tuple, bot_rad:float) ->None:
        self.obs = obs_list
        self.start = start
        self.goal = goal
        self.rad = bot_rad
        
    def __valid__(self, curr_pos:tuple, temp_pos:tuple, config:object) ->bool:
        coll = False
        for obs in self.obs:
            dist = np.sqrt(((obs[0]-temp_pos[0])**2) + ((obs[1]-temp_pos[1])**2))
            if dist < self.rad:
                coll = True
            elif temp_pos in self.obs:
                coll = True
                
        if coll == True:
            return False
        elif temp_pos == curr_pos:
            return False
        elif (temp_pos[0] < config.xrange[0]) or (temp_pos[0] > config.xrange[1]):
            return False
        elif (temp_pos[1] < config.yrange[0]) or (temp_pos[1] > config.yrange[1]):
            return False
        else:
            return True
        
class Node():
    def __init__(self, loc:tuple, cost:float, parent_index:int) ->None:
        self.loc = loc
        self.cost = cost
        self.par_ind = parent_index
        

class Path_Djik():
    def __init__(self, cspace:object, parameters:object) ->None:
        self.cspace = cspace
        self.parameters = parameters
        
    def node_dist(self, node1:object, node2:object) ->float:
        dist = np.sqrt(((node1.loc[0]-node2.loc[0])**2)+((node1.loc[1]-node2.loc[1])**2))
        return dist
    
    def find_path(self) ->list:
        unvisited_nodes = dict()
        visited_nodes = dict()
        
        curr_pos = self.parameters.start
        curr_index = self.cspace.__index__(curr_pos)
        curr_node = Node(curr_pos, 0, -1)
        unvisited_nodes[curr_index] = curr_node
        
   
        while len(unvisited_nodes) > 0:
            min_id = min(unvisited_nodes, key = lambda x: unvisited_nodes[x].cost)
            curr_node = unvisited_nodes[min_id]
            curr_pos = curr_node.loc
            visited_nodes[min_id] = unvisited_nodes[min_id]
            del unvisited_nodes[min_id]
            
            for i in (-self.cspace.grid, 0, self.cspace.grid):
                for j in (-self.cspace.grid, 0, self.cspace.grid):
                    temp_pos = [curr_node.loc[0]+i, curr_node.loc[1]+j]
                    temp_node = Node(temp_pos, 0, min_id)
                    temp_index = self.cspace.__index__(temp_pos)
                    temp_cost = self.node_dist(temp_node, curr_node)
                    temp_node.cost = curr_node.cost + temp_cost
                    if self.parameters.__valid__(curr_pos, temp_pos, self.cspace):
                        if temp_index in visited_nodes:
                            None
                        elif temp_index in unvisited_nodes:
                            if temp_node.cost < unvisited_nodes[temp_index].cost:
                                unvisited_nodes[temp_index].cost = temp_node.cost
                        else:
                            unvisited_nodes[temp_index] = temp_node
        
        path = []
        path_index = self.cspace.__index__(self.parameters.goal)
        path_node = visited_nodes[path_index]
        path.append(path_node.loc)
        while path_node.par_ind != -1:
            path_index = path_node.par_ind
            path_node = visited_nodes[path_index]
            path.append(path_node.loc)
        return path
        
    
    
    