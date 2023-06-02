import turtle 
from time import sleep

from main import FindMinWay

find_min_way = FindMinWay()

point_draw = turtle.Turtle(visible=False)
point_draw.pencolor("blue")
point_draw.pensize(4)
point_draw.speed(0)

k = turtle.Turtle()
k.pensize(2)
k.pencolor("red")
k.speed(1)


def draw_point(list_point:list, start_point:int):
    # point_draw.penup()
    for elem in range(len(list_point)):
        point_draw.pendown()
        if elem == start_point:
            point_draw.pencolor("red")
            k.penup()
            k.goto(list_point[elem][0], list_point[elem][1])
            k.pendown()
        else:
            point_draw.pencolor("blue")

        point_draw.penup()
        point_draw.goto(list_point[elem][0], list_point[elem][1])
        point_draw.pendown()
        point_draw.dot()
        
# <<<<<<<<<<<<<<<< START >>>>>>>>>>>>>>>>>
def draw_all_way():
    list_points = find_min_way.create_list_point(8, 0, -200, 200)

    draw_point(list_points, 0)
    try:
        for g in find_min_way.finally_variant(list_points, 0, True)[0]:
            k.goto(g[0], g[1])
    except:
        pass

    turtle.done()

draw_all_way()