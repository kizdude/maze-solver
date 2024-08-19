from cell import Cell
import time
import random
from graphics import Line, Point


class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
        ):
        if seed != None:
            random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls()


    def _create_cells(self):
        self._cells = []
        for col in range(self.num_cols):
            new_row = []
            for row in range(self.num_rows):
                x1 = self.x1 + col * self.cell_size_x
                y1 = self.y1 + row * self.cell_size_y
                x2 = self.x1 + (col + 1) * self.cell_size_x
                y2 = self.y1 + (row + 1) * self.cell_size_y
                new_cell = Cell(x1, y1, x2, y2, col, row, self.win)
                new_row.append(new_cell)
            self._cells.append(new_row)

        if self.win == None:
            return
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self.win == None:
            return
        self._cells[i][j].draw()
        self._animate()


    def _animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(0.02)


    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        bottom_right_cell = self._cells[self.num_cols - 1][self.num_rows - 1]
        top_left_cell.has_top_wall = False
        self._draw_cell(0, 0)
        bottom_right_cell.has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)


    def _break_walls(self):
        self._cells[0][0]._break_walls_r(0, 0, self)


    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if i == self.num_cols - 1 and j == self.num_rows:
            return True
        
        # left
        if not i - 1 < 0:
            if not current_cell.has_left_wall and self._cells[i - 1][j].visited == False:
                self._draw_move(i, j, to_cell_i, to_cell_j)
                self._solve_r(i - 1, j)

    def _draw_move(self, from_i, from_j, to_i, to_j):
        point_from = Point(from_i, from_j)
        move_line = Line()