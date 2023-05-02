import numpy as np
import itertools as it

arr = np.array([(1, 2), (3, 4)])

for g in it.permutations(arr):
    for i in range(len(g)-1):
        print(g[i][0], g[i+1][0])

print(arr[1][0])