# -*- coding: cp1251 -*-
from os import read
import random

class Task2: 
    
    # ���� ������. ���������� ���������� ��� ������� ������ � ��������� �������.
    def ShuffleString():
        print('������� ������: ')
        stroka = input()
        print('����������� ������: ' + stroka)
        
        ls = list(stroka)
        random.shuffle(ls)
        
        result = ''.join(ls)
        print('������������ ������: ' + result)


    