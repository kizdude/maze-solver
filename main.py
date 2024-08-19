from graphics import Window, Line, Point
from cell import Cell
from maze import Maze
import random
import sys


def main():
    sys.setrecursionlimit(3000)
    win = Window(800, 800)

    maze1 = Maze(20, 90, 10, 10, 20, 20, win, 0)
    maze1.solve()

    maze1 = Maze(300, 90, 10, 10, 20, 20, win, 1)
    maze1.solve()

    maze1 = Maze(20, 300, 50, 50, 5, 5, win, 0)
    maze1.solve()

    maze1 = Maze(300, 300, 50, 50, 5, 5, win, 1)
    maze1.solve()

    win.wait_for_close()


main()