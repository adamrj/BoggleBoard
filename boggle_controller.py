from boggle_models import BoggleBoard
from boggle_views import View

class Controller:
	def __init__(self):
		self.boggleboard = BoggleBoard()
		self.view = View()

	def game_logic(self):
		board = self.boggleboard.shake()
		self.view.print_board(board)

test = Controller()
test.game_logic()
