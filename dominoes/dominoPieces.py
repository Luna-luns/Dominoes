import random


class DominoPieces:
    def make_domino_list(self, domino: list) -> list:
        domino_list = []
        for element in domino:
            domino_list.append([element[0], element[1]])

        return domino_list

    def split_dominoes(self, domino: list) -> list:
        return random.sample(domino, 7)

    def has_snake_piece(self, domino: list) -> bool:
        for element in domino:
            return element[0] == element[1]

    def find_biggest_piece(self, domino: list) -> list:
        total_sum = 0
        biggest_piece = None

        for element in domino:
            total = sum(element)

            if total > total_sum:
                total_sum = total
                biggest_piece = element

        return biggest_piece

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
