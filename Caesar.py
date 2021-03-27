eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def long_rot(lang, phrase):
    if lang == 'рус':
        result = ''
        for i in range(1, int((len(rus_lower_alphabet) + 1) / 2 + 1)):
            result = find_encryption(lang, i, phrase)
            print(result)
    elif lang == 'анг':
        result = ''
        for i in range(1, int((len(eng_lower_alphabet) + 1) / 2 + 1)):
            result = find_encryption(lang, i, phrase)
            print(result)


def find_encryption(lang, rot, phrase):
    new_phrase = ''
    x = 0
    if lang == 'рус':
        for c in phrase:
            if not c.isalpha():
                new_phrase += c
            else:
                if c.isupper() == True:
                    if (int(rus_upper_alphabet.find(c)) + int(rot)) < len(rus_upper_alphabet):
                        x = int(rus_upper_alphabet.find(c)) + int(rot)
                        new_phrase += rus_upper_alphabet[x]
                    else:
                        x = int(rus_upper_alphabet.find(c)) + int(rot) - len(rus_upper_alphabet)
                        new_phrase += rus_upper_alphabet[x]
                else:
                    if (int(rus_lower_alphabet.find(c)) + int(rot)) < len(rus_lower_alphabet):
                        x = int(rus_lower_alphabet.find(c)) + int(rot)
                        new_phrase += rus_lower_alphabet[x]
                    else:
                        x = int(rus_lower_alphabet.find(c)) + int(rot) - len(rus_lower_alphabet)
                        new_phrase += rus_lower_alphabet[x]
        x = 0
    else:
        for c in phrase:
            if not c.isalpha():
                new_phrase += c
            else:
                if c.isupper() == True:
                    if (int(eng_upper_alphabet.find(c)) + int(rot)) < len(eng_upper_alphabet):
                        x = int(eng_upper_alphabet.find(c)) + int(rot)
                        new_phrase += eng_upper_alphabet[x]
                    else:
                        x = int(eng_upper_alphabet.find(c)) + int(rot) - len(eng_upper_alphabet)
                        new_phrase += eng_upper_alphabet[x]
                else:
                    if (int(eng_lower_alphabet.find(c)) + int(rot)) < len(eng_lower_alphabet):
                        x = int(eng_lower_alphabet.find(c)) + int(rot)
                        new_phrase += eng_lower_alphabet[x]
                    else:
                        x = int(eng_lower_alphabet.find(c)) + int(rot) - len(eng_lower_alphabet)
                        new_phrase += eng_lower_alphabet[x]
        x = 0
    return new_phrase


def find_decryption(lang, rot, phrase):
    new_phrase = ''
    x = 0
    if lang == 'рус':
        for c in phrase:
            if not c.isalpha():
                new_phrase += c
            else:
                if c.isupper():
                    if (int(rus_upper_alphabet.rfind(c)) - int(rot)) > 0:
                        x = int(rus_upper_alphabet.rfind(c)) - int(rot)
                        new_phrase += rus_upper_alphabet[x]
                    elif (int(rus_upper_alphabet.rfind(c)) - int(rot)) <= 0:
                        x = int(rus_upper_alphabet.rfind(c)) - int(rot) + len(rus_upper_alphabet)
                        new_phrase += rus_upper_alphabet[x]
                else:
                    if (int(rus_lower_alphabet.rfind(c)) - int(rot)) > 0:
                        x = int(rus_lower_alphabet.rfind(c)) - int(rot)
                        new_phrase += rus_lower_alphabet[x]
                    elif (int(rus_lower_alphabet.rfind(c)) - int(rot)) <= 0:
                        x = int(rus_lower_alphabet.rfind(c)) - int(rot) + len(rus_lower_alphabet)
                        new_phrase += rus_lower_alphabet[x]
        x = 0
    else:
        for c in phrase:
            if not c.isalpha():
                new_phrase += c
            else:
                if c.isupper():
                    if (int(eng_upper_alphabet.find(c)) + int(rot)) < len(eng_upper_alphabet):
                        x = int(eng_upper_alphabet.find(c)) + int(rot)
                        new_phrase += eng_upper_alphabet[x]
                    else:
                        x = int(eng_upper_alphabet.find(c)) + int(rot) - len(eng_upper_alphabet)
                        new_phrase += eng_upper_alphabet[x]
                else:
                    if (int(eng_lower_alphabet.find(c)) + int(rot)) < len(eng_lower_alphabet):
                        x = int(eng_lower_alphabet.find(c)) + int(rot)
                        new_phrase += eng_lower_alphabet[x]
                    else:
                        x = int(eng_lower_alphabet.find(c)) + int(rot) - len(eng_lower_alphabet)
                        new_phrase += eng_lower_alphabet[x]
        x = 0
    return new_phrase


print('Здравствуйте! Добро пожаловать в шифратор и дешифратор Цезаря')
cryption = ''
# проверка ввода шир-дешифр
while cryption.lower() != 'шифр' or cryption.lower() != 'дешифр':
    cryption = str(input('Будем шифровать или расшифровывать? шифр/дешифр '))
    if cryption.lower() == 'шифр' or cryption.lower() == 'дешифр':
        break
    else:
        print('Введите \"шифр\" или \"дешифр\"')
# проверка ввода сдвига
rot = ''
while rot.isdigit() == False or rot != 'неизв':
    print('Введите целое число или "неизв"!')
    rot = input('Какой шаг сдвига? (число или "неизв") ')
    if rot.isdigit() == True or rot == 'неизв':
        break

# проверка ввода запроса языка
lang = ''
while lang.lower() != 'рус' or lang.lower() != 'анг':
    lang = input('На каком языке будем шифроваться? рус/анг ')
    if lang.lower() == 'рус' or lang.lower() == 'анг':
        break
    else:
        print('Введите \"рус\" или \"анг\" ')
phrase = str(input('Введите фразу '))

if cryption == 'шифр' and rot.isdigit() == True:
    print(find_encryption(lang, rot, phrase))
elif cryption == 'дешифр' and rot.isdigit() == True:
    print(find_decryption(lang, rot, phrase))
elif cryption == 'шифр' and rot.isdigit() == False:
    long_rot(lang, phrase)
elif cryption == 'дешифр' and rot.isdigit() == False:
    long_rot(lang, phrase)
