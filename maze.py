import time
import random
from cell import Cell
from graphics import Point


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._create_maze()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited()

    def _create_maze(self):
        self._cells = []
        for i in range(0, self.__num_cols):
            row = []
            p1 = Point(self.__x1 + self.__cell_size_x * (i), self.__y1)
            for i in range(0, self.__num_rows):
                p2 = Point(p1.x + self.__cell_size_x, p1.y + self.__cell_size_y)
                cell = Cell(p1, p2, self.__win)
                row.append(cell)
                p1 = Point(p1.x, p1.y + self.__cell_size_y)
            self._cells.append(row)
        for col in self._cells:
            for cell in col:
                self._draw_cell(cell)

    def _draw_cell(self, cell):
        if self.__win is None:
            return
        cell.draw("black")
        self._animate()

    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_up_wall = False
        self._draw_cell(entrance_cell)
        exit_cell = self._cells[-1][-1]
        exit_cell.has_right_wall = False
        self._draw_cell(exit_cell)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            adjacent_cells = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            valid_adjacent_cells = [
                (x, y)
                for (x, y) in adjacent_cells
                if 0 <= x < self.__num_cols and 0 <= y < self.__num_rows
            ]
            possible_direction = [
                (x, y)
                for (x, y) in valid_adjacent_cells
                if not self._cells[x][y].visited
            ]
            if len(possible_direction) < 1:
                self._draw_cell(current)
                return
            next_cell_loc = random.choice(possible_direction)
            next_cell = self._cells[next_cell_loc[0]][next_cell_loc[1]]
            if next_cell_loc[0] > i:
                current.has_right_wall = False
                next_cell.has_left_wall = False
            elif next_cell_loc[0] < i:
                current.has_left_wall = False
                next_cell.has_right_wall = False
            elif next_cell_loc[1] > j:
                current.has_down_wall = False
                next_cell.has_up_wall = False
            elif next_cell_loc[1] < j:
                current.has_up_wall = False
                next_cell.has_down_wall = False
            self._draw_cell(current)
            self._draw_cell(next_cell)

            self._break_walls_r(next_cell_loc[0], next_cell_loc[1])

    def _reset_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _is_path_clear(self, cell, dir):
        if dir == "l" and not cell.has_left_wall:
            return True
        if dir == "r" and not cell.has_right_wall:
            return True
        if dir == "d" and not cell.has_down_wall:
            return True
        if dir == "u" and not cell.has_up_wall:
            return True
        return False

    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        if current == self._cells[-1][-1]:
            return True
        dirs = {"r": (i + 1, j), "l": (i - 1, j), "d": (i, j + 1), "u": (i, j - 1)}
        for dir in dirs:
            if (
                0 <= dirs[dir][0] < self.__num_cols
                and 0 <= dirs[dir][1] < self.__num_rows
                and self._is_path_clear(current, dir)
            ):
                print("possible dir: ", dirs[dir])
                next_cell = self._cells[dirs[dir][0]][dirs[dir][1]]
                if not next_cell.visited:
                    current.draw_move(next_cell)
                    if self._solve_r(dirs[dir][0], dirs[dir][1]):
                        return True
                    else:
                        current.draw_move(next_cell, True)
        return False
