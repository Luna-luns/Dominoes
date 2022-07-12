from player import Player
from field import Field
from domino_stock import DominoStock
from players_holder import PlayersHolder
from status import Status


class Game:
    def __init__(self, player_1: Player, player_2: Player, field: Field, stock: DominoStock):
        self.player_holder = PlayersHolder(player_1, player_2)
        self.field = field
        self.stock = stock

    def start_game(self):
        first_player: Player = self.player_holder.find_first_player()
        snake_domino = first_player.get_hand().find_biggest_domino()
        first_player.get_hand().remove_domino(snake_domino)
        self.field.append_right(snake_domino)
        self.play()

    def play(self):
        while True:
            if self.field.is_draw():
                self.show_game_info(self.player_holder.player_1, Status.DRAW)
                self.show_game_info(self.player_holder.player_2, Status.DRAW)
                break

            if self.player_holder.player_1.get_hand().size() == 0:
                self.show_game_info(self.player_holder.player_1, Status.PLAYER_WIN)
                self.show_game_info(self.player_holder.player_2, Status.OPPONENT_WIN)
                break

            if self.player_holder.player_2.get_hand().size() == 0:
                self.show_game_info(self.player_holder.player_1, Status.OPPONENT_WIN)
                self.show_game_info(self.player_holder.player_2, Status.PLAYER_WIN)
                break

            self.show_game_info(self.player_holder.player_1, self.player_holder.get_status(self.player_holder.player_1))
            self.show_game_info(self.player_holder.player_2, self.player_holder.get_status(self.player_holder.player_2))

            self.player_holder.current_player.make_move(self.field, self.stock)
            self.player_holder.switch_players()

    def show_game_info(self, player: Player, status: Status):
        player.show_game_info(
            self.stock.size(),
            self.player_holder.get_opposite_player(player).get_hand().size(),
            self.field,
            status
        )
