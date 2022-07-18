import user_interface
from player import Player
from field import Field, ALL, RIGHT
from domino_stock import DominoStock
from status import Status
from illegal_move_error import IllegalMoveError
from collections import Counter


class ComputerPlayer(Player):
    def show_game_info(self, stock_size: int, opponent_pieces_size: int, field: Field, status: Status) -> None:
        pass

    def make_move(self, field: Field, stock: DominoStock) -> None:
        user_interface.approve_comp_move()
        while True:
            domino = None
            try:
                dictionary = dict(Counter(self.player_hand.count_numbers()) + Counter(field.count_numbers()))

                appropriate_domino = []
                for _domino in self.player_hand.dominoes:
                    if field.is_appropriate(_domino, ALL):
                        appropriate_domino.append(_domino)

                if len(appropriate_domino) == 0:
                    if stock.is_empty():
                        return
                    else:
                        self.player_hand.append(stock.take_random_domino())
                        return

                lamb = lambda d: dictionary[d.left_side] + dictionary[d.right_side]
                domino = max(appropriate_domino, key=lamb)

                if field.is_appropriate(domino, RIGHT):
                    field.append_right(domino)
                    self.player_hand.remove_domino(domino)
                    return
                else:
                    field.append_left(domino)
                    self.player_hand.remove_domino(domino)
                    return

            except IllegalMoveError:
                if domino:
                    self.player_hand.append(domino)
