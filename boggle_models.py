from random import randrange

class BoggleBoard:
    def __init__(self):
        pass

    def shake(self):
        letter_bank = [['A','A','E','E','G','N'],['A','B','B','J','O','O'],['A','C','H','O','P','S'],['A','F','F','K','P','S'],['A','O','O','T','T','W'],['C','I','M','O','T','U'],['D','E','I','L','R','X'],['D','E','L','R','V','Y'],['D','I','S','T','T','Y'],['E','E','G','H','N','W'],['E','E','I','N','S','U'],['E','H','R','T','V','W'],['E','I','O','S','S','T'],['E','L','R','T','T','Y'],['H','I','M','N','U','Qu'],['H','L','N','N','R','Z']]
        board = []
        for i in range(0, 4):
            sublist = []
            for j in range(0, 4):
                x = randrange(0, len(letter_bank))
                y = randrange(0, 6)
                sublist.append(letter_bank[x][y])
                letter_bank.remove(letter_bank[x])
            board.append(sublist)
        return board

    def import_dictionary(self, text_file):
        usable_words = []
        file_object = open(text_file)
        all_words = file_object.readlines()
        for each_word in all_words:
            stripped = each_word.strip('\n').upper()
            if len(stripped) > 2:
                usable_words.append(stripped)
        return usable_words


test = BoggleBoard()

print (test.import_dictionary('test_dict.txt'))