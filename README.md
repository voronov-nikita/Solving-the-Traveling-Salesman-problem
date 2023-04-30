# Solving-the-Traveling-Salesman-problem
A repository for my solution of the traveling salesman problem by a programmatic method.


## **Content**
1. [About](/README.md#about)
2. [Example Code](/README.md#exaple-code)
3. [Useful Links](/README.md#useful-links)
4. [More Information](/README.md#more-inforamation)

## **About**

Solving the traveling salesman problem is a task whose main goal is to solve the problem of optimizing movement in space. To solve this problem, the _Python_ programming language was taken as incredibly easy to understand. When solving this problem, it is possible to optimize the delivery of certain goods, optimize and accelerate movement in space and, accordingly, have the largest number of resources at the end of the journey.

## **Example Code and other**
1. Сalculating the distance between two points:
    ```python
    def find_dist(cord1:tuple, cord2:tuple):
        if cord1 is cord2:
            return np.inf
        return np.sqrt((cord1[0]-cord2[0])**2 + (cord1[1]-cord2[1])**2)
    ```
2. Example grafic:

    ![graf1](/images/graf1.png)


## **Useful Links**

1. [python.org](https://python.org)
2. [ru.wikipedia.org - Задача комивояжера](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%BA%D0%BE%D0%BC%D0%BC%D0%B8%D0%B2%D0%BE%D1%8F%D0%B6%D1%91%D1%80%D0%B0#:~:text=%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0%20%D0%BA%D0%BE%D0%BC%D0%BC%D0%B8%D0%B2%D0%BE%D1%8F%D0%B6%D1%91%D1%80%D0%B0%20(%D0%B8%D0%BB%D0%B8%20TSP%20%D0%BE%D1%82,%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%BC%20%D0%B2%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%82%D0%BE%D0%BC%20%D0%B2%20%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9%20%D0%B3%D0%BE%D1%80%D0%BE%D0%B4.))

## **More Inforamation**

_The principle of operation_:
The first element is taken from the array with the coordinates of the points. Next, a search of options begins with a search of all possible options.

$$
P = (n-1)!
$$

Where _**P**_ - is the number of possible options. And _**n**_ - is the number of points in the array.

The point of start is a red point on grafics.

<br>

###### 29.04.2023 - the last change of README.md
