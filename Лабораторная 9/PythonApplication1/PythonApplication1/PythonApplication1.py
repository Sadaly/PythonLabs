# -*- coding:cp1251 -*-

import csv
from operator import delitem

with open('11 - 1.csv', encoding='utf-8') as csvfile:
    file_reader = csv.reader(csvfile, delimiter = ",")
    count = 0
    for row in file_reader:
        print(file_reader.)
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Вывод строк
            print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
        count += 1
    print(f'Всего в файле {count} строк.')