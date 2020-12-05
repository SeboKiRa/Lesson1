proceeds = input('Введите значение выручки: ')
proceeds = int(proceeds)

costs = input('Введите значение издержек: ')
costs = int(costs)

if proceeds > costs:
    print('Прибыль')
    profit = proceeds / costs
    print(f'Рентабельность фирмы составляет: {profit:.2f}%')
    workers = input('Введите количество сотрудников фирмы: ')
    workers = int(workers)
    print(f'Прибыль в расчете на одного сторудника сотавила {proceeds / workers:.2f}')
elif proceeds == costs:
    print("Фирма работает в ноль")
else:
    print('Убыток')
