# -*- coding:cp1251 -*-

def SortByAvgAsciiWeight(strings):
    return sorted(strings, key=lambda x: sum(map(ord, x))/len(x))

def SortByMedianAsciiDifference(strings):
    def median_difference(s):
        sorted_chars = sorted(map(ord, s))
        median_index = len(sorted_chars) // 2
        return abs(sorted_chars[median_index] - sorted_chars[median_index-1])

    return sorted(strings, key=median_difference)
