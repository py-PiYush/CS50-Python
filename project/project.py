#! python3
# project.py: Main file for handling all the functions of MinesweeperCLI

import os, sys
from pyfiglet import Figlet
import pyttsx3


def main():
    """
    Main function: get user's name
    """
    player = input("Enter your name: ").strip()
    command = welcome(player)
    if command == "g":
        # print("play game")
        game()
    elif command == "i":
        print("instructions")
        # print(instructions())
    else:
        print("high scores")
        # scores = get_high_scores()
        # for k, v in scores.items():
        #     print(f"{k}: {v}")


def welcome(player):
    """
    Shows welcome screen, takes and return command line arguments from the user
    """
    # Clear terminal
    os.system("cls" if os.name == "nt" else "clear")

    # Fancy welcome to minesweeper
    f1 = Figlet(font="slant")
    print(f1.renderText("Welcome To MineSweeper"))
    f2 = Figlet(font="small")
    print(f2.renderText("The CLI version"))
    print()

    # Text to speech
    engine = pyttsx3.init()
    engine.say(f"Hello {player}, welcome to minesweeper")
    engine.runAndWait()

    # Display command line usages
    display_usages()

    # Get command
    while True:
        command = input("Command: ").strip().lower()
        if command in ["i", "g", "s"]:
            break
        else:
            print("\n\033[31mInvalid Command\033[39m")
            display_usages()
    return command


def instructions():
    """Shows instructions to play game"""
    pass


def get_high_scores():
    """Prints top 5 scores"""
    pass


def game():
    """
    Simulates Minesweeper game
    """
    print("========= DIFFICULTY =============")
    print("e for Easy: 8x8 with 10 mines")
    print("m for Medium: 16x16 with 40 mines")
    print("h for Hard: 30x16 with 99 mines\n")
    while True:
        mode = input("Enter difficulty mode: ")
        if mode in ["e", "m", "h"]:
            break
        else:
            print("\n\033[31mInvalid\033[39m")
    if mode == "e":
        row, col, mines = 8, 8, 10
    elif mode == "m":
        row, col, mines = 16, 16, 40
    elif mode == "h":
        row, col, mines = 30, 16, 99
    # play(row, col, mines)


def display_usages():
    print("\033[33m1. Play game:\033[39m g, G")

    print("\033[33m2. See game instructions:\033[39m i, I")

    print("\033[33m3. See high scores:\033[39m s, S\n")


if __name__ == "__main__":
    main()
