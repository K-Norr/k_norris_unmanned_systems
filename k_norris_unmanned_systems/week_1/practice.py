import matplotlib.pyplot as plt

#test

class node:
    def __init__(self, x, y, parent_cost, index):
        self.x = x
        self.y = y
        self.cost = parent_cost
        self.index = index


      
maxx = 10
maxy = 10
gridsize = 0.5
lenx = (maxx / gridsize) + 1
leny = (maxy / gridsize) + 1

def find_index(x,y):
    found_index = (x / gridsize) + ((y / gridsize) * lenx)  
    return found_index

def find_x(index):
    found_x = (index % lenx)*gridsize
    return found_x

def find_y(index):
    found_y = (((index - (index % lenx)) / leny)*gridsize)
    return found_y


print(find_index(5.5,1))

for i in range(int(lenx)):
    for j in range(int(leny)):
        temp_x = i * gridsize
        temp_y = j * gridsize
        temp_index = find_index(temp_x,temp_y)
        plt.plot(temp_x,temp_y)
        plt.text(temp_x, temp_y, str(int(temp_index)), color="red", fontsize=7)
        plt.show