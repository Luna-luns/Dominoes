import random
import ast

class DominoPieces:
    def split_dominoes(self, domino: list) -> list:
        return random.sample(domino, 7)

    def has_snake_piece(self, domino: list) -> bool:
        for element in domino:
            return element[0] == element[1]

    def find_domino_snake(self, c_piece: list, pl_piece: list) -> list:
        if c_piece > pl_piece:
            return c_piece
        else:
            return pl_piece

    def set_status(self, domino_snake: list, comp_pieces: list) -> str:
        if domino_snake in comp_pieces:
            return 'player'
        else:
            return 'computer'

    def convert_to_list(self, snake: str) -> list:
        n = 6
        snake = [snake[i:i + n] for i in range(0, len(snake), n)]
        snake = [ast.literal_eval(elem) for elem in snake]

        return snake

    def is_end_num_times_wasted(self, snake: str) -> bool:
        snake = self.convert_to_list(snake)
        count = 0
        for elem in snake:
            if snake[0][0] in elem:
                count += 1
            if elem.count(snake[0][0]) == 2:
                count += 1
        return snake[0][0] == snake[-1][1] and count == 8

    def hide_pieces(self, snake: list):
        first_three = snake[0:3]
        second_three = snake[-3:]

        return f'{first_three[0]}{first_three[1]}{first_three[2]}...{second_three[0]}{second_three[1]}{second_three[2]}'



