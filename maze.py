from cell import Cell
import time
import random


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


    def _create_cells(self):
        self._cells = []
        for col in range(self.num_cols):
            new_row = []
            for row in range(self.num_rows):
                x1 = self.x1 + col * self.cell_size_x
                y1 = self.y1 + row * self.cell_size_y
                x2 = self.x1 + (col + 1) * self.cell_size_x
                y2 = self.y1 + (row + 1) * self.cell_size_y
                new_cell = Cell(x1, y1, x2, y2, self.win)
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
