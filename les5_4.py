'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

import os

file_path = os.path.join(os.path.dirname(__file__), 'work4.txt')

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []

with open(file_path, 'r', encoding='UTF-8') as file:
    for i in file:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open(file_path, 'w', encoding='UTF-8') as file:
    file.writelines(new_file)
