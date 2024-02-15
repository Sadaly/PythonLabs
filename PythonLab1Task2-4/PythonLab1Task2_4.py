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
    
    # Дана строка, состоящая из символов латиницы. Необходимо проверить, образуют ли прописные символы этой строки палиндром.
    def IsPalindrome():
        print('Введите строку: ')
        stroka = input()
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_case_letters = ''
        
        for i in range(0, len(stroka)):
            if (alphabet.find(stroka[i]) != -1):
                upper_case_letters += stroka[i]
                
        length_upp_cs_ltr = len(upper_case_letters)
        for i in range(0, length_upp_cs_ltr // 2 + length_upp_cs_ltr % 2):
            if (upper_case_letters[i] != upper_case_letters[length_upp_cs_ltr - 1 - i]):
                return False
            
        return True
    