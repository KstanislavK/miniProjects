from random import randint


class Card:
    def __init__(self):
        self.card = self.create_card()

    """Метод создания карточки"""

    def create_card(self):
        nums = []
        while len(nums) < 15:
            x = randint(1, 90)
            if x not in nums:
                nums.append(x)
        return nums

    """Метод создания вида карточки"""

    def card_for_print(self, needed_card, name):
        printable_card = list(map(str, needed_card))
        row_1 = printable_card[0:5]
        row_1.sort()
        row_2 = printable_card[5:10]
        row_2.sort()
        row_3 = printable_card[10:]
        row_3.sort()
        footer = '-' * (len(row_1) * 4)
        header = '-' * int(((len(footer)) - len(name)) / 2) + name + '-' * (int(((len(footer)) - len(name)) / 2))
        printable_card = header + '\n' + '  '.join(row_1) + '\n' + '  '.join(row_2) + '\n' + '  '.join(
            row_3) + '\n' + footer
        return printable_card


class Game(Card):
    def __init__(self, name, card_player, card_comp):
        self.name = name
        self.card_p = card_player
        self.card_c = card_comp
        self.used_kegs = []
        self.num_of_kegs = 90
        self.total = 0

    """Основной метод игры"""

    def game_on(self):
        while self.num_of_kegs > 0:
            self.num_of_kegs -= 1
            keg = self.new_keg()
            print(f'Новый бочонок: {keg} (Осталось {self.num_of_kegs})')
            print(self.card_for_print(self.card_p, self.name))
            print(self.card_for_print(self.card_c, 'Computer'))
            action = input('Зачеркнуть цифру? (y/n)').lower().strip()
            if action == 'q' or action == 'quit' or action == 'exit':
                break
            if action == 'y' or action == 'н':
                if keg in self.card_p:
                    self.card_p = self.replace_item(self.card_p, keg)
                    self.total += 1
                elif keg in self.card_c:
                    self.card_c = self.replace_item(self.card_c, keg)
                elif keg not in self.card_p:
                    print('В Вашей карточке нет такого числа')
                    print(
                        f'Вы проиграли матч. Осталось бочонков: {self.num_of_kegs}\nИспользованные бочонки: {self.used_kegs}')
                    LeaderBoard().write_in_board()
                    print('Доска почета')
                    LeaderBoard().print_board
                    break
                if self.digit_check(self.card_p) == False:
                    print(
                        f'Вы выйграли! Карточка закрыта.\nИспользованные бочонки: {self.used_kegs}')
                    LeaderBoard().write_in_board()
                    print('Доска почета')
                    LeaderBoard().print_board
                    break
                if self.digit_check(self.card_c) == False:
                    print(f'Вы проиграли матч. Компьютер закрыл карточку.')
                    print(f'Осталось бочонков: {self.num_of_kegs}\nИспользованные бочонки: {self.used_kegs}')
                    LeaderBoard().write_in_board()
                    print('Доска почета')
                    LeaderBoard().print_board
                    break
            if action == 'n' or action == 'т':
                if keg in self.card_p:
                    print(
                        f'Вы проиграли матч. В Вашей карточке есть такое число.\nОсталось бочонков: {self.num_of_kegs}\nИспользованные бочонки: {self.used_kegs}')
                    LeaderBoard().write_in_board()
                    print('Доска почета')
                    LeaderBoard().print_board
                    break
                if keg in self.card_c:
                    self.card_c = self.replace_item(self.card_c, keg)
                if self.digit_check(self.card_c) == False:
                    print(
                        f'Вы проиграли матч. Компьютер закрыл карточку.\nОсталось бочонков: {self.num_of_kegs}\nИспользованные бочонки: {self.used_kegs}')
                    LeaderBoard().write_in_board()
                    print('Доска почета')
                    LeaderBoard().print_board
                    break

    """Метод проверки наличия чисел в карточке"""

    def digit_check(self, card_list):
        digit_flag = False
        for item in card_list:
            flag = None
            try:
                int(item)
                flag = True
            except ValueError:
                flag = False
            if flag:
                digit_flag = True
                break
        return digit_flag

    """Метод замены числа в карте на прочерк"""

    def replace_item(self, card_list, keg):
        item = card_list.index(keg)
        card_list[item] = '--'
        return card_list

    """Метод выдачи нового бочонка"""

    def new_keg(self):
        flag = False
        keg = None
        while flag == False:
            keg = randint(1, 90)
            if keg not in self.used_kegs:
                self.used_kegs.append(keg)
                flag == True
                return keg


class LeaderBoard:
    """Класс доски почета. Записывает результаты в файл и выводит доску"""

    @property
    def print_board(self):
        table = ''
        with open(r'lb.txt') as obj:
            lines = obj.readlines()
        for el in lines:
            el = el.split()
            table += '|' + ' ' * (12 - int(len(el[0]) / 2)) + el[0] + ' ' * (12 - int(len(el[0]) / 2)) + '|' + ' ' * (
                        12 - int(len(el[1]) / 2)) + str(el[1]) + ' ' * (
                                 12 - int(len(el[1]) / 2)) + '|\n' + '-' * 52 + '\n'
        print(table)

    def write_in_board(self):
        with open(r'lb.txt', 'a') as obj:
            obj.write(f'\n{game.name}  {game.total}')


print('   Вас приветствует игра Спорт-лото!\n\
Вам предстоит сразиться с компьютером в виртуальную версию игры Лото\n\
Каждый ход выбирается один случайный бочонок и выводится на экран.\n\
С помощью клавиатуры нужно выбрать действие:\n\
y - зачеркнуть число, n - продолжить, q - выход\n\
Если числа не оказалось, а вы зачеркнули - проигрыш\n\
Если вы продолжили, а число в карточке есть - проигрыш\n\
Для просмотра итоговых очков наберите lb\n')
player_name = input('Введите ваше имя: ')
while player_name == 'lb':
    LeaderBoard().print_board
    player_name = input('Введите ваше имя: ')
else:
    game_flag = True
    while game_flag:
        quest = input('Поиграем? (y/n): ')
        if quest == 'y' or quest == 'н':
            card_player = Card()
            card_comp = Card()
            game = Game(player_name, card_player.card, card_comp.card)
            game.game_on()
        elif quest == 'n' or quest == 'т':
            game_flag = False
    else:
        print('Приходите еще')
