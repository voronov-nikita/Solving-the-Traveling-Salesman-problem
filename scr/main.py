from random import uniform, seed
import numpy as np
import matplotlib.pyplot as plt
import itertools as it


# count the point (the best is 10)
COUNT_POINT = 10
# random number accuracy (number of decimal places)
ICONIC_ACCURACY = 2
# position points (cords)
MIN_POSITION = -1
MAX_POSITION = 1

# created SEED to compare the efficiency of algorithms
# seed(42)


def find_dist(cord1:tuple, cord2:tuple):
    return np.sqrt((cord1[0]-cord2[0])**2 + (cord1[1]-cord2[1])**2)


def create_dict_varios(ls:list):
    dict_varios = dict()
    for j in range(COUNT_POINT):
        fixed_point = ls[j]
        ind_fixed_point = ls.index(fixed_point)
        copy_ls = (ls[:ind_fixed_point] + ls[ind_fixed_point+1:])
        for g in it.permutations(copy_ls):
            s=0
            g = (fixed_point, ) + g + (fixed_point, )
            for i in range(len(g)-1):
                s += find_dist(g[i], g[i+1])
            dict_varios[g] = s
    
    return dict_varios


def finally_variant(ls:list):
    new_varios = create_dict_varios(ls)
    min_value = min(new_varios.values())

    for key, value in new_varios.items():
        if value == min_value:
            return list(key), value
        

# create list with tuple of cords (random values)
list_point = [
    (np.round(uniform(MIN_POSITION, MAX_POSITION), ICONIC_ACCURACY), np.round(uniform(MIN_POSITION, MAX_POSITION), ICONIC_ACCURACY)) for _ in range(COUNT_POINT)
]


# <------------------ Build the Way ------------------>
new_list=[[(0,0)]*10]

result_function = finally_variant(list_point)
if result_function is not None:
    new_list = result_function


len_way = new_list[1]
x = [cord[0] for cord in new_list[0]]
y = [cord[1] for cord in new_list[0]]

print(f"LEN ALL WAY: {len_way}")

plt.plot(x, y)
plt.scatter(x, y)
plt.scatter(x[-1], y[-1], color="red")
plt.show()