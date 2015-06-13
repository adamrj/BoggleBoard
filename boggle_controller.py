from random import randrange

letter_bank = [['A','A','E','E','G','N'],
['A','B','B','J','O','O'],
['A','C','H','O','P','S'],
['A','F','F','K','P','S'],
['A','O','O','T','T','W'],
['C','I','M','O','T','U'],
['D','E','I','L','R','X'],
['D','E','L','R','V','Y'],
['D','I','S','T','T','Y'],
['E','E','G','H','N','W'],
['E','E','I','N','S','U'],
['E','H','R','T','V','W'],
['E','I','O','S','S','T'],
['E','L','R','T','T','Y'],
['H','I','M','N','U','Qu'],
['H','L','N','N','R','Z']]

for i in range(0, 4):
    board = []
    board.append(sublist)
    for i in range(0, 4):
        x = randrange(17)
        y = randrange(7)
        sublist = []
        sublist.append(letter_bank[x][y])

print (board)



