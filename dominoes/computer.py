import random


class Computer:
    def __init__(self, computer_pieces: list):
        self.computer_pieces = computer_pieces
        self.pieces_size = len(self.computer_pieces)
        self.biggest_piece = None

    def find_biggest_piece(self) -> list:
        total_sum = 0

        for element in self.computer_pieces:
            total = sum(element)

            if total > total_sum:
                total_sum = total
                self.biggest_piece = element

        return self.biggest_piece

    def choose_number_to_move(self) -> int:
        return random.randint(-self.pieces_size, self.pieces_size)

    def take_domino_to_move(self, number: int) -> list:
        return self.computer_pieces[abs(number) - 1]

    def put_right_or_left(self, number: int, snake: list, domino: list) -> str:
        if number > 0:
            return f'{snake}{domino}'

        return f'{domino}{snake}'

    def computer_move(self, snake: list, number: int) -> str:
        domino = self.take_domino_to_move(number)
        self.computer_pieces.remove(domino)
        snake = self.put_right_or_left(number, snake, domino)

        return snake

    def is_comp_out_off_pieces(self) -> bool:
        return self.pieces_size == 0

