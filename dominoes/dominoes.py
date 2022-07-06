import random
from dominoPieces import DominoPieces
from printFunctions import PrintFunctions
from computer import Computer
from player import Player
from stock import Stock
from user_interface import UserInterface
from inputError import InputError


full_domino_set = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 3],
                   [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6], [0, 0], [0, 1], [0, 2],
                   [0, 3], [0, 4], [0, 5], [0, 6]]

domino = DominoPieces()
stock = Stock(full_domino_set)
stock_pieces = stock.stock
user = UserInterface()

while True:
    comp_pieces = domino.split_dominoes(stock_pieces)
    computer = Computer(comp_pieces)
    computer_pieces = computer.computer_pieces
    result_comp = domino.has_snake_piece(computer_pieces)
    if result_comp:
        for elem in computer_pieces:
            stock_pieces.remove(elem)
            stock = Stock(stock_pieces)
        break

while True:
    pl_pieces = domino.split_dominoes(stock_pieces)
    player = Player(pl_pieces)
    player_pieces = player.player_pieces
    result_player = domino.has_snake_piece(player_pieces)
    if result_player:
        for elem in player_pieces:
            stock_pieces.remove(elem)
            stock = Stock(stock_pieces)
        break

biggest_comp_piece = computer.find_biggest_piece()
biggest_player_piece = player.find_biggest_piece()
domino_snake = domino.find_domino_snake(biggest_comp_piece, biggest_player_piece)
status = domino.set_status(domino_snake, computer.computer_pieces)
if status == 'player':
    computer_pieces.remove(domino_snake)
    computer = Computer(computer_pieces)
else:
    player_pieces.remove(domino_snake)
    player = Player(player_pieces)

while True:
    print_function = PrintFunctions()
    print_function.print_header()
    print_function.print_stock_size(stock.stock_size)
    print_function.print_comp_pieces_size(computer.pieces_size)

    if len(domino_snake) > 36:
        converted_snake = domino.convert_to_list(domino_snake)
        if len(converted_snake) > 6:
            snake = domino.hide_pieces(converted_snake)
            print_function.print_hidden_snake(snake)
    else:
        print_function.print_domino_snake(domino_snake)

    print_function.print_enumerated_pl_pieces(player.player_pieces)

    if player.is_pl_out_off_pieces():
        print_function.print_pl_wins()
        break
    elif computer.is_comp_out_off_pieces():
        print_function.print_comp_wins()
        break
    elif len(domino_snake) > 2 and domino.is_end_num_times_wasted(domino_snake):
        print_function.print_draw()
        exit()

    print_function.print_status(status)

    if status == 'player':
        while True:
            try:
                command = user.ask_command()
                if user.is_input_number(command):
                    number = int(command)
                else:
                    raise InputError
                if player.is_valid_number(number):
                    break
                else:
                    raise InputError
            except InputError as error:
                print(error)

        if -6 <= number < 0 or 0 < number <= 6:
            domino_snake = player.player_move(domino_snake, number)
            status = 'computer'
        elif stock.stock_size > 0:
            taken_piece = random.choice(stock_pieces)
            stock_pieces.remove(taken_piece)
            player.player_pieces.append(taken_piece)
            status = 'computer'
        elif stock.stock_size == 0:
            status = 'computer'

        player = Player(player_pieces)
        stock = Stock(stock_pieces)
    else:
        number = computer.choose_number_to_move()

        if -6 <= number < 0 or 0 < number <= 6:
            domino_snake = computer.computer_move(domino_snake, number)
            status = 'player'
        elif stock.stock_size > 0:
            piece = random.choice(stock_pieces)
            stock_pieces.remove(piece)
            computer.computer_pieces.append(piece)
            status = 'player'
        elif stock.stock_size == 0:
            status = 'player'

        computer = Computer(computer_pieces)
        stock = Stock(stock_pieces)
