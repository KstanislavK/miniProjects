# шифр цезаря, который определяет смещение символа по длине слова
lower_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encode(rot, word):
    new_word = ''
    x = 0
    for c in word:
        if not c.isalpha():
            new_word += c
        else:
            if c.isupper():
                x = upper_alphabet.find(c) + rot
                new_word += upper_alphabet[x]
            else:
                x = lower_alphabet.find(c) + rot
                new_word += lower_alphabet[x]
    x = 0
    return new_word


phrase = input('Введите фразу ')
phrase = phrase.split()
new_phrase = []
new_word = ''
count = 0

for c in phrase:
    for i in c:
        if i.isalpha():
            count += 1
    new_word = encode(count, c)
    print(new_word, end=' ')
    count = 0
