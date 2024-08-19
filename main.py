from graphics import Window, Line, Point
from cell import Cell
from maze import Maze
import random
import sys
import time


def main():
    sys.setrecursionlimit(100000)
    win = Window(1800, 800)

    scale = 210

    maze7 = Maze(20, 440, scale, scale, 200 / scale, 200 / scale, 0, seed=scale)
    maze8 = Maze(230, 440, scale, scale, 200 / scale, 200 / scale, 1, seed=scale)
    
    start = time.time()
    maze7.solve()
    end = time.time()
    time1 = int((end-start) * 1000)

    start = time.time()
    maze8.solve()
    end = time.time()
    time2 = int((end-start) * 1000)

    print("--------------------------")
    print(f"{scale}-by-{scale} DFS maze")
    print()
    output = "Time taken: {time:>6} ms".format(time = time1)
    print(output)
    output = "Cells visited: {time:>6}".format(time =maze7.get_cells_visited())
    print(output)
    output = "Comparisons: {time:>8}".format(time =maze7.comparisons)
    print(output)
    print("--------------------------")
    print(f"{scale}-by-{scale} BFS maze")
    print()
    output = "Time taken: {time:>6} ms".format(time = time2)
    print(output)
    output = "Cells visited: {time:>6}".format(time =maze8.get_cells_visited())
    print(output)
    output = "Comparisons: {time:>8}".format(time =maze8.comparisons)
    print(output)
    print()

    scale = 10

    maze1 = Maze(20, 20, scale, scale, 200 / scale, 200 / scale, 0, win, seed=scale)
    maze2 = Maze(230, 20, scale, scale, 200 / scale, 200 / scale, 1, win, seed=scale)

    maze1.solve()
    maze2.solve()

    scale = 20

    maze3 = Maze(20, 230, scale, scale, 200 / scale, 200 / scale, 0, win, seed=scale)
    maze4 = Maze(230, 230, scale, scale, 200 / scale, 200 / scale, 1, win, seed=scale)

    maze3.solve()
    maze4.solve()

    scale = 30

    maze5 = Maze(20, 440, scale, scale, 200 / scale, 200 / scale, 0, win, seed=scale)
    maze6 = Maze(230, 440, scale, scale, 200 / scale, 200 / scale, 1, win, seed=scale)

    maze5.solve()
    maze6.solve()

    for i in range(9):
        scale = 40 + i * 10
        r = i % 3
        c = int(i / 3)
        maze9 = Maze(440 + c * 420, 20 + r * 210, scale, scale, 200 / scale, 200 / scale, 0, win, seed=scale)
        maze10 = Maze(650 + c * 420, 20 + r * 210, scale, scale, 200 / scale, 200 / scale, 1, win, seed=scale)

        maze9.solve()
        maze10.solve()


    win.wait_for_close()


main()