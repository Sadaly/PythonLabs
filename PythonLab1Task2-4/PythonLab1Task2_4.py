# -*- coding: cp1251 -*-
import random
from re import I, split

class Task2: 
    
    # Дана строка. Необходимо перемешать все символы строки в случайном порядке.
    def ShuffleString(stroka):
        ls = list(stroka)
        random.shuffle(ls)
        
        result = ''.join(ls)
        return result
    
    # Дана строка, состоящая из символов латиницы. Необходимо проверить, образуют ли прописные символы этой строки палиндром.
    def IsPalindrome(stroka):
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
    
    # Дана строка в которой записаны слова через пробел. Необходимо упорядочить слова по количеству букв в каждом слове.
    def SortWordsInString(stroka):
        words = stroka.split()
        words_count = len(words)
        result = ''

        for i in range(0, words_count - 1):
            for j in range(i, words_count):
                if (len(words[i]) > len(words[j])):
                    temp = words[i]
                    words[i] = words[j]
                    words[j] = temp
        
        for i in range(0, words_count):
            result += words[i] + ' '
        
        return result
    
    while(True):
        print('1.ShuffleString(str)\n2.IsPalindrome(str)\n3.SortWordsInString(str)\nВведите номер необходимой функции:')
        task_number = int(input())
        
        print('Введите строку: ')
        stroka = input()
        
        if(task_number == 1):
            print('Перемешанная строка: ' + ShuffleString(stroka))
        elif(task_number == 2):
            print('Прописаные буквы строки образуют палиндром?: ' + str(IsPalindrome(stroka)))
        elif(task_number == 3):
            print('Отсортированная строка по длине слов: ' + SortWordsInString(stroka))
            
        print()
        
            
        

            
        