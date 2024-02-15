# -*- coding: cp1251 -*-
import random

class Task2: 
    
    # Дана строка. Необходимо перемешать все символы строки в случайном порядке.
    def ShuffleString():
        print('Введите строку: ')
        stroka = input()
        print('Изначальная строка: ' + stroka)
        
        ls = list(stroka)
        random.shuffle(ls)
        
        result = ''.join(ls)
        print('Перемешанная строка: ' + result)


    