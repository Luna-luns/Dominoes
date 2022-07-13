from player import Player
from field import Field
from domino_stock import DominoStock
from status import Status
import random


class ComputerPlayer(Player):
    def show_game_info(self, stock_size: int, opponent_pieces_size: int, field: Field, status: Status) -> None:
        pass

    def make_move(self, field: Field, stock: DominoStock) -> None:
        input()
        size = self.player_hand.size()
        number = random.randint(-size, size)

        if number == 0:
            self.player_hand.append(stock.take_random_domino())
            return

        domino = self.player_hand.take_domino(abs(number))
        if number > 0:
            field.append_right(domino)
        else:
            field.append_left(domino)
