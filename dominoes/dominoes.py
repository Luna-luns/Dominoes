import domino_stock
from real_player import RealPlayer
from computer_player import ComputerPlayer
from game import Game
from field import Field

full_domino_stock = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 3],
                     [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6], [0, 0], [0, 1], [0, 2],
                     [0, 3], [0, 4], [0, 5], [0, 6]]

stock = domino_stock.from_raw_list(full_domino_stock)  # instance DominoStock
player_hand = stock.take_hand()  # instance PlayerHand
player = RealPlayer(player_hand)
computer_hand = stock.take_hand()  # instance PlayerHand
computer = ComputerPlayer(computer_hand)
field = Field()
game = Game(player, computer, field, stock)
game.start_game()
