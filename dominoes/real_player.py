from player import Player
from field import Field
from domino_stock import DominoStock
from status import Status
import user_interface
from inputError import InputError


class RealPlayer(Player):
    def show_game_info(self, stock_size: int, opponent_pieces_size: int, field: Field, status: Status) -> None:
        user_interface.print_header()
        user_interface.print_stock_size(stock_size)
        user_interface.print_comp_pieces_size(opponent_pieces_size)
        user_interface.print_field(field)
        user_interface.print_enumerated_player_hand(self.player_hand)
        user_interface.print_status(status)

    def make_move(self, field: Field, stock: DominoStock) -> None:
        while True:
            try:
                number = user_interface.ask_number()

                if (abs(number)) > self.player_hand.size():
                    raise InputError()

                if number == 0:
                    self.player_hand.append(stock.take_random_domino())
                    return

                domino = self.player_hand.take_domino(abs(number))
                if number > 0:
                    field.append_right(domino)
                else:
                    field.append_left(domino)

                return
            except InputError as e:
                print(e)
