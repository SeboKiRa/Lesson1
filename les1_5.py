a = input("Введите результаты пробежки первого дня, в км: ")
a = int(a)
b = input("Введите общий желаемый результат, в км: ")
b = int(b)
result_days = 1
while a < b:
    a *= 1.1
    result_days += 1
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
