#2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

fields = ('имя: ', 'фамилия: ', 'год рождения:', 'город проживания: ', 'email: ', 'телефон: ')

data = {}
for field in fields:
    data[field] = input(f'Введите {field}')

print(data)