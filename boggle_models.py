from random import randrange
import itertools

class BoggleBoard:
    def __init__(self):
        # self.board = self.shake()
        # HARD CODED FOR TESTING
        self.board = [['D', 'E', 'U', 'Y'], 
                      ['M', 'T', 'P', 'E'], 
                      ['C', 'H', 'Z', 'E'], 
                      ['A', 'QU', 'T', 'B']]

    def shake(self):
        letter_bank = [['A','A','E','E','G','N'],['A','B','B','J','O','O'],['A','C','H','O','P','S'],['A','F','F','K','P','S'],['A','O','O','T','T','W'],['C','I','M','O','T','U'],['D','E','I','L','R','X'],['D','E','L','R','V','Y'],['D','I','S','T','T','Y'],['E','E','G','H','N','W'],['E','E','I','N','S','U'],['E','H','R','T','V','W'],['E','I','O','S','S','T'],['E','L','R','T','T','Y'],['H','I','M','N','U','QU'],['H','L','N','N','R','Z']]
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

    def q_controlled(self, user_guess):
        guess_as_list = list(user_guess)
        for i in range(len(guess_as_list) - 1):
            if guess_as_list[i] == 'Q':
                guess_as_list[i] += guess_as_list[i + 1]
                guess_as_list.remove(guess_as_list[i + 1])
        return guess_as_list

    def get_surround(self, row, column):
        surrounding_cells = []
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                if not ((i == row and j == column) or (i < 0) or (j < 0) or (j >= len(self.board) or (i >= len(self.board)))):
                    surrounding_cells.append(self.board[i][j])
        return surrounding_cells

    def get_coords(self, start_letter):
        for row in range(len(self.board)):
            for element in range(len(self.board[row])):
                if self.board[row][element] == start_letter:
                    return (row, element)
        return False
    
    def starting_letter_coords(self, user_guess):
        all_letter_coords = []
        for row in range(len(self.board)):
            for element in range(len(self.board[row])):
                if self.board[row][element] == user_guess[0]:
                    coords = (row, element)
                    all_letter_coords.append(coords)
        return all_letter_coords

    def evaluate(self, user_guess, possible_starting_coords):
        for coords in possible_starting_coords:
            surrounding_letters = self.get_surround(coords[0], coords[1])
            for letter in surrounding_letters:
                if letter == user_guess[1]: 




    # def evaluate(self, user_guess):
    #     if len(user_guess) == 1:
    #         print(user_guess)
    #         return
    #     if len(user_guess) > 1:
    #         start_letter = user_guess[0]
    #         start_coords = self.get_coords(start_letter)
    #         surrounding_letters = self.get_surround(start_coords[0], start_coords[1])
    #         for letter in surrounding_letters:
    #             if letter == user_guess[1] and start_coords != self.get_coords(letter):
    #                 print (letter, self.get_coords(letter))
    #                 stripped = user_guess.strip(user_guess[0])
    #                 self.evaluate(stripped)
    
    # def find_all(self):
    #     all_valid_cominations = []
    #     for row in self.board:
    #         for element in row:
    #             coords = self.get_coords(element)
    #             surrounding = self.get_surround(coords[0], coords[1])
                



test = BoggleBoard()
# test.q_controlled('QUIET')
# print (test.starting_letter_coords('ETH'))
# test.find_all()
# print (test.get_coords('Z'))
# print (test.get_surround(2,2))

# print (test.import_dictionary('test_dict.txt'))