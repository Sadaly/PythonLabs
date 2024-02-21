# -*- coding:cp1251 -*-

def SortByAvgAsciiWeight(strings):
    return sorted(strings, key=lambda x: sum(map(ord, x))/len(x))

