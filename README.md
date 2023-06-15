# Solving-the-Traveling-Salesman-problem
A repository for my solution of the traveling salesman problem by a programmatic method.


## **Content**
1. [About](/README.md#about)
2. [Example Code](/README.md#example-code-and-other)
3. [Useful Links](/README.md#useful-links)
4. [More Information](/README.md#more-inforamation)

## **About**

Solving the traveling salesman problem is a task whose main goal is to solve the problem of optimizing movement in space. To solve this problem, the _Python_ programming language was taken as incredibly easy to understand. When solving this problem, it is possible to optimize the delivery of certain goods, optimize and accelerate movement in space and, accordingly, have the largest number of resources at the end of the journey.

Now, for the convenience of simple use, a _Python desktop application script_ has appeared. When the application starts, a window will appear with the data that the user must enter manually. After that, you need to press the **START** button and wait a little. After identifying the shortest route, two new windows will open. _The first window_ contains information about the code execution time and the total route length in conventional units. _The second window_ is designed to display the route itself on the _graph_.

## **Example Code and other**
1. Сalculating the distance between two points:
    ```python
    def find_dist(cord1:tuple, cord2:tuple):
        if cord1 is cord2:
            return np.inf
        return np.sqrt((cord1[0]-cord2[0])**2 + (cord1[1]-cord2[1])**2)
    ```
2. calculating the best route by array points with a return return to the sending point or not, the dependence is revealed on the value of the variable _RETURN_START_POINT_.
    ```python
    def create_dict_varios(ls:list, start_point:int) -> dict:
    dict_varios = dict()
    fixed_point = ls[start_point]
    copy_ls = (ls[:start_point] + ls[start_point+1:])
    for g in permutations(copy_ls):
        if RETURN_START_POINT:
            g = (fixed_point, ) + g + (fixed_point, )
        else:
            g = (fixed_point, ) + g
        s=sum([find_dist(g[i], g[i+1]) for i in range(len(g)-1)])

        dict_varios[g] = s
    
    return dict_varios
    ```
3. Example grafic:

    ![graf1](/images/graf1.png)

    This is a graph consisting of 5 points, optimization is minimal. The entire range changes from -1 to 1. The range is changed manually in code cycles.

    ![graf2](/images/graf-10-point.png)

    This is a graph consisting of 10 points, optimization is maximum. The entire range changes from -1 to 1.The range changes in the code`s header.

4. Example Application:

![app](/images/app1.png)

This is an example of what the app looks like. It is made on the PyQt5 framework using CSS styles.

5. Example with turtle:

![turtle](/images/turtle-examle.png)


## **Useful Links**

1. [python - python.org](https://python.org)
2. [Задача комивояжера - wikipedia](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%BA%D0%BE%D0%BC%D0%BC%D0%B8%D0%B2%D0%BE%D1%8F%D0%B6%D1%91%D1%80%D0%B0#:~:text=%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0%20%D0%BA%D0%BE%D0%BC%D0%BC%D0%B8%D0%B2%D0%BE%D1%8F%D0%B6%D1%91%D1%80%D0%B0%20(%D0%B8%D0%BB%D0%B8%20TSP%20%D0%BE%D1%82,%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%BC%20%D0%B2%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%82%D0%BE%D0%BC%20%D0%B2%20%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9%20%D0%B3%D0%BE%D1%80%D0%BE%D0%B4.))
3. [Matplotlib: Научная графика в Python](https://pythonworld.ru/novosti-mira-python/scientific-graphics-in-python.html)

## **More Inforamation**

_The principle of operation_:
The first element is taken from the array with the coordinates of the points. Next, a search of options begins with a search of all possible options. 

$$
P = (n-1)!
$$

Where _**P**_ - is the number of possible options. And _**n**_ - is the number of points in the array.

The point of start is a red point on grafics.

You can read the [development log](/DevelopmentLog.md) posted in the same repository.

<br></n>

###### 15.06.2023 - the last change of README.md
