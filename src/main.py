from random import uniform
import matplotlib.pyplot as plt
from itertools import permutations
import time


# count the point (the best is 11)
COUNT_POINT:int = 9
# random number accuracy (number of decimal places)
ICONIC_ACCURACY:int = 0
# position points (cords)
MIN_POSITION:float = -10
MAX_POSITION:float = 10

# <--------- Additional parameters --------->
RETURN_START_POINT:bool = True
START_POINT:int = 0

# created SEED to compare the efficiency of algorithms
# seed(42)

class FindMinWay():

    def __init__(self):
        self.start_timer = time.time()
        self.execution_time = None

    def create_list_point(self, size_list:int, round_value:int, min_position:int, max_position:int):
        # create list with tuple of cords (random values)
        list_point = [
            (round(uniform(min_position, max_position), round_value), round(uniform(min_position, max_position), round_value)) for _ in range(size_list)
        ]
        return list_point

    def find_dist(self, cord1:tuple, cord2:tuple) -> float:
        return ((cord1[0]-cord2[0])**2 + (cord1[1]-cord2[1])**2)**0.5


    def create_dict_varios(self, ls:list, start_point:int, return_start_point:bool) -> dict:
        dict_varios = dict()
        fixed_point = ls[start_point]
        copy_ls = (ls[:start_point] + ls[start_point+1:])
        for g in permutations(copy_ls):
            if return_start_point:
                g = (fixed_point, ) + g + (fixed_point, )
            else:
                g = (fixed_point, ) + g
            s=sum([self.find_dist(g[i], g[i+1]) for i in range(len(g)-1)])

            dict_varios[g] = s
        
        return dict_varios


    def finally_variant(self, ls:list, start:int, return_start_point:bool):
        new_varios = self.create_dict_varios(ls, start, return_start_point)
        min_value = min(new_varios.values())

        for key, value in new_varios.items():
            if value == min_value:
                return (list(key), value)
        return ([], 0)
    
    def get_execution_time(self):
        if self.execution_time is not None:
            return self.execution_time
        return 0
    
    def show_way(self, data_list:tuple, start_point:int):

        len_way = data_list[1]
        x = [cord[0] for cord in data_list[0]]
        y = [cord[1] for cord in data_list[0]]

        end_timer = time.time()

        self.execution_time = end_timer - self.start_timer

        print("="*130)
        print(f"TIME: {round(self.execution_time, 2)} sec")
        # print(f"THE START POINT: {list_point[start_point]}")
        print(f"LEN ALL WAY: {len_way}")
        print("="*130)

        plt.plot(x, y)
        # plt.grid(True)
        plt.scatter(x, y)
        plt.scatter(x[-1], y[-1], color="red")
        plt.show()


            


# create grafwith tuple of cords
graf_point = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, 0), (1, 1), (1, -1)
]


# <------------------ Build the Way ------------------>
if __name__=="__main__":

    minway = FindMinWay()
    list_point = minway.create_list_point(COUNT_POINT, ICONIC_ACCURACY, MIN_POSITION, MAX_POSITION)
    result_function = minway.finally_variant(list_point, START_POINT, RETURN_START_POINT)
    new_list = result_function
    minway.show_way(new_list, START_POINT)

    