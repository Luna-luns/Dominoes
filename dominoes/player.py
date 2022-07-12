from player_hand import PlayerHand
from field import Field
from domino_stock import DominoStock
from status import Status


class Player:
    def __init__(self, hand: PlayerHand):
        self.player_hand = hand

    def get_hand(self) -> PlayerHand:
        return self.player_hand

    def show_game_info(self, stock_size: int, opponent_pieces_size: int, field: Field, status: Status) -> None:
        pass

    def make_move(self, field: Field, stock: DominoStock) -> None:
        pass
