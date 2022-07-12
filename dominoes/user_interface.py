from player_hand import PlayerHand
from field import Field
from status import Status
from inputError import InputError


def print_header() -> None:
    print('=' * 70)


def print_stock_size(stock_size: int) -> None:
    print(f'Stock size: {stock_size}')


def print_comp_pieces_size(pieces_size: int) -> None:
    print(f'Computer pieces: {pieces_size}')


def print_field(field: Field) -> None:
    print(f'\n{field}\n')


def print_enumerated_player_hand(player_hand: PlayerHand) -> None:
    print('Your pieces:')
    for count, elem in player_hand.enumerate(start=1):
        print(f'{count}:{elem}')


def print_status(status: Status) -> None:
    if status == Status.PLAYER_MOVE:
        print('\n' + "Status: It's your turn to make a move. Enter your command.")
    elif Status.OPPONENT_MOVE == status:
        print('\n' + 'Status: Computer is about to make a move. Press Enter to continue...')
    elif Status.PLAYER_WIN == status:
        print("PLAYER WIN")
    elif Status.OPPONENT_WIN == status:
        print("OPPONENT_WIN")
    elif Status.DRAW == status:
        print("DRAW")


def ask_number() -> int:
    try:
        return int(input())
    except ValueError:
        raise InputError()
