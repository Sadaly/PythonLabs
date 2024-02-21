# -*- coding:cp1251 -*-

def SortByAvgAsciiWeight(strings):
    return sorted(strings, key=lambda x: sum(map(ord, x))/len(x))

def SortByMedianAsciiDifference(strings):
    def median_difference(s):
        sorted_chars = sorted(map(ord, s))
        median_index = len(sorted_chars) // 2
        return abs(sorted_chars[median_index] - sorted_chars[median_index-1])

    return sorted(strings, key=median_difference)

def SortByQuadDeviation(strings):
    def quad_deviation(s):
        middle = len(s) // 2
        mirror_pairs = zip(s[:middle], reversed(s[middle:]))
        return sum((ord(a) - ord(b))**2 for a, b in mirror_pairs)

    return sorted(strings, key=quad_deviation)

def SortByFreqDeviation(strings):
    def freq_deviation(s, common_char):
        common_freq = s.count(common_char) / len(s)
        return (ord(common_char) - s.count(common_char))**2 / common_freq

    most_common_char = max(set("".join(strings)), key=lambda x: "".join(strings).count(x))
    return sorted(strings, key=lambda x: freq_deviation(x, most_common_char))

# ������������ �������� ������
task_choice = int(input("�������� ������� (1, 2, 3 ��� 4):\n1. � ������� ���������� �������� ���� ASCII-���� ������� ������.\n2. � ������� ���������� ���������� �������� ������� ����� (������� ��������� �������� ��������� �� ������� � ������������ ����� ������ ���������� ��������\n3. � ������� ���������� ������������� ���������� ����� ���������� ASCII-����� ������� ������ � ������� � ASCII-����� ��� ��������� ������������� �������� ������ (������������ �� ��������).\n4. � ������� ���������� ������������� ���������� ������� ������������� ������ ����������������� ������� � ������ ����� �� ������� ��� ������������� � ������ ������.\n"))

# ������ ����� � ����������
strings = []
num_strings = int(input("������� ����� ������: "))
for i in range(num_strings):
    string_input = input(f"������� ������ {i+1}: ")
    strings.append(string_input)

# ����� � ���������� ������
if task_choice == 1:
    result = SortByAvgAsciiWeight(strings)
elif task_choice == 2:
    result = SortByMedianAsciiDifference(strings)
elif task_choice == 3:
    result = SortByQuadDeviation(strings)
elif task_choice == 4:
    result = SortByFreqDeviation(strings)
else:
    result = None

# ����� ����������
if result:
    print("��������������� ������:")
    for string in result:
        print(string)
