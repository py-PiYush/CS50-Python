#! python3
# game.py: Simulates minesweeper game

import random, re, tabulate, sys
from tabulate import tabulate

from colorama import just_fix_windows_console

just_fix_windows_console()


class Board:
    bomb = "\033[33m*\033[39m"

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
                if self.board[row][col] == Board.bomb:
                    continue
                self.board[row][col] = self.get_surrounding_mines(row, col)

    def __str__(self) -> str:
        # return f"{self.player_bd()}"
        return tabulate(
            self.player_bd(),
            headers=range(self.dim_col),
            showindex=True,
            tablefmt="outline",
        )

    def plant_mines(self) -> None:
        """Plant mines on to the board"""
        mines_planted = 0
        # While mines planted are less than mines to be planted
        while mines_planted < self.num_mines:
            # Get random location
            row = random.randint(0, self.dim_row - 1)
            col = random.randint(0, self.dim_col - 1)
            # if already planted at that location, conitnue
            if self.board[row][col] == Board.bomb:
                continue

            # Plant mine
            self.board[row][col] = Board.bomb
            mines_planted += 1

    def get_surrounding_mines(self, row, col) -> int:
        """Return number of mines in surrounding cells of given cell"""
        # Check all surrounding cells of given location
        # Increment mine_count if mine is found
        mine_count = 0
        for r in range(max(0, row - 1), min(row + 2, self.dim_row)):
            for c in range(max(0, col - 1), min(col + 2, self.dim_col)):
                if self.board[r][c] == Board.bomb:
                    mine_count += 1
        return self.colored(mine_count)

    def colored(self, cnt) -> str:
        """Return colored str value of given integer"""
        if cnt == 0:
            return "\033[32m0\033[39m"
        if cnt in [1, 2]:
            return f"\033[34m{cnt}\033[39m"
        return f"\033[31m{cnt}\033[39m"

    def dig(self, row, col) -> bool:
        """Uncover cell at give row, col"""
        # Add this cell in visited celss
        self.visited.add((row, col))

        # If mine: return false
        if self.board[row][col] == Board.bomb:
            return False

        if self.board[row][col] != "\033[32m0\033[39m":
            return True
        # If number of surrounding mines is 0: recursively open all surrounding cells
        for r in range(max(0, row - 1), min(row + 2, self.dim_row)):
            for c in range(max(0, col - 1), max(col + 2, self.dim_col)):
                if (r, c) in self.visited:
                    continue
                self.dig(r, c)
        return True

    def player_bd(self):
        """Return board meant for players to see"""
        return [
            [
                self.board[row][col] if (row, col) in self.visited else "#"
                for col in range(self.dim_col)
            ]
            for row in range(self.dim_row)
        ]


def play(dim_row, dim_col, num_mines):
    board = Board(dim_row, dim_col, num_mines)
    board.make_board()

    # Repeat until all non-mine cells are uncovered
    while len(board.visited) < dim_row * dim_col - num_mines:
        # Ask user for location to dig
        print(board)
        row, col = map(
            int,
            re.split(
                r",\s*",
                input(
                    f"Enter the cell location as below pattern\nrow(0 - {dim_row - 1}), col(0 - {dim_col - 1}): "
                ).strip(),
            ),
        )
        res = board.dig(row, col)  # Dig at that location
        # If location is bomb, display entire board and game over
        if not res:
            board.visited = [(r, c) for c in range(dim_col) for r in range(dim_row)]
            print(board)
            sys.exit("GAME OVER !!!")

    print()
    board.visited = [(r, c) for r in range(dim_row) for c in range(dim_col)]
    print(board)
    print("CONGRATULATIONS!! You Won.")


play(2, 2, 1)
# b = Board(8, 8, 10)
# b.make_board()
# print(b)
