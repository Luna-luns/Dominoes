class PrintFunctions:
    def print_header(self) -> None:
        print('=' * 70)

    def print_stock_size(self, size: int) -> None:
        print(f'Stock size: {size}')

    def print_comp_pieces_size(self, size: int) -> None:
        print(f'Computer pieces: {size}')

    def print_domino_snake(self, snake: list) -> None:
        print(f'\n{snake}\n')\

    def print_enumerated_pl_pieces(self, pl_pieces: list) -> None:
        print('Your pieces:')
        for count, elem in enumerate(pl_pieces, start=1):
            print(f'{count}:{elem}')

    def print_status(self, status: str) -> None:
        if status == 'computer':
            print('\n' + 'Status: Computer is about to make a move. Press Enter to continue...')
        else:
            print('\n' + "Status: It's your turn to make a move. Enter your command.")

    def print_comp_wins(self) -> None:
        print('\n' + 'Status: The game is over. The computer won!')

    def print_pl_wins(self) -> None:
        print('\n' + 'Status: The game is over. You won!')

    def print_draw(self) -> None:
        print('\n' + "Status: The game is over. It's a draw!")

    def print_domino(self, domino: list) -> None:
        print(domino)

    def print_hidden_snake(self, snake: str) -> None:
        print(snake)
