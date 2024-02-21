# -*- coding:cp1251 -*-

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
def segment_length(point1, point2):
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5   

class Rectangle:
    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    def area(self):
        width = segment_length(self.top_left, self.top_right)
        height = segment_length(self.top_left, self.bottom_left)
        return width * height

    def __str__(self):
        return f"Прямоугольник (A: {self.top_left}, B: {self.top_right}, C: {self.bottom_left}, D: {self.bottom_right})"
    
class Quad:
    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    def area(self):
        width = segment_length(self.top_left, self.top_right)
        return width * width

    def __str__(self):
        return f"Квадрат (A: {self.top_left}, B: {self.top_right}, C: {self.bottom_left}, D: {self.bottom_right})"

def compare(t1, t2):
    area1 = t1.area()
    area2 = t2.area()
    
    if (area1 > area2):
        print(f'{t1} больше {t2}')
    elif (area1 == area2):
        print(f'{t1} равен {t2}')
    elif (area1 < area2):
        print(f'{t1} меньше {t2}')
        
def is_intersect(t1, t2):
    def find_intersection(point1, point2, point3, point4): # Проверяем пересекаются ли 2 отрезка
        # Проверка на параллельность
        if (point2.x - point1.x) * (point4.y - point3.y) == (point4.x - point3.x) * (point2.y - point1.y):
            return False  # Отрезки параллельны, нет пересечения
        
        t1 = ((point4.x - point3.x) * (point1.y - point3.y) - (point4.y - point3.y) * (point1.x - point3.x)) / ((point4.y - point3.y) * (point2.x - point1.x) - (point4.x - point3.x) * (point2.y - point1.y))
        t2 = ((point2.x - point1.x) * (point1.y - point3.y) - (point2.y - point1.y) * (point1.x - point3.x)) / ((point4.y - point3.y) * (point2.x - point1.x) - (point4.x - point3.x) * (point2.y - point1.y))

        # Проверка наличия точки пересечения внутри отрезков
        if 0 <= t1 <= 1 and 0 <= t2 <= 1:
            intersection_x = point1.x + t1 * (point2.x - point1.x)
            intersection_y = point1.y + t1 * (point2.y - point1.y)
            return True
        else:
            return False  # Точка пересечения не лежит внутри отрезков
        
    def is_segment_intersect_figure(point1, point2, t1): # Проверяем пересекает ли отрезок фигуру
        intersection1 = find_intersection(point1, point2, t1.top_left, t1.top_right)
        intersection2 = find_intersection(point1, point2, t1.top_right, t1.bottom_right)
        
        intersection3 = find_intersection(point1, point2, t1.bottom_right, t1.bottom_left)
        intersection4 = find_intersection(point1, point2, t1.bottom_left, t1.top_left)
           
        return intersection1 or intersection2 or intersection3 or intersection4
    
    intersection1 = is_segment_intersect_figure(t1.top_left, t1.top_right, t2)
    intersection2 = is_segment_intersect_figure(t1.top_right, t1.bottom_right, t2)
    
    intersection3 = is_segment_intersect_figure(t1.bottom_right, t1.bottom_left, t2)
    intersection4 = is_segment_intersect_figure(t1.bottom_left, t1.top_left, t2)
    
    return intersection1 or intersection2 or intersection3 or intersection4 

