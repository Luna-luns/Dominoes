class PrintFunctions:
    def print_header(self) -> None:
        print('=' * 70)

    def print_stock_size(self, stock: list) -> None:
        print(f'Stock size: {len(stock)}')

    def print_number_comp_pieces(self, comp_pieces: list) -> None:
        print(f'Computer pieces: {len(comp_pieces)}')

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
