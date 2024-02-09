from graphics import Line, Point


class Cell:
    def __init__(self, p1, p2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_up_wall = True
        self.has_down_wall = True
        self.__x1 = p1.x
        self.__x2 = p2.x
        self.__y1 = p1.y
        self.__y2 = p2.y
        self.visited = False
        self.__win = win

    def draw(self, fill_color):
        if self.has_left_wall:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)),
                fill_color,
            )
        else:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)),
                self.__win._bg_color,
            )
        if self.has_right_wall:
            self.__win.draw_line(
                Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)),
                fill_color,
            )
        else:
            self.__win.draw_line(
                Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)),
                self.__win._bg_color,
            )
        if self.has_up_wall:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)),
                fill_color,
            )
        else:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)),
                self.__win._bg_color,
            )
        if self.has_down_wall:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)),
                fill_color,
            )
        else:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)),
                self.__win._bg_color,
            )

    def draw_move(self, to_cell, undo=False):
        middle_self = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
        middle_next = Point(
            ((to_cell.__x1 + to_cell.__x2) / 2), ((to_cell.__y1 + to_cell.__y2) / 2)
        )
        if not undo:
            self.__win.draw_line(Line(middle_self, middle_next), "red")
        else:
            self.__win.draw_line(Line(middle_self, middle_next), "gray50")
