# -*- coding:cp1251 -*-
from collections import Counter

def FindUniqueElement(arr):
    counter = Counter(arr)
    for num, count in counter.items():
        if count == 1:
            return num
    return None

def FindTwoMinElements(arr):
    if len(arr) < 2:
        return None
    sorted_arr = sorted(arr)
    return sorted_arr[:2]
