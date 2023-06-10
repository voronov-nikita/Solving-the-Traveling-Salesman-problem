import turtle 
from time import sleep

from main import FindMinWay

find_min_way = FindMinWay()

class Run():
    point_draw = turtle.Turtle(visible=False)
    point_draw.pencolor("blue")
    point_draw.pensize(4)
    point_draw.speed(0)

    k = turtle.Turtle()
    k.pensize(2)
    k.pencolor("red")
    k.speed(1)


    def draw_point(self, list_point:list, start_point:int):
        # point_draw.penup()
        for elem in range(len(list_point)):
            self.point_draw.pendown()
            if elem == start_point:
                self.point_draw.pencolor("red")
                self.k.penup()
                self.k.goto(list_point[elem][0], list_point[elem][1])
                self.k.pendown()
            else:
                self.point_draw.pencolor("blue")

            self.point_draw.penup()
            self.point_draw.goto(list_point[elem][0], list_point[elem][1])
            self.point_draw.pendown()
            self.point_draw.dot()
            
    # <<<<<<<<<<<<<<<< START >>>>>>>>>>>>>>>>>
    def draw_all_way(self, count_point:int, round_value:int, min_position:int, max_position:int, start_point:int, return_back:bool=True):
        list_points = find_min_way.create_list_point(count_point,
                                                    round_value, 
                                                    min_position, 
                                                    max_position,)

        self.draw_point(list_points, 0)
        # try:
        for g in find_min_way.finally_variant(list_points, start_point, return_back)[0]:
            self.k.goto(g[0], g[1])
        # except :
            # pass

        turtle.done()

run = Run()
run.draw_all_way(6, 6, -100, 100, 0)
