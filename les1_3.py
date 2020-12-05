n = int(input("Введите число n: "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print("Результат равен:", comp)

# через цикл for
n = input("Введите число\n>>> ")
sum_n = 0
n_itr = ''
for i in range(3):
    n_itr = n_itr + n
    sum_n = int(sum_n) + int(n_itr)
    print("Результат", sum_n)

