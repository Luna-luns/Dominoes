class Player:
    def __init__(self, player_pieces: list):
        self.player_pieces = player_pieces
        self.pieces_size = len(self.player_pieces)
        self.biggest_piece = None

    def find_biggest_piece(self) -> list:
        total_sum = 0

        for element in self.player_pieces:
            total = sum(element)

            if total > total_sum:
                total_sum = total
                self.biggest_piece = element

        return self.biggest_piece

    def put_right_or_left(self, number: int, snake: list, domino: list) -> str:
        if number > 0:
            return f'{snake}{domino}'

        return f'{domino}{snake}'

    def player_move(self, snake: list, number: int) -> str:
        domino = self.take_domino_to_move(number)
        self.player_pieces.remove(domino)
        snake = self.put_right_or_left(number, snake, domino)

        return snake

    def take_domino_to_move(self, number: int) -> list:
        return self.player_pieces[abs(number) - 1]

    def is_valid_number(self, number: int) -> bool:
        return abs(number) <= self.pieces_size

    def is_pl_out_off_pieces(self) -> bool:
        return self.pieces_size == 0
