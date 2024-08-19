from graphics import Window, Line, Point
import random

class Cell():
    def __init__(self, x1, y1, x2, y2, col, row, win : Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.col = col
        self.row = row
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self):
        if self._win == None:
            return
        top_left = Point(self._x1, self._y1)
        bottom_left = Point(self._x1, self._y2)
        top_right = Point(self._x2, self._y1)
        bottom_right = Point(self._x2, self._y2)
        left_wall = Line(top_left, bottom_left)
        right_wall = Line(top_right, bottom_right)
        top_wall = Line(top_left, top_right)
        bottom_wall = Line(bottom_left, bottom_right)

        if self.has_left_wall:
            self._win.draw_line(left_wall, "red")
        else:
            self._win.draw_line(left_wall, "white")
        if self.has_right_wall:           
            self._win.draw_line(right_wall, "red")
        else:
            self._win.draw_line(right_wall, "white")
        if self.has_top_wall:
            self._win.draw_line(top_wall, "red")
        else:
            self._win.draw_line(top_wall, "white")
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, "red")
        else:
            self._win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        cell_1_mid_x = (self._x1 + self._x2) / 2
        cell_2_mid_x = (to_cell._x1 + to_cell._x2) / 2
        cell_1_mid_y = (self._y1 + self._y2) / 2
        cell_2_mid_y = (to_cell._y1 + to_cell._y2) / 2
        from_point = Point(cell_1_mid_x, cell_1_mid_y)
        to_point = Point(cell_2_mid_x, cell_2_mid_y)
        move_line = Line(from_point, to_point)
        if undo:
            line_colour = "gray"
        else:
            line_colour = "red"
        self._win.draw_line(move_line, line_colour)

    def _break_walls_r(self, i, j, maze):
        self.visited = True
        while True:
            to_visit = []
            if not j - 1 < 0:
                top_cell = maze._cells[i][j - 1]
                if top_cell.visited == False:
                    to_visit.append((i, j - 1))
            if not j + 1> maze.num_rows - 1:
                bottom_cell = maze._cells[i][j + 1]
                if bottom_cell.visited == False:
                    to_visit.append((i, j + 1))
            if not i - 1 < 0:
                left_cell = maze._cells[i - 1][j]
                if left_cell.visited == False:
                    to_visit.append((i - 1, j))
            if not i + 1 > maze.num_cols - 1:
                right_cell = maze._cells[i + 1][j]
                if right_cell.visited == False:
                    to_visit.append((i + 1, j))

            if len(to_visit) == 0:
                self.draw()
                return
            else:
                direction = random.randint(0, len(to_visit) - 1)
                cell_to_i, cell_to_j = to_visit[direction]

                # break above
                if cell_to_j < j:
                    self.has_top_wall = False
                    maze._cells[cell_to_i][cell_to_j].has_bottom_wall = False

                # break below
                if cell_to_j > j:
                    self.has_bottom_wall = False
                    maze._cells[cell_to_i][cell_to_j].has_top_wall = False

                # break left
                if cell_to_i < i:
                    self.has_left_wall = False
                    maze._cells[cell_to_i][cell_to_j].has_right_wall = False

                # break right
                if cell_to_i > i:
                    self.has_right_wall = False
                    maze._cells[cell_to_i][cell_to_j].has_left_wall = False

                maze._cells[cell_to_i][cell_to_j]._break_walls_r(cell_to_i, cell_to_j, maze)



