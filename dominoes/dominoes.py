from dominoPieces import DominoPieces


full_domino_set = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 3],
                   [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6], [0, 0], [0, 1], [0, 2],
                   [0, 3], [0, 4], [0, 5], [0, 6]]

domino = DominoPieces()
domino_list = domino.make_domino_list(full_domino_set)

while True:
    comp_pieces = domino.split_dominoes(domino_list)
    result_comp = domino.has_snake_piece(comp_pieces)
    if result_comp:
        for elem in comp_pieces:
            domino_list.remove(elem)
        break

while True:
    plyer_pieces = domino.split_dominoes(domino_list)
    result_player = domino.has_snake_piece(plyer_pieces)
    if result_player:
        for elem in plyer_pieces:
            domino_list.remove(elem)
        break

stock_pieces = domino_list
biggest_comp_piece = domino.find_biggest_piece(comp_pieces)
biggest_player_piece = domino.find_biggest_piece(plyer_pieces)
domino_snake = domino.find_domino_snake(biggest_comp_piece, biggest_player_piece)
status = domino.set_status(domino_snake, comp_pieces)
if status == 'player':
    comp_pieces.remove(domino_snake)
    domino_snake = [domino_snake]
else:
    plyer_pieces.remove(domino_snake)
    domino_snake = [domino_snake]

print(stock_pieces, comp_pieces, plyer_pieces, domino_snake, status, sep='\n')
