from random import uniform
import numpy as np
import matplotlib.pyplot as plt
import itertools as it

# count the point (the best is 10)
COUNT_POINT = 10
# random number accuracy (number of decimal places)
ICONIC_ACCURACY = 10


def find_dist(cord1:tuple, cord2:tuple):
    if cord1 is cord2:
        return np.inf
    return np.sqrt((cord1[0]-cord2[0])**2 + (cord1[1]-cord2[1])**2)


def create_dict_varios(ls:list):
    dict_varios = dict()
    for j in range(COUNT_POINT):
        fixed_point = ls[j]
        for g in it.permutations(ls):
            s=0
            g = list(g)
            del g[g.index(fixed_point)]
            g.insert(0, fixed_point)
            g = tuple(g)
            for i in range(len(g)-1):
                s += find_dist(g[i], g[i+1])
            dict_varios[g] = (s, fixed_point)
    
    return dict_varios


def finally_variant(ls:list):
    new_varios = create_dict_varios(ls)
    min_value = min(new_varios.values())[0]

    for key, value in new_varios.items():
        if value[0] == min_value:
            return list(key), value[0], value[1]
        

# create list with tuple of cords (random values)
list_point = [
    (np.round(uniform(-1, 1), ICONIC_ACCURACY), np.round(uniform(-1, 1), ICONIC_ACCURACY)) for _ in range(COUNT_POINT)
]


# <------------------ Build the Way ------------------>

new_list = finally_variant(list_point)
new_list[0].append(new_list[2])

len_way = new_list[1]
x = [cord[0] for cord in new_list[0]]
y = [cord[1] for cord in new_list[0]]

print(len_way)

plt.plot(x, y)
plt.scatter(x, y)
plt.scatter(x[-1], y[-1], color="red")
plt.show()