# -*- coding:cp1251 -*-

def find_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    # Проверка на параллельность
    if (x2 - x1) * (y4 - y3) == (x4 - x3) * (y2 - y1):
        return None  # Отрезки параллельны, нет пересечения
    
    t1 = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
    t2 = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))

    # Проверка наличия точки пересечения внутри отрезков
    if 0 <= t1 <= 1 and 0 <= t2 <= 1:
        intersection_x = x1 + t1 * (x2 - x1)
        intersection_y = y1 + t1 * (y2 - y1)
        return intersection_x, intersection_y
    else:
        return None  # Точка пересечения не лежит внутри отрезков