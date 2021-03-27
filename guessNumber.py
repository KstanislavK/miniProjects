from random import randint

print("Привет! Давай поиграем в игру!? Угадай, какое число от 0 до 100 я загадал?")


def is_valid(num):
    if num.isdigit() and 0 <= int(num) <= 100:
        return True
    else:
        return False


number = int(randint(1, 100))
answer = 0
count = 0
while answer != number:
    answer = input()
    count += 1
    if is_valid(answer):
        if int(answer) < number:
            print("Ваше число меньше загаданного, попробуйте еще раз")
        elif int(answer) > number:
            print("Ваше число больше загаданного, попробуйте еще раз")
        elif int(answer) == number:
            print(f"Вы угадали, поздравляем! Число попыток: {count}")
            break
    else:
        print("Неверный ввод, введите число от 0 до 100")
