from random import randint
import dices

print(dices.startText)
dicesCount = 1

while dicesCount != 0:
    dicesCount = int(input(dices.inputText))
    if int(dicesCount) > 0 and int(dicesCount) < 6:
        dicesList = []
        for i in range(dicesCount):
            number = randint(1, 6)
            dicesList.append(dices.dices[number])
        print('\n-------\n'.join(dicesList))
    else:
        print(dices.errorText)
else:
    print(dices.endText)
