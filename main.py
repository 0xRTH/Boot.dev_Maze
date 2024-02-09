from graphics import Window, Point, Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 20, 20, 20, 20, win)
    maze.solve()
    win.wait_for_close()


main()
