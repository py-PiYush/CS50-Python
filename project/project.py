#! python3
# project.py: Main file for handling all the functions of MinesweeperCLI

import os, sys, csv
from pyfiglet import Figlet
import pyttsx3
from game import play
from timeit import default_timer as timer
from datetime import timedelta


def main():
    """
    Main function: get user's name
    """
    player = input("Enter your name: ").strip()
    command = welcome(player)
    if command == "g":
        # print("play game")
        time = game()
        store_score(time, player)
    elif command == "i":
        print("instructions")
        # print(instructions())
    else:
        print("\033[33m=== HIGH SCORES ===\033[39m")
        scores = get_high_scores()
        for score in scores:
            print(f"{score['name']}: {score['time']} seconds")


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
    # engine = pyttsx3.init()
    # engine.say(f"Hello {player}, welcome to minesweeper")
    # engine.runAndWait()

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


def store_score(time, player):
    """Store time taken by user in csv file"""
    with open("scores.csv", "a") as file:
        fieldnames = ["name", "time"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"name": player, "time": round(time, 2)})


def get_high_scores():
    """Return top 5 scores"""
    with open("scores.csv", "r") as file:
        reader = csv.DictReader(file)
        top5 = []
        for row in sorted(reader, key=lambda x: x["time"], reverse=True)[:5]:
            top5.append({"name": row["name"], "time": row["time"]})
    return top5


def game():
    """
    Simulates Minesweeper game
    """
    print("========= DIFFICULTY =============")
    print("e for Easy: 6x6 with 5 mines")
    print("m for Medium: 8x8 with 10 mines")
    print("h for Hard: 16x16 with 40 mines\n")
    while True:
        mode = input("Enter difficulty mode: ")
        if mode in ["e", "m", "h"]:
            break
        else:
            print("\n\033[31mInvalid\033[39m")
    if mode == "e":
        row, col, mines = 6, 6, 5
    elif mode == "m":
        row, col, mines = 8, 8, 10
    elif mode == "h":
        row, col, mines = 16, 16, 40
    start = timer()
    play(row, col, mines)
    end = timer()
    time_taken = end - start
    print(f"\033[33mTime taken:\033[39m \033[32m{time_taken}\033[39m")
    return time_taken


def display_usages():
    print("\033[33m1. Play game:\033[39m g, G")

    print("\033[33m2. See game instructions:\033[39m i, I")

    print("\033[33m3. See high scores:\033[39m s, S\n")


if __name__ == "__main__":
    main()
