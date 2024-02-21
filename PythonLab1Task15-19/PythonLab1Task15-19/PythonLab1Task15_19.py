# -*- coding:cp1251 -*-
from collections import Counter

def FindUniqueElement(arr):
    counter = Counter(arr)
    for num, count in counter.items():
        if count == 1:
            return num
    return None
