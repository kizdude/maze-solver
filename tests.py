import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    
    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        m1._break_entrance_and_exit()
        top_left_cell = m1._cells[0][0]
        bottom_right_cell = m1._cells[num_cols - 1][num_rows - 1]
        self.assertEqual(top_left_cell.has_top_wall, False)
        self.assertEqual(bottom_right_cell.has_bottom_wall, False)

    def test_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        m1._break_entrance_and_exit()
        m1._break_walls()
        m1._reset_cells_visited()
        for col in range(num_cols):
            for row in range(num_rows):
                self.assertEqual(m1._cells[col][row].visited, False)

if __name__ == "__main__":
    unittest.main()