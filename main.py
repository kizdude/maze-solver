from graphics import Window, Line, Point
from cell import Cell
from maze import Maze
import random


def main():
    win = Window(800, 800)

    maze = Maze(90, 90, 10, 10, 50, 50, win)

    win.wait_for_close()


main()