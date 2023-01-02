import random

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
        self.gamers = {"X": None, "O": None}
        self.user_list = ("user", "easy", "medium", "hard")

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

    def get_command_and_gamers(self) -> tuple:
        while True:
            command, *levels = input("Input start/exit and command (user/easy/medium/hard): ").split(' ')
            if command == "exit":
                return command, levels
            if command not in ("start", "exit"):
                print("Bad parameters! Enter right command: 'start' or 'exit'.")
                continue
            if len(levels) != 2:
                print("Should be 2 gamers!")
                continue
            if any([level not in self.user_list for level in levels]):
                print("Bad parameters! Wrong gamer name.")
                continue
            return command, levels

    def set_levels_to_gamers(self, levels):
        self.gamers["X"] = levels[0]
        self.gamers["O"] = levels[1]

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

    def check_if_win_next_step(self, x: int, y: int, gamer: str) -> bool:
        field = self.field.copy()
        if field[x][y] == ' ':
            field[x][y] = gamer
            field_lines = self.get_field_lines(field)
            result = self.get_game_result(field_lines)
            field[x][y] = ' '
            if any([result == 'X wins', result == 'O wins', result == 'Draw']):
                return True

    def get_coordinates(self, gamer) -> tuple:
        if self.gamers[gamer] == "user":
            x, y = [int(i) for i in input("Enter the coordinates: ").split()]
            return x, y
        if self.gamers[gamer] == "easy":
            x, y = random.choice([1, 2, 3]), random.choice([1, 2, 3])
            return x, y
        if self.gamers[gamer] == "medium":
            for x in range(3):
                for y in range(3):
                    if self.check_if_win_next_step(x, y, gamer):
                        return x + 1, y + 1
                    if self.check_if_win_next_step(x, y, list({"X", "O"}.difference(gamer))[0]):
                        return x + 1, y + 1
            x, y = random.choice([1, 2, 3]), random.choice([1, 2, 3])
            return x, y
        if self.gamers[gamer] == "hard":
            pass

    def get_new_coordinates(self, gamer: str) -> Coordinates:
        while True:
            try:
                x, y = self.get_coordinates(gamer)

                if not (1 <= x <= 3 and 1 <= y <= 3):
                    print("Coordinates should be from 1 to 3!")
                    continue
                if not (self.field[x - 1][y - 1] == ' '):
                    print('This cell is occupied! Choose another one!')
                    continue
                return Coordinates(x, y)
            except ValueError:
                print("You should enter 2 numbers!")

    def get_field_lines(self, field: list) -> FieldLines:
        matrix = np.asarray(field)
        rows = [''.join(matrix[i, :]) for i in range(3)]
        cols = [''.join(matrix[:, i]) for i in range(3)]
        diag_lr = [''.join(matrix.diagonal())]
        diag_rl = [''.join(np.fliplr(matrix).diagonal())]
        return FieldLines(rows, cols, diag_lr, diag_rl)

    def get_game_result(self, field_lines: FieldLines) -> str:
        all_lines = field_lines.rows + field_lines.cols + field_lines.diag_lr + field_lines.diag_rl
        if any(map(lambda x: x == "XXX", all_lines)):  # "XXX" in row/col, returns X wins
            return 'X wins'
        elif any(map(lambda x: x == "OOO", all_lines)):  # "OOO" in row/col, returns O wins
            return 'O wins'
        elif all(map(lambda x: " " not in x, field_lines.rows)):  # there isn't " " (and nobody wins) in all table, returns Draw
            return 'Draw'
        elif any(map(lambda x: " " in x, field_lines.rows)):  # if any " " in all table, returns Game not finished
            return 'Game not finished'
        else:
            return 'Impossible'
