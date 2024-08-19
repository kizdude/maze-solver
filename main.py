from graphics import Window, Line, Point
from cell import Cell
from maze import Maze
import random
import sys
import time


def main():
    sys.setrecursionlimit(3000)
    win = Window(1600, 800)

    scale = 60

    maze7 = Maze(20, 440, scale, scale, 200 / scale, 200 / scale, 0)
    maze8 = Maze(230, 440, scale, scale, 200 / scale, 200 / scale, 1)
    
    start = time.time()
    maze7.solve()
    end = time.time()
    print(f"Time taken to run the code was {end-start} seconds")

    start = time.time()
    maze8.solve()
    end = time.time()
    print(f"Time taken to run the code was {end-start} seconds")

    scale = 10

    maze1 = Maze(20, 20, scale, scale, 200 / scale, 200 / scale, 0, win)
    maze2 = Maze(230, 20, scale, scale, 200 / scale, 200 / scale, 1, win)

    maze1.solve()
    maze2.solve()

    scale = 20

    maze3 = Maze(20, 230, scale, scale, 200 / scale, 200 / scale, 0, win)
    maze4 = Maze(230, 230, scale, scale, 200 / scale, 200 / scale, 1, win)

    maze3.solve()
    maze4.solve()

    scale = 40

    maze5 = Maze(20, 440, scale, scale, 200 / scale, 200 / scale, 0, win)
    maze6 = Maze(230, 440, scale, scale, 200 / scale, 200 / scale, 1, win)

    maze5.solve()
    maze6.solve()



    win.wait_for_close()


main()