# -*- coding: utf-8 -*-
"""
Problem 2 - Week 1 - Declaring node class
Created on Tue Aug 30 22:59:24 2022

@author: kanor
"""

#declaration of node class with 4 variables:
#x position, y position, parent cost and node index

class node:
    def __init__(self, x, y, parent_cost, index):
        self.x = x
        self.y = y
        self.cost = parent_cost
        self.index = index