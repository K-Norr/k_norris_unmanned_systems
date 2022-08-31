# -*- coding: utf-8 -*-
"""
Problem 4 - Week 1 - Node Plotting
Created on Tue Aug 30 23:09:10 2022

@author: kanor
"""

import matplotlib.pyplot as plt

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


#cycle through x and y values and plot the node index for each node
for i in range(int(lenx)):
    for j in range(int(leny)):
        temp_x = i * gridsize
        temp_y = j * gridsize
        temp_index = find_index(temp_x,temp_y)
        plt.plot(temp_x,temp_y)
        plt.text(temp_x, temp_y, str(int(temp_index)), color="red", fontsize=7)
        plt.show
