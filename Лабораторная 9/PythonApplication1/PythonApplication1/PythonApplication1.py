# -*- coding:cp1251 -*-

import csv
from operator import delitem

with open('11 - 1.csv', encoding='utf-8') as csvfile:
    file_reader = csv.reader(csvfile, delimiter = ",")
    count = 0
    for row in file_reader:
        print(file_reader.)
        if count == 0:
            # ����� ������, ���������� ��������� ��� ��������
            print(f'���� �������� �������: {", ".join(row)}')
        else:
            # ����� �����
            print(f'    {row[0]} - {row[1]} � �� ������� � {row[2]} ����.')
        count += 1
    print(f'����� � ����� {count} �����.')