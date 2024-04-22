# -*- coding:cp1251 -*-

# Открываем файл для чтения (режим 'r' - read)
with open('27-170c.txt', 'r') as file:
    # Читаем все строки из файла в массив
    lines = file.readlines()

N, K = map(int, lines[0].split())
max_sum = -9999999999999
rast = 999999999999
s = [0]*N

for i in range(0, N): # Заполняем список суммами растояний от начала до флага
    s[i] = s[i-1] + int(lines[i + 1]) 
for j in range(K,N):
    rast = min(rast, s[j-K]) # Находим минимальную сумму растояний, её можно исключить из максимальной 
    max_sum = max(max_sum, s[j], s[j] - rast)

        
print(max_sum)