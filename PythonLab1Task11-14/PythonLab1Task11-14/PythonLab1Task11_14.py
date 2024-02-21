# -*- coding:cp1251 -*-

def SortByAvgAsciiWeight(strings):
    return sorted(strings, key=lambda x: sum(map(ord, x))/len(x))

def SortByMedianAsciiDifference(strings):
    def median_difference(s):
        sorted_chars = sorted(map(ord, s))
        median_index = len(sorted_chars) // 2
        return abs(sorted_chars[median_index] - sorted_chars[median_index-1])

    return sorted(strings, key=median_difference)

def SortByQuadDeviation(strings):
    def quad_deviation(s):
        middle = len(s) // 2
        mirror_pairs = zip(s[:middle], reversed(s[middle:]))
        return sum((ord(a) - ord(b))**2 for a, b in mirror_pairs)

    return sorted(strings, key=quad_deviation)

