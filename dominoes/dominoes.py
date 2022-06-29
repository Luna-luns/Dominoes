import random


def split_dominoes(domino: list) -> list:
    return random.sample(domino, 7)


def find_double_pieces(pieces: list) -> list:
    for i in pieces:
        if i in snake_dominoes:
            return pieces


def find_biggest_piece(pieces: list) -> list:
    total_sum = 0
    biggest_piece = None

    for element in pieces:
        total = sum(element)

        if total > total_sum:
            total_sum = total
            biggest_piece = element

    return biggest_piece


def find_domino_snake(c_piece: list, pl_piece: list) -> list:
    if c_piece > pl_piece:
        return c_piece
    else:
        return pl_piece


full_domino_set = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 3],
                   [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6], [0, 0], [0, 1], [0, 2],
                   [0, 3], [0, 4], [0, 5], [0, 6]]

snake_dominoes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]

while True:

    comp_pieces = split_dominoes(full_domino_set)
    result = find_double_pieces(comp_pieces)

    if result is not None:
        for elem in result:
            full_domino_set.remove(elem)
        break

while True:

    plyer_pieces = split_dominoes(full_domino_set)
    result = find_double_pieces(plyer_pieces)

    if result is not None:
        for elem in result:
            full_domino_set.remove(elem)
        break


stock_pieces = full_domino_set
biggest_comp_piece = find_biggest_piece(comp_pieces)
biggest_player_piece = find_biggest_piece(plyer_pieces)
domino_snake = find_domino_snake(biggest_comp_piece, biggest_player_piece)
status = None
if domino_snake in comp_pieces:
    comp_pieces.remove(domino_snake)
    domino_snake = [domino_snake]
    status = 'player'
else:
    plyer_pieces.remove(domino_snake)
    domino_snake = [domino_snake]
    status = 'computer'

print(stock_pieces, comp_pieces, plyer_pieces, domino_snake, status, sep='\n')
