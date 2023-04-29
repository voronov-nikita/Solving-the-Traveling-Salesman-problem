from random import uniform
import numpy as np
import matplotlib.pyplot as plt

# колличество точек при решении задачи
COUNT_POINT = 5
# точность случаного числа (количесво знаков после запятой)
ICONIC_ACCURACY = 10


def find_dist(cord1:tuple, cord2:tuple):
    print(cord1, cord2)
    if cord1 is cord2:
        return np.inf
    return np.sqrt((cord1[0]-cord2[0])**2 + (cord1[1]-cord2[1])**2)


def find_min_dist(start:tuple, all_list:list):
    dict_point=dict()
    for elem in range(len(all_list)):
        dict_point[all_list[elem]] = find_dist(start, all_list[elem])

    min_value = min(dict_point.values())

    for k, v in dict_point.items():
        if v==min_value:
            list_point.remove(k)
            return k, v


list_point = [
    (np.round(uniform(-1, 1), ICONIC_ACCURACY), np.round(uniform(-1, 1), ICONIC_ACCURACY)) for _ in range(COUNT_POINT)
]

m = tuple(sorted(list_point)[0])
slx=[]
sly=[]
s=0
for _ in range(COUNT_POINT):
    # print(m, "->", find_min_dist(m, list_point, list_without_repeate))
    m1 = find_min_dist(m, list_point)
    s+= m1[1]
    m = m1[0]
    print(m, m1[1])
    slx.append(m[0])
    sly.append(m[1])
print(s)

plt.plot(slx, sly)
plt.scatter(slx, sly)
plt.show()


