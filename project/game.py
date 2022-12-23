#! python3
# game.py: Simulates minesweeper game

import random
from tabulate import tabulate
from colorama import just_fix_windows_console

just_fix_windows_console()


class Board:
    def __init__(self, dim_row, dim_col, num_mines) -> None:
        self.board = [[None for _ in range(dim_col)] for __ in range(dim_row)]
        self.dim_row = dim_row  # row dimension
        self.dim_col = dim_col  # col dimension
        self.num_mines = num_mines  # number of mines
        self.visited = set()  # to keep track of visited cells

    def make_board(self):
        """Make board with given dimensions and number of mines"""
        # Plant mines at random location
        self.plant_mines()

        # Set every other cell with number of surrounding mines
        for row in range(self.dim_row):
            for col in range(self.dim_col):
                if self.board[row][col] == "\033[33m*\033[39m":
                    continue
                self.board[row][col] = self.get_surrounding_mines(row, col)

    def __str__(self) -> str:
        return tabulate(self.board)

    def plant_mines(self) -> None:
        """Plant mines on to the board"""
        mines_planted = 0
        # While mines planted are less than mines to be planted
        while mines_planted < self.num_mines:
            # Get random location
            row = random.randint(0, self.dim_row - 1)
            col = random.randint(0, self.dim_col - 1)
            # if already planted at that location, conitnue
            if self.board[row][col] == "\033[33m*\033[39m":
                continue

            # Plant mine
            self.board[row][col] = "\033[33m*\033[39m"
            mines_planted += 1

    def get_surrounding_mines(self, row, col) -> int:
        """Return number of mines in surrounding cells of given cell"""
        # Check all surrounding cells of given location
        # Increment mine_count if mine is found
        mine_count = 0
        for r in range(max(0, row - 1), min(row + 2, self.dim_row)):
            for c in range(max(0, col - 1), min(col + 2, self.dim_col)):
                if self.board[r][c] == "\033[33m*\033[39m":
                    mine_count += 1
        return self.colored(mine_count)

    def colored(self, cnt) -> str:
        """Return colored str value of given integer"""
        if cnt == 0:
            return "\033[32m0\033[39m"
        if cnt in [1, 2]:
            return f"\033[34m{cnt}\033[39m"
        return f"\033[31m{cnt}\033[39m"


b = Board(8, 8, 10)
b.make_board()
print(b)
