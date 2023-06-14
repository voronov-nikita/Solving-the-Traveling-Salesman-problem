from time import time
from numba import *


def summa1(ls):
    k=0
    for i in range(len(ls)-1):
        for g in range(len(ls)-1):
            k += ls[i] * ls[g]

    return k


@jit
def summa2(ls):
    k=0
    for i in range(len(ls)-1):
        for g in range(len(ls)-1):
            k += ls[i] * ls[g]

    return k


list_example = [i for i in range(1000)]
start_1 = time()
summa1(list_example)
print(time() - start_1)

start_2 = time()
summa2(list_example)
print(time() - start_2)