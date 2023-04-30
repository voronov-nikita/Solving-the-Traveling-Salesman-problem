# Development Log

- [x] 29.04.2023 (part 1):

    *Changes*:
    - Created a repository
    - uploaded highlights to README.md
    - wrote a small code for the solution.

    *Problems*:
    - incorrect path finding (has the ability to go back to the previous point)

- [x] 29.04.2023 (part 2):

    *Changes*:
    - Delete a part of code
    - Add new varios of code
    - Add new line for task

    *Problems*:
    - incorrect path finding (has the ability to go back to the previous point)
    - ~~lose the point (from 5 point after - 4)~~


- [x] 30.04.2023:

    *Tests have been carried out*:

    | Coint Point | Time (sec) | Result (satisfaction with the option, %)   |
    |-------|-----------|----------|
    | 2     |   1,81    | 100%   |
    | 3     |   1,65    | 100%   |
    | 4     |   2,07    | 100%   |
    | 5     |   2,18    |  100%  |
    | 6     |   2,47    |  100%  |
    | 7     |   2,77    |  99%   |
    | 8     |   9,22    |  100%  |
    | 9     |   94,97   |  90%   |

    - Moving on is too slow!

    - After a small change in the code (removed the transformation of the tuple into a list) the code began to work on average 20-30 milliseconds faster

- [x] 01.05.2023:

    - added code optimization, namely reducing the number of useless devices by 1, which simplifies the counting process from ```n!``` to ```(n-1)!```


