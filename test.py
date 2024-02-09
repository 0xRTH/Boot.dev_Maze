import unittest
from maze import Maze


class Test(unittest.TestCase):
    def test_maze_create_cell(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(5, 5, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_reset_validated(self):
        m1 = Maze(5, 5, 10, 10, 10, 10)
        for row in m1._cells:
            for cell in row:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
