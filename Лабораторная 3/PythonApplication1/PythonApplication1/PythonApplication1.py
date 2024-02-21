# -*- coding:cp1251 -*-

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
class Rectangle:
    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        

    def area(self):
        width = self.top_right.x - self.bottom_left.x
        height = self.top_right.y - self.bottom_left.y
        return width * height

    def __str__(self):
        return f"Rectangle (bottom left: {self.bottom_left}, top right: {self.top_right})"


def find_intersection(point1, point2, point3, point4):
    # Проверка на параллельность
    if (point2.x - point1.x) * (point4.y - point3.y) == (point4.x - point3.x) * (point2.y - point1.y):
        return None  # Отрезки параллельны, нет пересечения
    
    t1 = ((point4.x - point3.x) * (point1.y - point3.y) - (point4.y - point3.y) * (point1.x - point3.x)) / ((point4.y - point3.y) * (point2.x - point1.x) - (point4.x - point3.x) * (point2.y - point1.y))
    t2 = ((point2.x - point1.x) * (point1.y - point3.y) - (point2.y - point1.y) * (point1.x - point3.x)) / ((point4.y - point3.y) * (point2.x - point1.x) - (point4.x - point3.x) * (point2.y - point1.y))

    # Проверка наличия точки пересечения внутри отрезков
    if 0 <= t1 <= 1 and 0 <= t2 <= 1:
        intersection_x = point1.x + t1 * (point2.x - point1.x)
        intersection_y = point1.y + t1 * (point2.y - point1.y)
        return intersection_x, intersection_y
    else:
        return None  # Точка пересечения не лежит внутри отрезков