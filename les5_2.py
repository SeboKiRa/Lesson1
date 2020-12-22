'''
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

import os

file_path = os.path.join(os.path.dirname(__file__), 'work2.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    print(f'Количество строк в файле - {len(lines)}')

with open(file_path, 'r', encoding='UTF-8') as file:
        lines = file.read()
        lines = lines.split()
        print(f'Общее количество слов - {len(lines)}')
