import numpy as np
from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int


class TicTacToe:

    def __init__(self):
        self.lines = [[' ' for _ in range(3)] for _ in range(3)]
        self.gamer = None

    def greet(self):
        print("-----------------")
        print("  Greeting you   ")
        print("     in game     ")
        print("   Tic-Tac-Toe   ")
        print("-----------------")
        print("input format: x y")
        print("  x - row number ")
        print("  y - col number ")
        print("-----------------\n")

    def draw_table(self) -> None:
        print('---------')
        for line in self.lines:
            print('|', *line, '|', sep=' ')
        print('---------')

    def change_gamer(self) -> None:
        self.gamer = "X" if self.gamer == "O" else "O"

    def make_move(self, coordinates: Coordinates, gamer: str) -> None:
        self.lines[coordinates.x - 1][coordinates.y - 1] = gamer

    def get_new_coordinates(self) -> Coordinates:
        while True:
            try:
                x, y = [int(i) for i in input("Enter the coordinates: ").split()]

                if not (1 <= x <= 3 and 1 <= y <= 3):
                    print("Coordinates should be from 1 to 3!")
                    continue
                if not (self.lines[x - 1][y - 1] == ' '):
                    print('This cell is occupied! Choose another one!')
                    continue
                return Coordinates(x, y)
            except ValueError:
                print("You should enter 2 numbers!")

    def get_table_thrimers(self) -> list:
        matrix = np.asarray(self.lines)
        rows = [''.join(matrix[:, i]) for i in range(3)]
        cols = [''.join(matrix[i, :]) for i in range(3)]
        diag1 = [''.join(matrix.diagonal())]
        diag2 = [''.join(np.fliplr(matrix).diagonal())]
        return rows + cols + diag1 + diag2

    def result(self, thrimers: list):
        if any(map(lambda x: x == "XXX", thrimers)):
            return 'X wins'
        elif any(map(lambda x: x == "OOO", thrimers)):
            return 'O wins'
        elif all(map(lambda x: " " not in x, thrimers)):
            return 'Draw'
        elif any(map(lambda x: " " in x, thrimers)):
            return 'Game not finished'
        else:
            return 'Impossible'
