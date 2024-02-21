# -*- coding: cp1251 -*-
import random
from re import I, split

class Task2: 
    
    # ���� ������. ���������� ���������� ��� ������� ������ � ��������� �������.
    def ShuffleString(stroka):
        ls = list(stroka)
        random.shuffle(ls)
        
        result = ''.join(ls)
        return result
    
    # ���� ������, ��������� �� �������� ��������. ���������� ���������, �������� �� ��������� ������� ���� ������ ���������.
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
    
    # ���� ������ � ������� �������� ����� ����� ������. ���������� ����������� ����� �� ���������� ���� � ������ �����.
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
        print('1.ShuffleString(str)\n2.IsPalindrome(str)\n3.SortWordsInString(str)\n������� ����� ����������� �������:')
        task_number = int(input())
        
        print('������� ������: ')
        stroka = input()
        
        if(task_number == 1):
            print('������������ ������: ' + ShuffleString(stroka))
        elif(task_number == 2):
            print('���������� ����� ������ �������� ���������?: ' + str(IsPalindrome(stroka)))
        elif(task_number == 3):
            print('��������������� ������ �� ����� ����: ' + SortWordsInString(stroka))
            
        print()
        
            
        

            
        