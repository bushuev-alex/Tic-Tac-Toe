from tictactoe import TicTacToe


my_game = TicTacToe()
my_game.greet()
my_game.gamer = "X"
my_game.draw_table()

while True:
    print(f"\n'{my_game.gamer}' moves")
    coordinates = my_game.get_new_coordinates()
    my_game.make_move(coordinates, my_game.gamer)
    my_game.draw_table()
    field_lines = my_game.get_field_lines()
    result = my_game.get_game_result(field_lines)
    if result != 'Game not finished':
        print(result)
        break
    my_game.change_gamer()
