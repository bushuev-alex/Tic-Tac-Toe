import numpy as np
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Coordinates:
    x: int
    y: int


@dataclass(slots=True, frozen=True)
class FieldLines:
    rows: list
    cols: list
    diag_lr: list
    diag_rl: list


class TicTacToe:

    def __init__(self):
        self.field = [[' ' for _ in range(3)] for _ in range(3)]
        self.gamer = None

    def set_gamer_to_move(self, gamer: str) -> None:
        self.gamer = gamer

    def greet(self):
        print("\n-----------------")
        print("  Greeting you   ")
        print("     in game     ")
        print("   Tic-Tac-Toe   ")
        print("-----------------")
        print("input format: x y")
        print("  x - row number ")
        print("  y - col number ")
        print("-----------------\n")

    def draw_table(self) -> None:
        print(' ', ' ', '1', '2', '3')
        print('  ---------')
        for n, row in enumerate(self.field):
            print(n + 1, '|', *row, '|')
        print('  ---------')

    def change_gamer(self) -> None:
        self.gamer = "X" if self.gamer == "O" else "O"

    def make_move(self, coordinates: Coordinates, gamer: str) -> None:
        self.field[coordinates.x - 1][coordinates.y - 1] = gamer

    def get_new_coordinates(self) -> Coordinates:
        while True:
            try:
                x, y = [int(i) for i in input("Enter the coordinates: ").split()]

                if not (1 <= x <= 3 and 1 <= y <= 3):
                    print("Coordinates should be from 1 to 3!")
                    continue
                if not (self.field[x - 1][y - 1] == ' '):
                    print('This cell is occupied! Choose another one!')
                    continue
                return Coordinates(x, y)
            except ValueError:
                print("You should enter 2 numbers!")

    def get_field_lines(self) -> FieldLines:
        matrix = np.asarray(self.field)
        rows = [''.join(matrix[:, i]) for i in range(3)]
        cols = [''.join(matrix[i, :]) for i in range(3)]
        diag_lr = [''.join(matrix.diagonal())]
        diag_rl = [''.join(np.fliplr(matrix).diagonal())]
        return FieldLines(rows, cols, diag_lr, diag_rl)

    def get_game_result(self, field_lines: FieldLines) -> str:
        all_lines = field_lines.rows + field_lines.cols + field_lines.diag_lr + field_lines.diag_rl
        if any(map(lambda x: x == "XXX", all_lines)):  # "XXX" in row/col, returns X wins
            return 'X wins'
        elif any(map(lambda x: x == "OOO", all_lines)):  # "OOO" in row/col, returns O wins
            return 'O wins'
        elif all(map(lambda x: " " not in x, field_lines.rows)):  # no " " in all table and nobody wins, returns Draw
            return 'Draw'
        elif any(map(lambda x: " " in x, field_lines.rows)):  # if any " " in all table, returns Game not finished
            return 'Game not finished'
        else:
            return 'Impossible'
