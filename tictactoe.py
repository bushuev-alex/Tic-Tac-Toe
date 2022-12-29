from game import TicTacToe


my_game = TicTacToe()
my_game.greet()
my_game.gamer = "X"
my_game.draw_table()

while True:
    print(f"\n'{my_game.gamer}' moves")
    coordinates = my_game.get_new_coordinates()
    my_game.make_move(coordinates, my_game.gamer)
    my_game.draw_table()
    rows, cols, diag_1, diag_2 = my_game.get_table_thrimers()
    result = my_game.get_result(rows, cols, diag_1, diag_2)
    if result != 'Game not finished':
        print(result)
        break
    my_game.change_gamer()
