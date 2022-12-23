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
    command = welcome(player).lower()
    if command == "g":
        print("play game")
        # game(args[1])
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
        command = input("Command: ").strip()
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
    pass


def display_usages():
    print("\033[33m1. Play game:\033[39m g, G")

    print("\033[33m2. See game instructions:\033[39m i, I")

    print("\033[33m3. See high scores:\033[39m s, S\n")


if __name__ == "__main__":
    main()
