from player import Player
from status import Status


class PlayersHolder:
    def __init__(self, player_1: Player, player_2: Player):
        self.player_1 = player_1
        self.player_2 = player_2
        self.current_player = None

    def get_opposite_player(self, player: Player) -> Player:
        if self.player_1 == player:
            return self.player_2

        return self.player_1

    def find_first_player(self) -> Player:
        biggest_player_1_domino = self.player_1.get_hand().find_biggest_domino()
        biggest_player_2_domino = self.player_2.get_hand().find_biggest_domino()

        first_player = self.player_1 if biggest_player_1_domino.count_domino_sum() > biggest_player_2_domino.count_domino_sum() else self.player_2

        self.current_player = self.get_opposite_player(first_player)

        return first_player

    def is_current_player(self, player: Player) -> bool:
        return player == self.current_player

    def switch_players(self):
        self.current_player = self.get_opposite_player(self.current_player)

    def get_status(self, player: Player):
        return Status.PLAYER_MOVE if self.is_current_player(player) else Status.OPPONENT_MOVE
