from tictactoe import TicTacToe


my_game = TicTacToe()
command, levels = my_game.get_command_and_gamers()

if command == "start":
    my_game.set_levels_to_gamers(levels)
    my_game.greet()
    my_game.set_gamer_to_move("X")
    my_game.draw_table()

    while True:
        print(f"\n'{my_game.gamer}' moves")
        coordinates = my_game.get_new_coordinates(my_game.gamer)
        my_game.make_move(coordinates, my_game.gamer)
        my_game.draw_table()
        field_lines = my_game.get_field_lines(my_game.field)
        result = my_game.get_game_result(field_lines)
        if result != 'Game not finished':
            print(result)
            break
        my_game.change_gamer()
