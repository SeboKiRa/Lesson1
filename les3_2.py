'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

user_name = input('Имя: ')
user_surname = input('Фамилия: ')
user_birth_year = input('Год рождения: ')
user_city = input('Город проживания: ')
user_email = input('Почта: ')
user_phone = input('Телефон: ')

def contact(name: str, surname: str, birth_year: int, city: str, email: str, phone: int):
    """
    Выводит данные о пользователе
    """
    return f"{name} {surname},\n{birth_year} года рождения, \n" \
           f"Проживает в городе {city}.\nКонтакты: {email}, {phone} "

print(contact(name=user_name, surname=user_surname, birth_year=user_birth_year,
              city=user_city, email=user_email, phone=user_phone))
