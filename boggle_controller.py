from boggle_models import BoggleBoard
from boggle_views import View

class Controller:
    def __init__(self, text_file):
        self.boggleboard = BoggleBoard()
        self.view = View()
        self.text_file = text_file

    def game_logic(self):
        board = self.boggleboard.board
        self.view.print_board(board)
        dictionary = self.boggleboard.import_dictionary(self.text_file)
        user_guess = self.view.user_inputs_word().upper()
        q_controlled_guess = self.boggleboard.q_controlled(user_guess)
        start_letter = user_guess[0]
        start_coords = self.boggleboard.get_coords(start_letter)
        surrounding_letters = self.boggleboard.get_surround(start_coords[0], start_coords[1])
        print (surrounding_letters)


test = Controller('test_dict.txt')
test.game_logic()
