'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

import os

file_path = os.path.join(os.path.dirname(__file__), 'work5.txt')

file_numbers = [3, 3, 1, 11, 14, 8, 17, 14, 4, 9, 1, 14, 6, 9, 4, 12, 2, 6, 1, 6]

# Записываем строку с числами в файл, разделенными пробелами
with open(file_path, 'w', encoding='UTF-8') as file:
    file_str = ' '.join(map(str, file_numbers))
    file.write(file_str)

# Читаем строку в файле
with open(file_path, 'r', encoding='UTF-8') as file:
    numbers = map(int, file.readline().split(' '))

print(sum(numbers))     # Вывод суммы чисел на экран
