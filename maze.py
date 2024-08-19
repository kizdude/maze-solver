from cell import Cell
import time
import random
from graphics import Line, Point
import math


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
            search=0,
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
        self.search = search
        self.delay = 2 ** (num_cols * num_rows)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls()
        self._reset_cells_visited()


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
        self._animate(10)


    def _animate(self, speed=1):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(1 / self.delay / speed / 20)


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

    def _count_cells_visited(self):
        count = 0
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                if self._cells[i][j].visited:
                    count += 1
        return count

    def solve(self):
        if self.search == 0:
            self._solve_depth_first_r(0, 0)
            visited = self._count_cells_visited()
            print(f"depth first search visited {visited} cells")
        if self.search == 1: 
            self._solve_breadth_first(0, 0)
            visited = self._count_cells_visited()
            print(f"breadth first search visited {visited} cells")
        
        


    def _solve_depth_first_r(self, i, j, depth=0):
        self._animate(1)

        current_cell = self._cells[i][j]
        current_cell.visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        # left
        if not i - 1 < 0:
            to_cell = self._cells[i - 1][j]
            if not current_cell.has_left_wall and to_cell.visited == False:
                if i - 1 == self.num_cols - 1 and j == self.num_rows:
                    return True
                current_cell.draw_move(to_cell, depth)
                if self._solve_depth_first_r(i - 1, j, depth + 1):
                    return True
                current_cell.draw_move(to_cell, depth, True)

        # right
        if not i + 1 > self.num_cols - 1:
            to_cell = self._cells[i + 1][j]
            if not current_cell.has_right_wall and to_cell.visited == False:
                if i + 1 == self.num_cols - 1 and j == self.num_rows:
                    return True
                current_cell.draw_move(to_cell, depth)
                if self._solve_depth_first_r(i + 1, j, depth + 1):
                    return True
                current_cell.draw_move(to_cell, depth, True)

        # up
        if not j - 1 < 0:
            to_cell = self._cells[i][j - 1]
            if not current_cell.has_top_wall and to_cell.visited == False:
                if i == self.num_cols and j - 1 == self.num_rows:
                    return True
                current_cell.draw_move(to_cell, depth)
                if self._solve_depth_first_r(i, j - 1, depth + 1):
                    return True
                current_cell.draw_move(to_cell, depth, True)

        # down
        if not j + 1 > self.num_rows - 1:
            to_cell = self._cells[i][j + 1]
            if not current_cell.has_bottom_wall and to_cell.visited == False:
                if i == self.num_cols and j + 1 == self.num_rows:
                    return True
                current_cell.draw_move(to_cell, depth)
                if self._solve_depth_first_r(i, j + 1, depth + 1):
                    return True
                current_cell.draw_move(to_cell, depth, True)
        
        return False

    def _solve_breadth_first(self, i, j):
        self._animate(1)
        to_visit = []
        depth = 0
        current_cell = self._cells[i][j]

        cell_and_depth = (current_cell, depth)
        to_visit.append(cell_and_depth)

        while len(to_visit) > 0:
            self._animate(1)

            current_cell_and_depth = to_visit.pop(0)
            current_cell = current_cell_and_depth[0]
            current_depth = current_cell_and_depth[1]

            current_cell.visited = True
            i = current_cell.col
            j = current_cell.row

            if i == self.num_cols - 1 and j == self.num_rows - 1:
                return True

            # left
            if not i - 1 < 0:
                neighbour_cell = self._cells[i - 1][j]
                if not current_cell.has_left_wall and neighbour_cell.visited == False and neighbour_cell not in to_visit:
                    current_cell.draw_move(neighbour_cell, depth)
                    neighbour_cell_and_depth = (neighbour_cell, depth)
                    to_visit.append(neighbour_cell_and_depth)

            # right
            if not i + 1 > self.num_cols - 1:
                neighbour_cell = self._cells[i + 1][j]
                if not current_cell.has_right_wall and neighbour_cell.visited == False and neighbour_cell not in to_visit:
                    current_cell.draw_move(neighbour_cell, depth)
                    neighbour_cell_and_depth = (neighbour_cell, depth)
                    to_visit.append(neighbour_cell_and_depth)

            # up
            if not j - 1 < 0:
                neighbour_cell = self._cells[i][j - 1]
                if not current_cell.has_top_wall and neighbour_cell.visited == False and neighbour_cell not in to_visit:
                    current_cell.draw_move(neighbour_cell, depth)
                    neighbour_cell_and_depth = (neighbour_cell, depth)
                    to_visit.append(neighbour_cell_and_depth)

            # down
            if not j + 1 > self.num_rows - 1:
                neighbour_cell = self._cells[i][j + 1]
                if not current_cell.has_bottom_wall and neighbour_cell.visited == False and neighbour_cell not in to_visit:
                    current_cell.draw_move(neighbour_cell, depth)
                    neighbour_cell_and_depth = (neighbour_cell, depth)
                    to_visit.append(neighbour_cell_and_depth)
            
            depth += 1
        
        return False