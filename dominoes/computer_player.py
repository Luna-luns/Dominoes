import random
import user_interface
from player import Player
from field import Field
from domino_stock import DominoStock
from status import Status
from illegal_move_error import IllegalMoveError


class ComputerPlayer(Player):
    def show_game_info(self, stock_size: int, opponent_pieces_size: int, field: Field, status: Status) -> None:
        pass

    def make_move(self, field: Field, stock: DominoStock) -> None:
        user_interface.approve_comp_move()
        while True:
            domino = None
            try:
                size = self.player_hand.size()
                number = random.randint(-size, size)

                if number == 0:
                    if stock.is_empty():
                        return
                    else:
                        self.player_hand.append(stock.take_random_domino())
                        return

                domino = self.player_hand.take_domino(abs(number))

                if number > 0:
                    field.append_right(domino)
                else:
                    field.append_left(domino)

                return

            except IllegalMoveError:
                if domino:
                    self.player_hand.append(domino)
