import numpy as np

def find_dist(cord1:tuple, cord2:tuple):
    return np.sqrt((cord1[0]-cord2[0])**2 + (cord1[1]-cord2[1])**2)


cord1=  (1, 1)
cord2 = (-1, -1)

print(find_dist(cord1, cord2))