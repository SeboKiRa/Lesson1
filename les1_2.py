user_time = input("Введите время в секундах\n>>> ")

if user_time.isdigit():
    user_time = int(user_time)
else:
    print("Ошибка ввода, введите число")
    exit()

hours = user_time // (60 * 60)
user_time %= (60 * 60)
minutes = user_time // 60
user_time %= 60

print(f'{hours}:{minutes}:{user_time}')
