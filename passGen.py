# программа генерирует нужное количество

from random import randint

letters = '23456789abcdefghjkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ!#$%&*+-=?@^_'


def generate_password(pass_len, letters):
    password = ''
    for _ in range(pass_len):
        y = randint(1, len(letters) - 1)
        password += str(letters[y])
    return password


pass_count = int(input('Сколько паролей создать? '))
pass_len = int(input('Какой длины должен быть пароль? '))

for k in range(pass_count):
    print(generate_password(pass_len, letters))

input('Нажмите ENTER чтобы закрыть приложение')
