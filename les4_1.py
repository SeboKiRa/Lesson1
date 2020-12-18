'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv

for param in argv:
    try:
        _, production, rate, prize, *_ = argv
        result = float(production) * float(rate) + float(prize)
        print(result)
    except ValueError as e:
        print("Ошибка ввода данных")
        print(e)
